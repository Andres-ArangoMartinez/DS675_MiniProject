# Reproduce the descriptive evidence supporting Milestone 2

## Environment and source files

Use Python 3.12 or newer, create/activate a virtual environment, then install `requirements.txt`. The verified core environment is in [the run manifest](../results/run_manifest.json); [requirements-lock.txt](../requirements-lock.txt) records the full installed package set. Use that lock file instead of `requirements.txt` to install the exact recorded dependencies on a compatible platform. Commands below run from the repository root.

```bash
python -m venv .venv
```

PowerShell activation: `.\.venv\Scripts\Activate.ps1`. On Linux/macOS: `source .venv/bin/activate`. Alternatively invoke the environment's Python executable directly.

```bash
python -m pip install -r requirements.txt
python scripts/validate_repository_hygiene.py
python reproduce.py --download
python scripts/run_tests.py
python scripts/execute_notebook.py
python scripts/validate_ai_interactions.py
python scripts/validate_repository.py
```

The first run downloads about 172 MB from the fixed [Zenodo release](https://doi.org/10.5281/zenodo.4017659). The official files are publicly downloadable. The eleven filenames, published MD5s and original URLs are in [source_manifest.json](../data/source_manifest.json). All inputs are checked against the fixed official release before use. Raw data stay in ignored `data/raw/`. To use an existing flat folder of these exact files:

```bash
python reproduce.py --import-data /path/to/source/files
```

The same official checksums apply to imported files. The default workflow downloads and processes its inputs within this repository. For a separate output folder, use `--output-dir results/check`; default outputs go to `results/`.

## Source-byte integrity and Git tracking

The [hygiene validator](../scripts/validate_repository_hygiene.py) checks tracking, ignore rules and byte-preserving attributes before data acquisition. Git versions the official manifest and reproducible evidence; downloaded source files remain local in `data/raw/`. Python caches, full derived tables and duplicate notebook/check output folders are also local. The four primary figures, executed notebook, compact result tables, source inventories and submitted artifacts remain versioned.

The `.gitattributes` rules preserve exact bytes for fingerprinted CSV, JSON, notebook and transcript files. Editable code/prose uses LF normalization. The [repair record](reproducibility_repair.md) explains the observed Git line-ending conversion, including the earlier failing workflow and the original hashes retained for the evidence.

Existing input files are checked before processing. A valid cache is reused unchanged. If a checksum differs, the command reports the expected and observed values and preserves the existing file; move that file to a backup location, then run `python reproduce.py --download` to acquire the official release. Downloads are verified in temporary files before promotion to the source cache.

## What runs

1. Verify official source checksums and all eight table shapes, dates, unique timestamps, spacing and missing values.
2. Select January–September 2018 and six signals; pair current values with n1 three samples later.
3. Calculate descriptive persistence MAE/RMSE, range and Pearson correlations.
4. Parse the nominal network, identify boundary-connected pipe components and calculate shortest pipe paths.
5. Join the 47-source inventory with 35 groups; validate membership, category and selected-study counts.
6. Generate four figures and compare results against the independently retained [report values](../evidence/reported_values.json).

The pipeline writes statistics, table and topology checks, correlations, small readable samples, figures and an input/code/output hash manifest. Full derived pair tables are generated locally but ignored by Git. The [notebook](../notebooks/milestone2_analysis.ipynb) gives a readable step-by-step execution of the same functions. The test runner records its actual exit code and test count. Tests independently check time alignment, mismatched timestamps, inventory membership, nominal boundaries and report values.

**Executed work:** descriptive EDA, source/table checks, nominal topology, inventory recounts and figures. The 2019 files support structural checks. **Planned work:** model training/selection and final chronological forecast assessment. The learning matrix will add 55-minute histories, with eligible rows determined by history and target availability. Execution dates and attribution identify each recorded reproduction.

## Evidence and interpretation

- [Submitted-artifact hashes](../evidence/submitted_artifacts.json) verify unchanged report and figure bytes.
- [Report claim checklist](../evidence/report_claims.csv) maps submitted sections to sources, code, outputs and status.
- [Literature source checks](../evidence/literature_checks.json) retain paper locators and inspected pinned author-code paths; [recorded code-link checks](../evidence/code_link_checks.json) verify retrieved bytes.
- [Official release check](../evidence/data_release_check.json) compares all eleven manifest entries with live Zenodo metadata and verifies a content-download endpoint.
- [External-link checks](../evidence/external_links.json) record actual automated access outcomes. The records identify successful retrievals and publisher/institutional access conditions. Official DOI links are retained.
- [Repository validation](../results/repository_validation.json) checks links, catalog relationships, notes, report hashes, licenses and scope.
- [Public interaction appendix](../evidence/ai_interactions/README.md) exposes available recovered dialogue and its documented redactions. Its [validator](../scripts/validate_ai_interactions.py) checks public hashes and locators; optional private-source comparison checks every changed and unchanged text interval. The coverage section identifies available replies and the remaining recovery work.

Figures use the established navy/teal/gold palette and serif type. The regenerated images present the same quantities and layout with portable fonts; [submitted images](../evidence/submitted_figures/) retain the original rendering. Numeric comparison uses tolerances; generated image and compressed-table hashes can differ between systems. Together these checks establish traceable calculations and artifacts. The literature notes describe review coverage, and C3 defines the planned test of auxiliary-signal utility.
