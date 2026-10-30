"""Check Git tracking and byte-preservation rules before acquiring official data."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def git_executable():
    executable = shutil.which('git')
    if executable:
        return executable
    local = os.environ.get('LOCALAPPDATA')
    if local:
        candidates = list((Path(local) / 'GitHubDesktop').glob('app-*/resources/app/git/cmd/git.exe'))
        if candidates:
            return str(max(candidates, key=lambda p: p.stat().st_mtime))
    raise RuntimeError('Install Git CLI or GitHub Desktop to validate repository tracking.')


def validate():
    executable = git_executable()

    def git(*args):
        return subprocess.check_output([executable, '-C', str(ROOT), *args])

    assert Path(git('rev-parse', '--show-toplevel').decode().strip()).resolve() == ROOT.resolve()
    tracked = [p for p in git('ls-files', '-z').decode().split('\0') if p]
    unwanted = [p for p in tracked if p.startswith(('data/raw/', 'results/notebook/', 'results/check/', '.venv/', 'venv/'))
                or '__pycache__' in Path(p).parts or Path(p).suffix in {'.pyc', '.pyo'}
                or p in {'results/selected_inputs_full.csv.gz', 'results/forecast_pairs_full.csv.gz'}]
    assert not unwanted, f'Keep reproducible caches local by removing these paths from Git tracking: {unwanted}'
    probes = ['data/raw/2018_SCADA_Pressures.csv', 'src/__pycache__/probe.pyc', '.venv/probe.txt',
              'results/selected_inputs_full.csv.gz', 'results/forecast_pairs_full.csv.gz',
              'results/notebook/figures/probe.png', 'results/check/probe.json', '.ipynb_checkpoints/probe.ipynb']
    for path in probes:
        result = subprocess.run([executable, '-C', str(ROOT), 'check-ignore', '--no-index', '--quiet', '--', path])
        assert result.returncode == 0, f'Add an ignore rule for {path}'
    manifest = json.loads((ROOT / 'evidence/ai_interactions/manifest.json').read_text(encoding='utf-8'))
    part = 'evidence/ai_interactions/' + manifest['sources'][0]['parts'][0]['file']
    protected = ['data/raw/2018_SCADA_Pressures.csv', 'data/source_manifest.json',
                 'literature/source_records.csv', 'notebooks/milestone2_analysis.ipynb',
                 'evidence/ai_interactions/repository_construction_request.json', part]
    values = git('check-attr', '-z', 'text', '--', *protected).decode().split('\0')[:-1]
    attributes = {values[i]: values[i+2] for i in range(0, len(values), 3)}
    assert all(attributes[p] == 'unset' for p in protected), attributes
    attachment = manifest['provided_request_attachment']
    staged = git('show', ':evidence/ai_interactions/' + attachment['file'])
    assert hashlib.sha256(staged).hexdigest() == attachment['sha256'], 'Stage the original request bytes using the protected attributes.'
    record = {'status': 'PASS', 'checked_utc': datetime.now(timezone.utc).isoformat(),
              'tracked_files': len(tracked), 'tracked_raw_files': 0, 'tracked_cache_files': 0,
              'ignore_probes_passed': len(probes), 'byte_preservation_paths_checked': len(protected),
              'staged_request_fingerprint_matches': True,
              'gitignore_sha256': hashlib.sha256((ROOT / '.gitignore').read_bytes()).hexdigest(),
              'gitattributes_sha256': hashlib.sha256((ROOT / '.gitattributes').read_bytes()).hexdigest()}
    (ROOT / 'results').mkdir(exist_ok=True)
    (ROOT / 'results/repository_hygiene.json').write_text(json.dumps(record, indent=2)+'\n', encoding='utf-8', newline='\n')
    print(json.dumps(record, indent=2))
    return record


if __name__ == '__main__':
    validate()
