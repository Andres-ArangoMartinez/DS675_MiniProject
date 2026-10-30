"""Validate the public transcript appendix, optionally against private recovered views."""
import argparse
from collections import Counter, defaultdict
import csv
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'evidence/ai_interactions'

def digest(data):
    return hashlib.sha256(data).hexdigest()

def rows(name):
    with (BASE/name).open(encoding='utf-8', newline='') as handle:
        return list(csv.DictReader(handle))

def validate(originals=None):
    manifest=json.loads((BASE/'manifest.json').read_text(encoding='utf-8'))
    sources=manifest['sources']
    assert len(sources)==16
    assert {s['source_id'] for s in sources}=={f'T{i:02}' for i in range(1,17)}
    continuation=next(s for s in sources if s['source_id']=='T16')
    assert continuation['continuation_of']=='T02'
    assert continuation['raw_continuation']['raw_first_record']==11414
    assert continuation['raw_continuation']['previous_raw_prefix_records']==11413
    attachment=manifest['provided_request_attachment']
    attachment_bytes=(BASE/attachment['file']).read_bytes()
    assert len(attachment_bytes)==attachment['bytes'] and digest(attachment_bytes)==attachment['sha256']
    logs=rows('redactions.csv')
    grouped=defaultdict(list)
    for row in logs: grouped[row['source_id']].append(row)
    assert len({r['redaction_id'] for r in logs})==len(logs)
    allowed={'credential','credential-fragment','access-token','restricted-course-link','image-payload'}
    all_parts=set(); original_checks=0; content={}
    for source in sources:
        sid=source['source_id']; parts=source['parts']; cursor=0; blocks=[]
        for i,part in enumerate(parts,1):
            p=(BASE/part['file']).resolve()
            assert p.is_relative_to(BASE.resolve()) and p.suffix=='.txt'
            assert p.name==f'part-{i:03}.txt'
            data=p.read_bytes(); assert digest(data)==part['sha256']
            assert len(data)==part['bytes'] and len(data)<=390000
            text=data.decode('utf-8')
            assert part['character_start']==cursor
            cursor+=len(text); assert part['character_end']==cursor
            blocks.append(text); all_parts.add(p)
        text=''.join(blocks); content[sid]=text
        assert len(text.encode('utf-8'))==source['public_bytes']
        assert digest(text.encode('utf-8'))==source['public_joined_sha256']
        entries=grouped[sid]
        assert len(entries)==source['redactions']
        end=0
        for entry in entries:
            a=int(entry['source_character_start']); b=int(entry['source_character_end'])
            assert a>=end and b>a; end=b
            assert entry['category'] in allowed
            assert text.count(entry['marker'])==1
            location=entry['public_locator']; filename,line=location.rsplit('#L',1)
            target=(BASE/filename).read_bytes().decode('utf-8').split('\n')
            assert entry['marker'] in target[int(line)-1]
        # Bounded public scan: recognizable credentials and unreviewed image bytes.
        assert not re.search(r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{20,}|(?:AKIA|ASIA)[A-Z0-9]{16})',text)
        assert not re.search(r'data:image/[^;,\s]+;base64,[A-Za-z0-9+/=]{200,}',text)
        if originals is not None:
            archive=source.get('private_archive','DS675_AI_Transcripts_'+source['platform'])
            private=Path(originals)/archive/source['source_relative']
            data=private.read_bytes(); assert digest(data)==source['private_readable_sha256']
            original=data.decode('utf-8'); rebuilt=[]; cursor=0
            for entry in entries:
                a=int(entry['source_character_start']); b=int(entry['source_character_end'])
                assert original.count('\n',0,a)+1==int(entry['source_text_line'])
                rebuilt.extend([original[cursor:a],entry['marker']]); cursor=b
            rebuilt.append(original[cursor:])
            assert ''.join(rebuilt)==text, f'Undocumented change in {sid}'
            assert digest(private.read_bytes())==source['private_readable_sha256']
            if source.get('continuation_of'):
                raw=source['raw_continuation']
                candidates=list((Path(originals)/archive/'original_sessions').glob('*.jsonl'))
                assert len(candidates)==1
                h=hashlib.sha256(); prefix=hashlib.sha256(); remaining=raw['previous_raw_prefix_bytes']; size=0
                with candidates[0].open('rb') as handle:
                    for block in iter(lambda:handle.read(1048576),b''):
                        h.update(block); size+=len(block)
                        if remaining:
                            n=min(remaining,len(block)); prefix.update(block[:n]); remaining-=n
                assert size==raw['raw_snapshot_bytes']
                assert h.hexdigest()==raw['raw_snapshot_sha256']
                assert remaining==0 and prefix.hexdigest()==raw['previous_raw_prefix_sha256']
            original_checks+=1
    assert all_parts=={p.resolve() for p in BASE.rglob('part-*.txt')}
    cases=rows('contribution_links.csv')
    assert len(cases)==31
    assert {r['activity_id'] for r in cases}=={f'A{i:02}' for i in range(1,11)}
    for row in cases:
        filename,line=row['public_locator'].rsplit('#L',1)
        text=(BASE/filename).read_bytes().decode('utf-8').split('\n')
        assert 0<int(line)<=len(text)
        anchor=text[int(line)-1]
        assert ('source-line-' if row['platform']=='Codex' else 'message-') in anchor
    construction=rows('repository_construction_contributions.csv')
    assert len(construction)==5
    for row in construction:
        assert row['student_contribution'] and row['AI_assistance'] and row['evidence_boundary']
        for field in ['student_locator','AI_locator','execution_locator']:
            for locator in filter(None,row[field].split(';')):
                filename,line=locator.rsplit('#L',1)
                lines=(BASE/filename).read_bytes().decode('utf-8').split('\n')
                assert 0<int(line)<=len(lines)
                assert 'source-line-' in lines[int(line)-1]
    guide=(BASE/'README.md').read_text(encoding='utf-8')
    assert all(f'### A{i:02}.' in guide for i in range(1,11))
    guide_links=0; guide_anchors=0
    for destination in re.findall(r'\]\(([^\s]+?)\)',guide):
        if destination.startswith(('http:','https:','mailto:','#')):continue
        filename,_,fragment=destination.partition('#')
        target=(BASE/filename).resolve()
        assert target.is_relative_to(ROOT.resolve()) and target.exists(),destination
        guide_links+=1
        if fragment.startswith('L') and target.suffix=='.txt':
            line=int(fragment[1:]); lines=target.read_bytes().decode('utf-8').split('\n')
            assert 0<line<=len(lines),destination
            assert '<a id="source-line-' in lines[line-1] or '<a id="message-' in lines[line-1],destination
            guide_anchors+=1
    result={'status':'PASS','source_views':len(sources),'public_parts':len(all_parts),
            'documented_redactions':len(logs),'redactions_by_category':dict(Counter(r['category'] for r in logs)),
            'contribution_links':len(cases),'public_hashes_and_locators_match':True,
            'repository_construction_activities':len(construction),
            'guide_local_links_checked':guide_links,'guide_transcript_anchors_checked':guide_anchors,
            'provided_request_attachment_hash_matches':True,
            'original_views_compared_without_modification':original_checks,
            'privacy_scan_limit':'Pattern checks cover the specified credential and inline-image formats; source coverage and privacy treatment are documented.',
            'historical_completeness_certified':False}
    print(json.dumps(result,indent=2))
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--originals',type=Path,help='Optional private directory containing both recovered archives. Never uploaded.')
    args=parser.parse_args()
    validate(args.originals)
