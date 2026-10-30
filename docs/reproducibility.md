# Reproduce the descriptive evidence supporting Milestone 2

## Environment and source files

Use Python 3.12 or newer. The [run manifest](../results/run_manifest.json) records the core environment; [requirements-lock.txt](../requirements-lock.txt) lists the installed packages for a compatible platform. Run commands from the repository root.

```bash
python -m venv .venv
```

Activate with `.\.venv\Scripts\Activate.ps1` in PowerShell or `source .venv/bin/activate` on Linux/macOS; alternatively invoke the environment's Python directly.

```bash
python -m pip install -r requirements.txt
python scripts/validate_repository_hygiene.py
python reproduce.py --download
python scripts/run_tests.py
python scripts/execute_notebook.py
python scripts/validate_ai_interactions.py
python scripts/validate_repository.py
```

The first run downloads about **172 MB** from the fixed [Zenodo release](https://doi.org/10.5281/zenodo.4017659). The [source manifest](../data/source_manifest.json) records eleven filenames, official MD5s and URLs. Inputs are verified before processing and stored in ignored `data/raw/`. An existing flat cache can be imported with the same checks:

```bash
python reproduce.py --import-data /path/to/source/files
```

Outputs default to `results/`; `--output-dir results/check` selects a separate folder. Use `requirements-lock.txt` instead of `requirements.txt` to install the recorded dependency set.

## Source-byte integrity and Git tracking

The [hygiene validator](../scripts/validate_repository_hygiene.py) checks tracking, ignore rules and protected attributes. Git versions code, manifests, compact results, four primary figures, the executed notebook, inventories and retained report artifacts. Raw downloads, Python caches, full derived tables and duplicate notebook/check outputs remain local.

Attributes preserve fingerprinted CSV, JSON, notebook and transcript bytes; editable code/prose uses LF normalization. The [repair record](reproducibility_repair.md) documents the earlier conversion failure and corrected checkout.

Valid cached files are reused unchanged. A checksum mismatch reports expected/observed values and preserves the existing file. Move it to a backup location before rerunning `python reproduce.py --download`. Temporary downloads are verified before promotion.

## What runs

1. Check official hashes and all eight tables' shapes, dates, unique timestamps, spacing and missing values.
2. Select six signals for January–September 2018; pair current values with n1 three samples later.
3. Calculate persistence MAE/RMSE, pressure range and Pearson correlations.
4. Parse nominal boundaries/components and shortest pipe paths.
5. Join 47 source records with 35 groups; check categories and detailed selections.
6. Generate four figures and compare quantities with retained [report values](../evidence/reported_values.json).

The pipeline writes statistics, table/topology checks, correlations, samples, figures, local full tables and input/code/output fingerprints. The [notebook](../notebooks/milestone2_analysis.ipynb) executes the same functions. Seven tests check official integrity, timestamp alignment, missing/duplicate times, inventory membership, nominal boundaries/distances and report values; the runner records its exit code and count.

**Completed:** descriptive exploratory analysis, source/table checks, nominal topology, inventory recounts and figures. **Proposed:** C1–C3 learning experiments and the planned final chronological assessment. The 2019 files support structural checks; proposed forecast rows will require complete 55-minute histories and in-period targets.

## Evidence and interpretation

- [Artifact fingerprints](../evidence/submitted_artifacts.json) identify the retained report/figure copies. Hash agreement checks these copies against repository records; it does not authenticate an external course-platform submission.
- [Claim map](../evidence/report_claims.csv) links report sections to sources, code, outputs and status.
- [Literature inspections](../evidence/literature_checks.json) and [code-link checks](../evidence/code_link_checks.json) record paper locators and pinned code fingerprints.
- [Release check](../evidence/data_release_check.json) compares eleven manifest entries with retrieved Zenodo metadata and tests a content endpoint.
- [External-link checks](../evidence/external_links.json) record retrieval results and publisher/institutional access conditions; official DOIs remain linked.
- [Repository validation](../results/repository_validation.json) checks links, catalog relationships, notes, retained hashes and scope.
- [Conversation evidence](../evidence/ai_interactions/README.md) states recovery limits and redactions. Its [validator](../scripts/validate_ai_interactions.py) checks public hashes/locators; optional private-source comparison reconstructs registered changes and retained intervals.

Figures retain the navy/teal/gold palette, serif type, quantities and layout, using portable fonts. [Report images](../evidence/submitted_figures/) preserve the retained rendering. Numerical comparisons use stored tolerances; regenerated image and compressed-table hashes may vary across systems.
