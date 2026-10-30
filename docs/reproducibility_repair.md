# Source integrity and reproducible checkout

This repair preserves the student's n1(+15) research question, six selected signals, C1–C3 proposal and the original submitted artifacts. It addresses the source-acquisition failure in [workflow run 41061626951](https://github.com/Andres-ArangoMartinez/DS675_MiniProject/actions/runs/41061626951) at commit `4690d5020d73782faa2ff514003cf082cb52f380`.

## Verified cause

The recreated repository tracked the eleven official input files under `data/raw/` with `* text=auto` and had lost its `.gitignore`. Git stored LF-normalized versions while the Windows local cache retained the official CRLF bytes. The local files match all eleven published MD5 hashes.

For `2018_SCADA_Pressures.csv`, the official/local file has **22,593,812 bytes** and MD5 `d389d8541350c19ff0bfc6b80f246d35`. The failed commit stored **22,488,691 bytes** and MD5 `b6f76d9a2907df3be17bf86523ac7e3a`, exactly the value in the failed job log. Each of the eight CSVs lost **105,121 bytes**, corresponding to its CR characters. The INP, YAML and source README were also normalized. An in-memory diagnostic of the conversion reproduced all eleven official hashes; the repair uses official downloaded bytes for analysis and preserves the valid local originals.

The same inspection found **103 public transcript parts** whose Git blobs differed from their valid local originals. Their original manifests and content remain the authority for exact bytes. [Diagnostic source record](../results/source_integrity_audit.json).

## Corrections and protection

- Official inputs are local downloads/imports verified against the fixed Zenodo release. Removing their Git tracking preserves the existing local cache.
- `.gitignore` keeps raw inputs, Python bytecode, full derived CSV tables and duplicate notebook/check figures local. Original reports, submitted figures, literature, public transcripts, primary figures and the executed notebook remain versioned.
- `.gitattributes` preserves fingerprinted CSV, JSON, notebook and transcript bytes. Protected evidence is staged from the local copies that match the recorded fingerprints.
- The hygiene validator checks Git tracking, ignore behavior, protected attributes and the supplied request's staged fingerprint. GitHub Actions runs it before acquisition, and the final repository validator repeats the tracking check.
- Existing-cache failures report expected and observed MD5s while retaining the existing file. The established official-download and checksum checks remain in force. The seven-test suite also checks official byte sizes.

The [Git attribute documentation](https://git-scm.com/docs/gitattributes#_text) describes the text conversion controlled by these rules.

## Verification procedure

The candidate Git index is exported to an isolated checkout with LF behavior and an initially empty `data/raw/`. It uses the documented Python environment and downloads all eleven files directly from the official Zenodo URLs. The following commands are executed in order:

```bash
python scripts/validate_repository_hygiene.py
python reproduce.py --download
python scripts/run_tests.py
python scripts/execute_notebook.py
python scripts/validate_ai_interactions.py
python scripts/validate_repository.py
```

Both the working execution and the isolated fresh-download execution completed all six commands successfully. The [isolated checkout record](../results/clean_checkout_validation.json) contains the actual eleven download fingerprints, command exit codes, tested source hashes and reproduced quantities. The 226 protected original files and the four regenerated PNG fingerprints agree across both copies. Recorded outputs identify each execution, input/code fingerprints, numerical results and notebook status. [Hygiene result](../results/repository_hygiene.json) · [Numerical verification](../results/verification.json) · [Test execution](../results/test_execution.json) · [Notebook execution](../results/notebook_execution.json) · [Repository validation](../results/repository_validation.json).

The repaired workflow targets `main` and follows the same acquisition and validation sequence. Publication and its exact-commit Actions result are recorded after the student's approval of the commit title and description. The [workflow history](https://github.com/Andres-ArangoMartinez/DS675_MiniProject/actions/workflows/reproduce.yml) supplies the public execution record.

## Academic scope

Professor Houle requested traceable EDA, inventory and attribution, together with a clear anticipated contribution. The [feedback response](professor_feedback.md), [student contribution guide](student_contributions.md), [literature reviews](../literature/README.md) and [proposal](anticipated_contributions.md) retain that scope. This verification reproduces descriptive calculations and preserves the original author-reported literature findings. C1–C3 remain the proposed next research stage.
