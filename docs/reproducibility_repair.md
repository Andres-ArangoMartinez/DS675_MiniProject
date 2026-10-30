# Source integrity and reproducible checkout

Commit [`ac6ba439f0739e1562c310fbe50bcc8c2fb1e445`](https://github.com/Andres-ArangoMartinez/DS675_MiniProject/commit/ac6ba439f0739e1562c310fbe50bcc8c2fb1e445) corrected source acquisition while preserving n1(+15), six signals and proposed C1–C3 experiments. [Workflow run 41067513928](https://github.com/Andres-ArangoMartinez/DS675_MiniProject/actions/runs/41067513928) completed successfully for that commit.

## Verified cause

At `4690d5020d73782faa2ff514003cf082cb52f380`, Git tracked eleven raw inputs under `* text=auto`, and `.gitignore` was absent. Git stored LF-normalized files; the local Windows cache retained official CRLF bytes matching all eleven published MD5s. [The failed workflow](https://github.com/Andres-ArangoMartinez/DS675_MiniProject/actions/runs/41061626951) stopped on the pressure-file checksum.

`2018_SCADA_Pressures.csv` had **22,593,812 official/local bytes**, MD5 `d389d8541350c19ff0bfc6b80f246d35`; its Git blob had **22,488,691 bytes**, MD5 `b6f76d9a2907df3be17bf86523ac7e3a`, matching the failure log. Each of eight CSVs lost **105,121 CR bytes**. INP, YAML and README were also normalized. An in-memory conversion diagnostic reproduced the eleven official hashes; analysis used official bytes, and valid local files were preserved.

The inspection also found **103 transcript parts** with normalized Git blobs. The repair restored their manifest-matching local bytes. [Diagnostic record](../results/source_integrity_audit.json).

## Corrections

- Keep verified official downloads/imports in local `data/raw/`; remove Git tracking while retaining the cache.
- Ignore bytecode, full derived tables and duplicate notebook/check outputs. Retain reports, literature, transcripts, primary figures and notebook.
- Preserve fingerprinted CSV, JSON, notebook and transcript bytes through `.gitattributes`; see [Git documentation](https://git-scm.com/docs/gitattributes#_text).
- Check tracking, ignore rules, attributes and the supplied request's staged fingerprint before acquisition and during repository validation.
- Retain mismatched cached files with an explicit error; verify official downloads and test byte sizes as well as hashes.

## Execution evidence

An isolated candidate checkout started with empty `data/raw/` and downloaded all eleven official files. It and the working copy completed:

```bash
python scripts/validate_repository_hygiene.py
python reproduce.py --download
python scripts/run_tests.py
python scripts/execute_notebook.py
python scripts/validate_ai_interactions.py
python scripts/validate_repository.py
```

The [isolated record](../results/clean_checkout_validation.json) identifies inputs, tested source hashes, quantities and exit codes. The **226 protected files** matched retained pre-repair fingerprints in both copies; four regenerated PNG fingerprints also matched. These checks establish retained-copy integrity against repository records.

[Hygiene](../results/repository_hygiene.json) · [Numerical verification](../results/verification.json) · [Tests](../results/test_execution.json) · [Notebook](../results/notebook_execution.json) · [Repository validation](../results/repository_validation.json) · [Workflow history](https://github.com/Andres-ArangoMartinez/DS675_MiniProject/actions/workflows/reproduce.yml)

The [feedback response](professor_feedback.md), [attribution guide](student_contributions.md), [literature reviews](../literature/README.md) and [proposal](anticipated_contributions.md) distinguish reproduced descriptive quantities, published author findings and proposed experiments.
