"""Run the actual tests and retain this execution's outcome."""
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import subprocess
import sys
ROOT = Path(__file__).resolve().parents[1]
command = [sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-v']
result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, encoding='utf-8', errors='replace')
output = result.stdout + result.stderr
match = re.search(r'Ran (\d+) tests?', output)
record = {'executed_utc':datetime.now(timezone.utc).isoformat(), 'command':'python -m unittest discover -s tests -v',
          'status':'PASS' if result.returncode == 0 else 'FAIL', 'exit_code':result.returncode,
          'tests_run':int(match.group(1)) if match else 0, 'output':output}
(ROOT / 'results/test_execution.json').write_text(json.dumps(record, indent=2)+'\n', encoding='utf-8', newline='\n')
print(output)
raise SystemExit(result.returncode)
