"""Execute the explanatory notebook with this environment's Python kernel."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import nbformat
from nbclient import NotebookClient
from jupyter_client.kernelspec import KernelSpecManager

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / 'notebooks/milestone2_analysis.ipynb'
nb = nbformat.read(path, as_version=4)
with tempfile.TemporaryDirectory(prefix='ds675_kernel_') as folder:
    kernel = Path(folder) / 'kernel'
    kernel.mkdir()
    (kernel / 'kernel.json').write_text(json.dumps({'argv':[sys.executable, '-m', 'ipykernel_launcher', '-f', '{connection_file}'], 'display_name':'Python 3', 'language':'python'}), encoding='utf-8')
    manager = KernelSpecManager(kernel_dirs=[folder])
    # The directory name is the kernel spec's identifier, independently of user-global kernels.
    client = NotebookClient(nb, timeout=240, kernel_name='kernel', resources={'metadata':{'path':str(ROOT)}})
    client.km = client.create_kernel_manager()
    client.km.kernel_spec_manager = manager
    client.execute()
with path.open('w', encoding='utf-8', newline='\n') as output:
    nbformat.write(nb, output)
errors = [out for cell in nb.cells if cell.cell_type=='code' for out in cell.get('outputs', []) if out.output_type=='error']
assert not errors
record = {'executed_utc':datetime.now(timezone.utc).isoformat(), 'notebook':'notebooks/milestone2_analysis.ipynb',
          'code_cells':sum(c.cell_type=='code' for c in nb.cells), 'error_outputs':len(errors),
          'sha256':hashlib.sha256(path.read_bytes()).hexdigest(), 'learned_models_fitted':False}
(ROOT / 'results/notebook_execution.json').write_text(json.dumps(record, indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(record,indent=2))
