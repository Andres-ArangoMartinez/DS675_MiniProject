"""Create a scoped public supplement from a student-supplied ChatGPT ZIP export.

The archive stays private. The fixed allowlist comprises the eleven legacy chats
and one directly related recovery handoff. Existing evidence is never replaced.
"""
import argparse
from collections import Counter
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'evidence/ai_interactions'
OUT = BASE / 'chatgpt_export'
RECOVERY_ID = '6ae35e86-9b68-83ea-a355-b938f88ef913'
VISIBLE_TYPES = {'text', 'multimodal_text'}
MAX_PART_BYTES = 390000


def sha(data):
    return hashlib.sha256(data).hexdigest()


def utc(value):
    return datetime.fromtimestamp(value, timezone.utc).isoformat() if value is not None else 'not recorded'


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode('utf-8')


def selected_conversations(archive, selected):
    found = {}
    with zipfile.ZipFile(archive) as source:
        for name in source.namelist():
            if not re.fullmatch(r'conversations-\d+\.json', name):
                continue
            raw = source.read(name)
            for item in json.loads(raw):
                cid = item.get('conversation_id') or item['id']
                if cid in selected:
                    assert cid not in found, f'Duplicate selected conversation: {cid}'
                    found[cid] = (item, name, sha(raw))
    assert set(found) == set(selected), f'Missing selected conversations: {set(selected)-set(found)}'
    return found


def ordered_visible(conversation):
    mapping = conversation['mapping']
    active = set()
    node = conversation.get('current_node')
    while node is not None:
        assert node not in active, 'Cycle in active message path'
        active.add(node)
        node = mapping[node].get('parent')
    depth_cache = {}
    def depth(nid, visiting=None):
        if nid in depth_cache:
            return depth_cache[nid]
        visiting = set() if visiting is None else visiting
        assert nid not in visiting, 'Cycle in message mapping'
        visiting.add(nid)
        parent = mapping[nid].get('parent')
        value = 0 if parent is None else depth(parent, visiting)+1
        visiting.remove(nid)
        depth_cache[nid] = value
        return value
    nodes = []
    for nid, node in mapping.items():
        m = node.get('message')
        if m and m['author']['role'] in {'user', 'assistant'} and m['content']['content_type'] in VISIBLE_TYPES:
            nodes.append((nid, node, nid in active))
    nodes.sort(key=lambda x: (depth(x[0]), x[1]['message'].get('create_time') or 0, x[0]))
    return nodes


def render_content(content):
    blocks = []
    for i, part in enumerate(content.get('parts', [])):
        if isinstance(part, str):
            blocks.append(part)
        else:
            kind = part.get('content_type', 'non-text')
            pointer = part.get('asset_pointer', 'not recorded')
            blocks.append(f'[Export non-text part {i}: {kind}; asset reference: {pointer}; binary retained privately.]')
    text = '\n'.join(blocks)
    if not text.strip():
        text = '[Export message has no text body; attachment metadata remains in the private archive.]'
    return text


def render_conversation(c):
    cid = c.get('conversation_id') or c['id']
    header = (f'# ChatGPT export conversation\n\nConversation ID: {cid}\n'
              f'Original title: {c.get("title", "")}\n'
              f'Created UTC: {utc(c.get("create_time"))}\nUpdated UTC: {utc(c.get("update_time"))}\n'
              'Source: student-supplied account export; original language and text retained.\n'
              'Scope: user/assistant text and multimodal text in mapping order; non-text model records remain private.\n\n')
    rows = []
    text = header
    for nid, node, active in ordered_visible(c):
        m = node['message']
        mid = m['id']
        body = render_content(m['content'])
        text += (f'<a id="message-{mid}"></a>\n'
                 f'## {m["author"]["role"]} | {utc(m.get("create_time"))} | {mid}\n\n'
                 f'Export node: {nid}\nParent node: {node.get("parent")}\n'
                 f'Active branch: {str(active).lower()}\nContent type: {m["content"]["content_type"]}\n\n'
                 '### Original message body\n\n'+body+'\n\n')
        rows.append({'conversation_id': cid, 'node_id': nid, 'message_id': mid,
                     'role': m['author']['role'], 'created_raw': m.get('create_time'),
                     'created_utc': utc(m.get('create_time')), 'parent_node': node.get('parent'),
                     'active_branch': active, 'content_type': m['content']['content_type'],
                     'native_content_sha256': sha(canonical(m['content'])),
                     'native_text_characters': sum(len(x) for x in m['content'].get('parts', []) if isinstance(x, str)),
                     'non_text_parts': sum(not isinstance(x, str) for x in m['content'].get('parts', []))})
    return text, rows


def sensitive_literals(originals):
    manifest = json.loads((BASE/'manifest.json').read_text(encoding='utf-8'))
    sources = {s['source_id']: s for s in manifest['sources']}
    with (BASE/'redactions.csv').open(encoding='utf-8-sig', newline='') as h:
        records = list(csv.DictReader(h))
    cache = {}
    literals = {}
    for row in records:
        if row['category'] == 'image-payload':
            continue
        sid = row['source_id']
        if sid not in cache:
            s = sources[sid]
            archive = s.get('private_archive', 'DS675_AI_Transcripts_'+s['platform'])
            raw = (Path(originals)/archive/s['source_relative']).read_bytes()
            assert sha(raw) == s['private_readable_sha256']
            cache[sid] = raw.decode('utf-8')
        value = cache[sid][int(row['source_character_start']):int(row['source_character_end'])]
        if len(value) >= 8:
            literals[value] = row['category']
    return literals


def redact(text, literals, offset):
    spans = []
    for value, category in literals.items():
        spans.extend((m.start(), m.end(), category) for m in re.finditer(re.escape(value), text))
    patterns = [
        ('access-token', r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{20,}|(?:AKIA|ASIA)[A-Z0-9]{16})'),
        ('restricted-course-link', r'https?://[^\s<>"\]]*zoom\.us/(?:rec/|j/|w/)[^\s<>"\]]+'),
        ('restricted-course-link', r'https?://[^\s<>"\]]*(?:instructure\.com/courses/|panopto\.com/Panopto/Pages/Viewer)[^\s<>"\]]+'),
        ('image-payload', r'data:image/[^;,\s]+;base64,[A-Za-z0-9+/=]{200,}')]
    for category, pattern in patterns:
        spans.extend((m.start(), m.end(), category) for m in re.finditer(pattern, text, re.I))
    for m in re.finditer(r'(?:password|contrase\u00f1a)\s*[:=]\s*["\']?([^\s"\'<>`]{6,})', text, re.I):
        spans.append((m.start(1), m.end(1), 'credential'))
    for m in re.finditer(r'(?:[?&]|\b)(?:X-Amz-Signature|X-Amz-Security-Token|AWSAccessKeyId|access_token|refresh_token|sig)=([^&\s<>"\]]+)', text, re.I):
        spans.append((m.start(1), m.end(1), 'access-token'))
    merged = []
    for start, end, category in sorted(spans, key=lambda x: (x[0], -x[1])):
        if merged and start < merged[-1][1]:
            a, z, cats = merged[-1]
            merged[-1] = (a, max(z, end), cats | {category})
        else:
            merged.append((start, end, {category}))
    pieces = []
    cursor = 0
    rows = []
    for i, (start, end, categories) in enumerate(merged, offset+1):
        rid = f'CGPT-REDACTION-{i:04}'
        marker = f'[[{rid}]]'
        pieces += [text[cursor:start], marker]
        rows.append({'redaction_id': rid, 'source_character_start': start, 'source_character_end': end,
                     'category': ';'.join(sorted(categories)), 'marker': marker,
                     'reason': 'Credential, restricted-access link, signed access value, or inline image bytes; academic text retained.'})
        cursor = end
    pieces.append(text[cursor:])
    return ''.join(pieces), rows


def split_parts(text):
    while text:
        raw = text.encode('utf-8')
        if len(raw) <= MAX_PART_BYTES:
            yield text
            return
        prefix = raw[:MAX_PART_BYTES].decode('utf-8', errors='ignore')
        cut = prefix.rfind('\n')+1
        if not cut:
            cut = len(prefix)
        yield text[:cut]
        text = text[cut:]


def write_csv(path, rows, fields):
    with path.open('w', encoding='utf-8', newline='') as h:
        writer = csv.DictWriter(h, fieldnames=fields, lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def build(archive, originals, private_output):
    assert not OUT.exists(), 'Preserve the existing export supplement; choose a reviewed replacement procedure.'
    legacy = json.loads((BASE/'manifest.json').read_text(encoding='utf-8'))
    selected = {s['id']: s for s in legacy['sources'] if s['platform']=='ChatGPT'}
    found = selected_conversations(archive, set(selected)|{RECOVERY_ID})
    literals = sensitive_literals(originals)
    OUT.mkdir()
    private_output.mkdir(parents=True, exist_ok=True)
    all_messages = []
    redactions = []
    conversations = []
    for cid, (conversation, member, member_hash) in sorted(found.items(), key=lambda x: x[1][0]['create_time']):
        source, messages = render_conversation(conversation)
        (private_output/f'{cid}.txt').write_bytes(source.encode('utf-8'))
        public, changed = redact(source, literals, len(redactions))
        folder = OUT/cid
        folder.mkdir()
        parts = []
        cursor = 0
        for i, part in enumerate(split_parts(public), 1):
            name = f'{cid}/segment-{i:03}.txt'
            data = part.encode('utf-8')
            (OUT/name).write_bytes(data)
            parts.append({'file': name, 'bytes': len(data), 'sha256': sha(data), 'character_start': cursor, 'character_end': cursor+len(part)})
            cursor += len(part)
        def locator(needle):
            for part in parts:
                txt = (OUT/part['file']).read_bytes().decode('utf-8')
                at = txt.find(needle)
                if at >= 0:
                    return part['file']+'#L'+str(txt.count('\n', 0, at)+1)
            raise AssertionError(f'Public locator missing in {cid}')
        for m in messages:
            m['public_locator'] = locator(f'<a id="message-{m["message_id"]}"></a>')
        for row in changed:
            row['conversation_id'] = cid
            row['public_locator'] = locator(row['marker'])
        mapping = conversation['mapping']
        excluded = Counter(n['message']['content']['content_type'] for n in mapping.values()
                           if n.get('message') and n['message']['content']['content_type'] not in VISIBLE_TYPES)
        conversations.append({'conversation_id':cid, 'original_title':conversation.get('title'),
                              'legacy_view_id':selected.get(cid, {}).get('source_id'),
                              'scope':'historical project conversation' if cid in selected else 'direct recovery handoff',
                              'created_utc':utc(conversation.get('create_time')), 'updated_utc':utc(conversation.get('update_time')),
                              'zip_member':member, 'zip_member_sha256':member_hash,
                              'private_readable_sha256':sha(source.encode()), 'public_joined_sha256':sha(public.encode()),
                              'source_characters':len(source), 'public_characters':len(public), 'parts':parts,
                              'visible_messages':len(messages), 'roles':dict(Counter(m['role'] for m in messages)),
                              'non_text_model_record_counts_kept_private':dict(excluded), 'redactions':len(changed)})
        all_messages.extend(messages)
        redactions.extend(changed)
    with (Path(originals)/'DS675_AI_Transcripts_ChatGPT/message_index.csv').open(encoding='utf-8-sig',newline='') as h:
        prior=list(csv.DictReader(h))
    lookup={(m['conversation_id'],m['message_id']):m for m in all_messages}
    recovery=[]
    for old in prior:
        current=lookup[(old['conversation_id'],old['message_id'])]
        pending=old['retrieval_body_status']=='reference_only' and old['browser_body_present']!='True'
        recovery.append({'conversation_id':old['conversation_id'],'message_id':old['message_id'],'role':old['role'],
                         'previous_status':old['retrieval_body_status'],'browser_body_previously_present':old['browser_body_present'],
                         'previously_pending_reference':pending,'export_text_characters':current['native_text_characters'],
                         'export_text_available':current['native_text_characters']>0,'public_locator':current['public_locator']})
    assert len(recovery)==82 and all(x['export_text_available'] for x in recovery)
    archive_hash=hashlib.sha256()
    with Path(archive).open('rb') as h:
        for block in iter(lambda:h.read(8*1024*1024),b''):
            archive_hash.update(block)
    manifest={'captured_utc':datetime.now(timezone.utc).isoformat(),'source_kind':'Student-supplied ChatGPT account data export ZIP',
              'archive_bytes':Path(archive).stat().st_size,'archive_sha256':archive_hash.hexdigest(),
              'publication_scope':'Fixed allowlist: eleven legacy project chats and one direct recovery handoff. Other account conversations remain private.',
              'rendering':'User/assistant text and multimodal_text, ordered by parent depth then creation time and node ID. Native content hashes retain the source identity. Non-text model records and binary assets remain private.',
              'conversations':conversations,'visible_messages':len(all_messages),'roles':dict(Counter(m['role'] for m in all_messages)),
              'legacy_messages_matched':len(recovery),'prior_reference_only_bodies_recovered':sum(x['previous_status']=='reference_only' for x in recovery),
              'pending_reference_bodies_resolved':sum(x['previously_pending_reference'] for x in recovery),
              'prior_truncated_messages_recovered':sum(x['previous_status']=='truncated' for x in recovery),
              'redactions':len(redactions),'redaction_categories':dict(Counter(x['category'] for x in redactions)),
              'legacy_evidence_preserved':True,'historical_completeness_certified':False,
              'limits':'The export establishes available selected message bodies and recorded structure, not server authenticity, worldwide historical completeness, or the truth of every archived AI statement.'}
    write_csv(OUT/'message_index.csv',all_messages,list(all_messages[0]))
    write_csv(OUT/'recovery_map.csv',recovery,list(recovery[0]))
    write_csv(OUT/'redactions.csv',redactions,['conversation_id','redaction_id','source_character_start','source_character_end','category','marker','reason','public_locator'])
    preserved = ['manifest.json','record_index.csv','conversation_index.csv','redactions.csv','contribution_links.csv','repository_construction_request.json','verification.json']
    legacy_paths = [BASE/n for n in preserved] + [BASE/p['file'] for s in legacy['sources'] for p in s['parts']]
    manifest['legacy_preservation_sha256'] = {p.relative_to(ROOT).as_posix(): sha(p.read_bytes()) for p in legacy_paths}
    manifest['derivation_code_sha256'] = {n: sha((ROOT/n).read_bytes()) for n in ['scripts/import_chatgpt_export.py','scripts/validate_chatgpt_export.py']}
    manifest['support_files_sha256'] = {n: sha((OUT/n).read_bytes()) for n in ['message_index.csv','recovery_map.csv','redactions.csv']}
    (OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({k:v for k,v in manifest.items() if k!='conversations'},indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive',type=Path,required=True)
    parser.add_argument('--originals',type=Path,required=True)
    parser.add_argument('--private-output',type=Path,required=True)
    args=parser.parse_args()
    assert not args.archive.resolve().is_relative_to(ROOT.resolve())
    assert not args.private_output.resolve().is_relative_to(ROOT.resolve())
    build(args.archive,args.originals,args.private_output)
