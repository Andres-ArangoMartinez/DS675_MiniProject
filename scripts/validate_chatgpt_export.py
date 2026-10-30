"""Validate the export supplement, optionally against the private ZIP source."""
import argparse
from collections import Counter, defaultdict
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
BASE = ROOT/'evidence/ai_interactions/chatgpt_export'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read_csv(name):
    with (BASE/name).open(encoding='utf-8-sig', newline='') as h:
        return list(csv.DictReader(h))


def validate(archive=None):
    manifest = json.loads((BASE/'manifest.json').read_text(encoding='utf-8'))
    conversations = manifest['conversations']
    for name, digest in manifest['derivation_code_sha256'].items():
        assert sha((ROOT/name).read_bytes()) == digest, name
    legacy = json.loads((ROOT/'evidence/ai_interactions/manifest.json').read_text(encoding='utf-8'))
    old_ids = {s['id'] for s in legacy['sources'] if s['platform']=='ChatGPT'}
    assert {c['conversation_id'] for c in conversations} == old_ids | {'6ae35e86-9b68-83ea-a355-b938f88ef913'}
    for name, digest in manifest['support_files_sha256'].items():
        path = (BASE/name).resolve()
        assert path.is_relative_to(BASE.resolve()) and sha(path.read_bytes())==digest, name
    for name, digest in manifest['legacy_preservation_sha256'].items():
        assert sha((ROOT/name).read_bytes())==digest, f'Legacy evidence changed: {name}'
    redactions=read_csv('redactions.csv')
    grouped=defaultdict(list)
    for row in redactions:
        grouped[row['conversation_id']].append(row)
    messages=read_csv('message_index.csv')
    assert len(messages)==manifest['visible_messages']
    assert len({m['message_id'] for m in messages})==len(messages)
    assert dict(Counter(m['role'] for m in messages))==manifest['roles']
    texts={}; all_parts=set(); locators={}
    for conv in conversations:
        cid=conv['conversation_id'];blocks=[];cursor=0
        for i,part in enumerate(conv['parts'],1):
            path=(BASE/part['file']).resolve()
            assert path.is_relative_to(BASE.resolve())
            assert path.name==f'segment-{i:03}.txt'
            data=path.read_bytes();assert len(data)==part['bytes']<=390000 and sha(data)==part['sha256']
            text=data.decode('utf-8');assert part['character_start']==cursor
            cursor+=len(text);assert part['character_end']==cursor
            blocks.append(text);all_parts.add(path)
        joined=''.join(blocks);texts[cid]=joined
        assert len(joined)==conv['public_characters'] and sha(joined.encode())==conv['public_joined_sha256']
        assert len(grouped[cid])==conv['redactions']
        assert len([m for m in messages if m['conversation_id']==cid])==conv['visible_messages']
        end=0
        for row in sorted(grouped[cid],key=lambda x:int(x['source_character_start'])):
            a,z=int(row['source_character_start']),int(row['source_character_end'])
            assert a>=end and z>a;end=z
            assert joined.count(row['marker'])==1
            name,line=row['public_locator'].rsplit('#L',1)
            assert row['marker'] in (BASE/name).read_bytes().decode().split('\n')[int(line)-1]
        assert not re.search(r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{20,}|(?:AKIA|ASIA)[A-Z0-9]{16})',joined)
        assert not re.search(r'data:image/[^;,\s]+;base64,[A-Za-z0-9+/=]{200,}',joined)
        assert not re.search(r'https?://[^\s<>"\]]*zoom\.us/(?:rec/|j/|w/)[^\s<>"\]]+',joined,re.I)
    assert all_parts=={p.resolve() for p in BASE.rglob('segment-*.txt')}
    for m in messages:
        name,line=m['public_locator'].rsplit('#L',1)
        target=(BASE/name).resolve();assert target in all_parts
        assert (f'<a id="message-{m["message_id"]}"></a>' in target.read_bytes().decode().split('\n')[int(line)-1])
        locators[(m['conversation_id'],m['message_id'])]=m
    recovery=read_csv('recovery_map.csv')
    assert len(recovery)==manifest['legacy_messages_matched']==82
    assert len({(x['conversation_id'],x['message_id']) for x in recovery})==len(recovery)
    for row in recovery:
        m=locators[(row['conversation_id'],row['message_id'])]
        assert m['role']==row['role'] and m['public_locator']==row['public_locator']
        assert int(row['export_text_characters'])==int(m['native_text_characters'])>0
        assert row['export_text_available']=='True'
    assert sum(x['previous_status']=='reference_only' for x in recovery)==manifest['prior_reference_only_bodies_recovered']==19
    assert sum(x['previous_status']=='truncated' for x in recovery)==manifest['prior_truncated_messages_recovered']==5
    assert sum(x['previously_pending_reference']=='True' for x in recovery)==manifest['pending_reference_bodies_resolved']==15
    cases=read_csv('contribution_links.csv')
    assert {'A11','A12'} <= {x['activity_id'] for x in cases}
    guide = (ROOT/'evidence/ai_interactions/README.md').read_text(encoding='utf-8')
    assert all(f'### {aid}.' in guide for aid in ['A11','A12'])
    for row in cases:
        m=locators[(row['conversation_id'],row['message_id'])]
        assert row['role']==m['role'] and row['public_locator']==m['public_locator']
    proof=json.loads((BASE/'prompt_provenance.json').read_text(encoding='utf-8'))['checked_prompts']
    for row in proof:
        raw=(BASE/row['provided_file']).read_bytes();assert sha(raw)==row['provided_file_sha256']
        d=json.loads(raw.decode('utf-8-sig'))
        norm=json.dumps(d,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()
        assert sha(norm)==row['canonical_json_sha256']
        m=locators[(row['conversation_id'],row['assistant_message_id'])]
        assert m['role']=='assistant' and m['public_locator']==row['assistant_public_locator']
        conversation_text = texts[row['conversation_id']]
        marker = f'<a id="message-{row["assistant_message_id"]}"></a>'
        start = conversation_text.index(marker)
        end = conversation_text.find('\n<a id="message-', start+len(marker))
        block = conversation_text[start:] if end < 0 else conversation_text[start:end]
        candidates = []
        for match in re.finditer(r'\{\s*"role"\s*:', block):
            try: obj, consumed = json.JSONDecoder().raw_decode(block[match.start():])
            except json.JSONDecodeError: continue
            candidates.append(sha(json.dumps(obj,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()))
        assert row['canonical_json_sha256'] in candidates, row['provided_file']

    assert not list(BASE.rglob('*.zip')) and not list(BASE.rglob('*.jsonl'))
    source_checks=0
    if archive is None:
        source_record = json.loads((BASE/'validation.json').read_text(encoding='utf-8'))
        assert source_record['manifest_sha256'] == sha((BASE/'manifest.json').read_bytes())
        assert source_record['validator_sha256'] == sha(Path(__file__).read_bytes())
        assert source_record['private_export_conversations_compared'] == len(conversations)
    if archive is not None:
        from scripts.import_chatgpt_export import selected_conversations,render_conversation,canonical
        archive=Path(archive)
        assert not archive.resolve().is_relative_to(ROOT.resolve())
        h=hashlib.sha256()
        with archive.open('rb') as handle:
            for block in iter(lambda:handle.read(8*1024*1024),b''):h.update(block)
        assert archive.stat().st_size==manifest['archive_bytes'] and h.hexdigest()==manifest['archive_sha256']
        native=selected_conversations(archive,{c['conversation_id'] for c in conversations})
        for conv in conversations:
            cid=conv['conversation_id'];c,member,member_hash=native[cid]
            assert member==conv['zip_member'] and member_hash==conv['zip_member_sha256']
            source,source_messages=render_conversation(c)
            excluded = Counter(n['message']['content']['content_type'] for n in c['mapping'].values() if n.get('message') and n['message']['content']['content_type'] not in {'text','multimodal_text'})
            assert dict(excluded) == conv['non_text_model_record_counts_kept_private']
            assert len(source)==conv['source_characters'] and sha(source.encode())==conv['private_readable_sha256']
            cursor=0;pieces=[]
            for row in sorted(grouped[cid],key=lambda x:int(x['source_character_start'])):
                a,z=int(row['source_character_start']),int(row['source_character_end'])
                pieces.extend([source[cursor:a],row['marker']]);cursor=z
            pieces.append(source[cursor:]);assert ''.join(pieces)==texts[cid],f'Unregistered source change: {cid}'
            expected={(m['conversation_id'],m['message_id']):m for m in source_messages}
            public={key:value for key,value in locators.items() if key[0]==cid}
            assert set(expected)==set(public)
            for key,m in expected.items():
                for field in ['role','content_type','native_content_sha256','native_text_characters','created_utc','node_id']:
                    assert str(m[field])==str(public[key][field]),(key,field)
            for row in proof:
                if row['conversation_id']!=cid:continue
                msg=next(n['message'] for n in c['mapping'].values() if n.get('message') and n['message']['id']==row['assistant_message_id'])
                text='\n'.join(x for x in msg['content'].get('parts',[]) if isinstance(x,str));candidates=[]
                for match in re.finditer(r'\{\s*"role"\s*:',text):
                    try:obj,end=json.JSONDecoder().raw_decode(text[match.start():])
                    except json.JSONDecodeError:continue
                    candidates.append(sha(canonical(obj)))
                assert row['canonical_json_sha256'] in candidates
            source_checks+=1
    result={'status':'PASS','checked_utc':datetime.now(timezone.utc).isoformat(),
            'manifest_sha256':sha((BASE/'manifest.json').read_bytes()),
            'validator_sha256':sha(Path(__file__).read_bytes()),
            'export_conversations':len(conversations),'visible_messages':len(messages),'message_roles':manifest['roles'],
            'legacy_messages_matched':len(recovery),'reference_only_bodies_recovered':19,
            'pending_reference_bodies_resolved':15,'truncated_messages_recovered':5,
            'registered_export_redactions':len(redactions),'extended_contribution_cases':len(cases),
            'supplied_prompts_equal_to_assistant_drafts':len(proof),'legacy_files_preserved':len(manifest['legacy_preservation_sha256']),
            'private_export_conversations_compared':source_checks,'historical_completeness_certified':False}
    print(json.dumps(result,indent=2))
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive',type=Path,help='Optional private ZIP for native-source comparison; never uploaded.')
    args=parser.parse_args();result=validate(args.archive)
    output = 'validation.json' if args.archive is not None else 'public_validation.json'
    (BASE/output).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
