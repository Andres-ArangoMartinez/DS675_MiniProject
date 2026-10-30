# Milestone 2 — research contributions and supporting evidence

**Learning Models for Pressure Forecasting · Andres Arango Martinez · DS675, NJIT**

This repository is a **feedback-response supplement** to the [original submitted Milestone 2 report](reports/Milestone2.pdf). It provides reproducible descriptive calculations, a literature inventory and source-linked student/AI attribution. [Milestone 1](reports/Milestone1.pdf) records the earlier pressure-forecasting proposal.

The proposed supervised-regression task is **recorded n1 pressure at +15 minutes**, using six five-minute signals: **n1, n4, n31, T1, PUMP_1 and AMR_n1** from the simulated [BattLeDIM/L-Town release](https://doi.org/10.5281/zenodo.4017659). The [recorded exchanges](docs/student_contributions.md) document the student's control/modeling interests, dataset choice, local sensor proposal, final n1 selection, AMR restriction and technical revisions. They also identify AI methodological recommendations, code generation, execution, source inspection and drafting.

## Contents

| Topic | Supporting material |
|---|---|
| Feedback response and attribution | [Professor's concerns](docs/professor_feedback.md), [student/AI roles](docs/student_contributions.md), [conversation evidence](evidence/ai_interactions/README.md) |
| Dataset, target and hydraulic scope | [Area C and selected signals](docs/research_scope.md) |
| Descriptive exploratory analysis | [Explanation and four figures](docs/exploratory_analysis.md), [executed notebook](notebooks/milestone2_analysis.ipynb), [code](src/), [run manifest](results/run_manifest.json) |
| Literature | [47 source records](literature/source_records.csv), [35 group assignments](literature/groups.csv), [screening notes](literature/screening_notes.md), [recount](results/screening_summary.json), [six detailed comparisons](literature/README.md) |
| Feedback-related source | [Ahmed et al. comparison](literature/ahmed_feedback.md) |
| Proposed experiments | [C1–C3 and evaluation criteria](docs/anticipated_contributions.md) |
| Report claims | [Claim-to-evidence map](evidence/report_claims.csv) |

## Completed analysis and proposed experiments

The January–September 2018 descriptive exploratory analysis covers **273 days, 78,624 timestamps and 78,621 valid +15-minute pairs**. n1 ranges from **25.67 to 29.36 m**. The persistence reference gives **MAE 0.0518 m** and **RMSE 0.0685 m**. Four figures show the supply boundary, daily profiles, correlations and literature groups.

The historical inventory contains **47 source records assigned to 35 related-work groups**, including six studies selected for detailed comparison. Related papers and code may share a group. Published scores retain their authors' evaluation context; Ahmed et al. is a separate feedback supplement.

The **proposed C1–C3 experiments** cover forecast-data preparation, Gradient Boosting versus persistence/Ridge/Random Forest, and the joint value of auxiliary signals versus n1 history with the same calendar variables and rows. [Work status](evidence/work_status.json).

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

Official inputs are checksum-verified in ignored `data/raw/`. [Reproduction instructions](docs/reproducibility.md) describe versioned evidence, local outputs and byte preservation; the [repair record](docs/reproducibility_repair.md) documents the corrected checkout and workflow. The [source notice](NOTICE.md) identifies retained license evidence for 32 public PDFs.

The [interaction appendix](evidence/ai_interactions/README.md) preserves the earlier capture and adds an [account-export supplement](evidence/ai_interactions/chatgpt_export/README.md): twelve selected conversations, 186 readable entries and resolution of all fifteen previously pending reply bodies. A11/A12 document additional prompt-drafting evidence. [Coverage](docs/student_contributions.md#interaction-records-and-limits) distinguishes export and Codex boundaries, private binaries and registered redactions.
