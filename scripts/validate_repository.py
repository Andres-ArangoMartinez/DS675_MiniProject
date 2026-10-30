"""Audit internal links, report identity, complete literature and descriptive scope."""
import csv
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.screening import recount
from src.data import digest


def validate():
    broken = []
    checked_links = 0
    markdown = list(ROOT.glob('*.md'))
    for folder in ['docs', 'literature']:
        markdown += list((ROOT / folder).rglob('*.md'))
    interaction_markdown = list((ROOT / 'evidence/ai_interactions').rglob('*.md'))
    # Historical text parts are evidence, not current author claims or new report references.
    link_markdown = markdown + interaction_markdown
    for file in link_markdown:
        for link in re.findall(r'\]\(([^\s]+?)\)', file.read_text(encoding='utf-8')):
            if link.startswith(('http:', 'https:', 'mailto:', '#')):
                continue
            target = unquote(link.split('#', 1)[0].strip('<>'))
            checked_links += 1
            resolved = (file.parent / target).resolve()
            generated_by_this_audit = ROOT / 'results/repository_validation.json'
            if resolved != generated_by_this_audit and not resolved.exists():
                broken.append([file.relative_to(ROOT).as_posix(), target])
    assert not broken, broken
    submitted = json.loads((ROOT / 'evidence/submitted_artifacts.json').read_text())
    for item in submitted:
        assert digest(ROOT / item['file']) == item['sha256'], item['file']
    assert len(submitted) == 6
    result = recount()
    assert (result['source_records'], result['groups'], result['selected_groups']) == (47, 35, 6)
    assert [v['groups'] for v in result['categories']] == [27, 3, 2, 2, 1]
    with (ROOT / 'literature/groups.csv').open(encoding='utf-8-sig') as h:
        groups = list(csv.DictReader(h))
    notes = (ROOT / 'literature/screening_notes.md').read_text(encoding='utf-8')
    note_ids = re.findall(r'<!-- group: ([^ ]+) -->', notes)
    assert len(note_ids) == 35 and set(note_ids) == {g['group'] for g in groups}
    expected_reviews = {'chebnet.md', 'sam_knn.md', 'agn.md', 'lila.md', 'gatres.md', 'eilf.md'}
    assert {p.name for p in (ROOT / 'literature/detailed_review').glob('*.md')} == expected_reviews
    with (ROOT / 'literature/papers_catalog.csv').open(encoding='utf-8-sig') as h:
        catalog = list(csv.DictReader(h))
    pdfs = []
    for row in catalog:
        if row['public_pdf']:
            path = ROOT / 'literature' / row['public_pdf']
            assert path.exists(), row['document']
            assert digest(path) == row['sha256'], row['document']
            assert row['license'] in {'CC-BY-4.0', 'CC-BY-NC-ND-4.0'}, row['document']
            assert row['license_evidence'], row['document']
            for evidence in re.findall(r'license_evidence/[^; ]+\.json', row['license_evidence']):
                assert (ROOT / 'literature' / evidence).exists(), evidence
            pdfs.append(path)
    assert set(pdfs) == set((ROOT / 'literature/papers').glob('*.pdf'))
    for name in ['eda_statistics', 'verification', 'screening_summary', 'table_checks', 'topology_audit', 'run_manifest']:
        assert (ROOT / f'results/{name}.json').exists(), name
    stats = json.loads((ROOT / 'results/eda_statistics.json').read_text())
    assert stats['rows'] == 78624 and stats['forecast_pairs'] == 78621
    assert stats['learned_models_fitted'] is False
    for number, label in [(1,'supply_boundary'), (2,'daily_profiles'), (3,'correlations'), (4,'historical_screening')]:
        for suffix in ['png','svg']:
            assert (ROOT / f'results/figures/figure{number}_{label}.{suffix}').is_file()
    # Inspect owned explanatory/code text, not unmodified third-party PDFs or image encodings.
    owned = markdown + list((ROOT / 'src').glob('*.py')) + list((ROOT / 'tests').glob('*.py')) + [ROOT / 'reproduce.py']
    forbidden = re.compile(r'\b' + 'E' + r'[0-4]\b|ds675\.automationfreelancer\.com|MILESTONE3|MILESTONE_3', re.I)
    for file in owned:
        assert not forbidden.search(file.read_text(encoding='utf-8')), file
    assert not any('sklearn' in p.read_text(encoding='utf-8') for p in (ROOT / 'src').glob('*.py'))
    manifest = json.loads((ROOT / 'results/run_manifest.json').read_text())
    for file, sha in manifest['code_sha256'].items():
        assert digest(ROOT / file) == sha, f'Execution is stale for {file}'
    for file, sha in manifest['classification_and_protocol_sha256'].items():
        assert digest(ROOT / file) == sha, f'Execution is stale for {file}'
    for file, sha in manifest['output_sha256'].items():
        path = ROOT / 'results' / file
        if file.endswith('_full.csv.gz') and not path.exists():
            continue  # Locally generated tables are intentionally not distributed in Git.
        assert path.exists() and digest(path) == sha, file
    execution = json.loads((ROOT / 'results/notebook_execution.json').read_text())
    notebook = ROOT / execution['notebook']
    assert digest(notebook) == execution['sha256'], 'Notebook execution record is stale'
    nb = json.loads(notebook.read_text(encoding='utf-8'))
    cells = [c for c in nb['cells'] if c['cell_type'] == 'code']
    assert len(cells) == execution['code_cells'] == 7
    assert all(c['execution_count'] is not None for c in cells)
    assert not any(o.get('output_type') == 'error' for c in cells for o in c.get('outputs', []))
    test_result = json.loads((ROOT / 'results/test_execution.json').read_text())
    assert test_result['status'] == 'PASS' and test_result['tests_run'] == 7
    code_checks = json.loads((ROOT / 'evidence/code_link_checks.json').read_text())['checks']
    assert len(code_checks) == 9 and all(c.get('matches_recorded_sha256') for c in code_checks)
    # Public scope: do not package recovered interactions or private local paths.
    approved_roots = ['docs', 'evidence', 'literature', 'notebooks', 'reports', 'results', 'scripts', 'src', 'data', '.github']
    public_files = [p for name in approved_roots for p in (ROOT / name).rglob('*') if p.is_file()
                    and not any(part in {'raw', '__pycache__', 'notebook', 'check'} for part in p.relative_to(ROOT).parts)]
    blocked_parts = {'original_sessions', 'database_exports', 'AI Assitance', 'private_exports'}
    for path in public_files:
        relative = path.relative_to(ROOT)
        assert not blocked_parts.intersection(relative.parts), relative
        assert path.suffix.lower() not in {'.jsonl', '.sqlite', '.db', '.zst', '.bundle'}, relative
    explanatory = [ROOT / 'README.md', ROOT / 'docs/student_contributions.md', ROOT / 'docs/professor_feedback.md']
    for path in explanatory:
        text = path.read_text(encoding='utf-8')
        assert not re.search(r'[CD]:[\\/]Users[\\/]|private_exports[\\/]', text), path
    with (ROOT / 'evidence/contribution_summary.csv').open(encoding='utf-8-sig') as handle:
        attribution = list(csv.DictReader(handle))
    assert len(attribution) == 10 and len({x['activity_id'] for x in attribution}) == 10
    assert all(x['student_role'] and x['AI_role'] and x['evidence_basis'] for x in attribution)
    work = json.loads((ROOT / 'evidence/work_status.json').read_text())
    assert len(work['proposed_only']) == 3
    from scripts.validate_ai_interactions import validate as validate_interactions
    interactions = validate_interactions()
    record = {'status':'PASS', 'internal_links_checked':checked_links, 'broken_internal_links':[],
              'submitted_artifact_hashes_match':True, 'source_records':47, 'groups':35, 'screening_notes':35,
              'detailed_studies':6, 'category_counts':[27,3,2,2,1], 'public_pdf_count':len(pdfs),
              'paper_hashes_match':True, 'license_evidence_present':True,
              'execution_code_and_input_hashes_current':True, 'four_generated_figures_present':True,
              'notebook_executed_without_errors':True, 'tests_passed':7, 'pinned_code_hashes_match':9,
              'public_contribution_summary_activities':10, 'private_session_exports_absent':True,
              'public_recovered_source_views':interactions['source_views'],
              'public_transcript_parts':interactions['public_parts'],
              'documented_transcript_redactions':interactions['documented_redactions'],
              'contribution_to_message_links':interactions['contribution_links'],
              'scope':'Executed descriptive evidence; next stage is the proposed modeling study.'}
    (ROOT / 'results/repository_validation.json').write_text(json.dumps(record, indent=2)+'\n', encoding='utf-8', newline='\n')
    print(json.dumps(record, indent=2))
    return record


if __name__ == '__main__':
    validate()
