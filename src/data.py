"""Acquire the fixed Zenodo release and validate its published checksums."""
from pathlib import Path
import hashlib
import json
import shutil
import time
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def digest(path, algorithm='sha256'):
    h = hashlib.new(algorithm)
    with Path(path).open('rb') as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def source_manifest():
    return json.loads((ROOT / 'data/source_manifest.json').read_text(encoding='utf-8'))


def ensure_data(folder, download=False, import_folder=None):
    """Do not silently substitute a different mirror or dataset release."""
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    manifest = source_manifest()
    records = []
    for source in manifest['files']:
        path = folder / source['filename']
        method = 'existing_local_file_checked_against_official_md5'
        if not path.exists() and import_folder is not None:
            candidate = Path(import_folder) / source['filename']
            if candidate.exists():
                shutil.copyfile(candidate, path)
                method = 'imported_local_cache_checked_against_official_md5'
        if not path.exists():
            if not download:
                raise FileNotFoundError(
                    f'{source["filename"]} is missing. Run python reproduce.py --download '
                    'or specify --import-data /path/to/flat/cache.'
                )
            print(f'Downloading {source["filename"]} from Zenodo ...', flush=True)
            temporary = path.with_name(path.name + '.part')
            for attempt in range(3):
                try:
                    request = urllib.request.Request(
                        source['download_url'], headers={'User-Agent': 'DS675-reproducibility/1.0'}
                    )
                    with urllib.request.urlopen(request, timeout=45) as response, temporary.open('wb') as output:
                        shutil.copyfileobj(response, output)
                    if digest(temporary, 'md5') != source['md5']:
                        raise ValueError(f'Official checksum mismatch: {source["filename"]}')
                    temporary.replace(path)
                    break
                except Exception:
                    if temporary.exists():
                        temporary.unlink()
                    if attempt == 2:
                        raise
                    time.sleep(1)
            method = 'downloaded_from_official_zenodo_url'
        actual = digest(path, 'md5')
        if actual != source['md5']:
            raise ValueError(
                f'Checksum mismatch for {source["filename"]}: expected {source["md5"]}, '
                f'observed {actual}. The existing file is preserved. Move it to a backup '
                'location, then use --download to acquire the official bytes.'
            )
        records.append({
            'filename': path.name, 'acquisition': method, 'bytes': path.stat().st_size,
            'md5': actual, 'official_md5_matches': True, 'sha256': digest(path),
            'source_url': source['download_url'], 'license': 'CC-BY-4.0',
        })
        print(f'Verified {path.name}', flush=True)
    return records
