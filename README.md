# Milestone 2 — research contributions and supporting evidence

**Learning Models for Pressure Forecasting · Andres Arango Martinez · DS675, NJIT**

Andres Arango Martinez developed this project around a question from his control-engineering practice: **how can local SCADA measurements help forecast pressure at a monitored water-network node?** He selected BattLeDIM/L-Town, proposed the Area C sensor cohort, chose n1 as the target, narrowed the local measurements and directed the literature review and visual analyses. The [recorded contributions](docs/student_contributions.md) trace these decisions and the associated AI assistance.

This repository complements the [submitted Milestone 2 report](reports/Milestone2.pdf) with reproducible calculations, a literature inventory and source-linked contribution evidence. The task is **recorded n1 pressure at +15 minutes**, using six five-minute signals: **n1, n4, n31, T1, PUMP_1 and AMR_n1**. The simulated SCADA measurements come from the [official Zenodo release](https://doi.org/10.5281/zenodo.4017659). [Milestone 1](reports/Milestone1.pdf) records the earlier engineering motivation and pressure-forecasting proposal.

## Student-led research and evidence

| Contribution or research question | Supporting material |
|---|---|
| Engineering direction, choices and critical review | [Student contributions and AI collaboration](docs/student_contributions.md), with [source-level conversation evidence](evidence/ai_interactions/README.md) |
| Hydraulic scope and selection of six local signals | [Dataset, target and Area C rationale](docs/research_scope.md) |
| Daily profiles, correlations and persistence reference | [Executed notebook](notebooks/milestone2_analysis.ipynb), [EDA explanation](docs/exploratory_analysis.md), [code](src/) and [run manifest](results/run_manifest.json) |
| Classification of previous work by objective | [47 source records](literature/source_records.csv), [35 assignments](literature/groups.csv), [screening notes](literature/screening_notes.md) and [recount](results/screening_summary.json) |
| Understanding six relevant previous approaches | [Detailed reviews and source/code links](literature/README.md) |
| Relationship to Ahmed et al. | [Feedback-related comparison](literature/ahmed_feedback.md) |
| Planned predictive-learning contribution | [C1–C3 and evaluation criteria](docs/anticipated_contributions.md) |

[Response to the professor's feedback](docs/professor_feedback.md) · [Report claim-to-evidence map](evidence/report_claims.csv)

## Completed analysis and next research stage

The completed descriptive analysis covers **273 days, 78,624 timestamps and 78,621 valid +15-minute pairs** from January–September 2018. n1 ranges from **25.67 to 29.36 m**. The persistence reference has **MAE 0.0518 m** and **RMSE 0.0685 m**. Four figures document the supply boundary, daily profiles, correlations and literature classification. AI-assisted code implements and executes these calculations under the student's research direction.

The focused literature inventory contains **47 records → 35 related-work groups → six detailed selections**. Related papers and repositories can share a group. Published author scores appear with their original evaluation tasks and sources; Ahmed et al. is a separate feedback supplement.

The next stage is the submitted modeling plan: **C1**, prepare aligned forecast data; **C2**, compare Gradient Boosting with persistence, Ridge and Random Forest; **C3**, assess the joint value of the auxiliary signals against n1 history using the same calendar variables and evaluation rows. These are **proposed learning experiments**. [Work-status summary](evidence/work_status.json).

## Reproduce

Use Python 3.12 or newer; the recorded execution used Python 3.14.

```bash
python -m venv .venv
# Activate .venv using your shell's command.
python -m pip install -r requirements.txt
python scripts/validate_repository_hygiene.py
python reproduce.py --download
python scripts/run_tests.py
python scripts/execute_notebook.py
python scripts/validate_ai_interactions.py
python scripts/validate_repository.py
```

The public download verifies official checksums and stores inputs in ignored `data/raw/`. [Reproduction instructions](docs/reproducibility.md) describe the calculations and their interpretation; [redistribution terms](NOTICE.md) cover the data sources and 32 permitted original PDFs.

Git versions the source manifest, code and supporting evidence. Official downloads, Python caches and duplicate full notebook outputs stay local. Byte-preservation attributes protect fingerprinted transcripts, JSON, CSV and notebook files. [Source-integrity repair](docs/reproducibility_repair.md) documents the verified line-ending issue and the checks that protect future checkouts.

The [AI interaction appendix](evidence/ai_interactions/README.md) provides available recovered conversations, documented privacy redactions and direct links to the student's decisions and AI assistance. Its coverage section identifies the partial ChatGPT recovery and the recorded Codex snapshot dates. Untouched originals support private source comparison. See [interaction coverage](docs/student_contributions.md#interaction-records-and-limits).
