# Milestone 2 feedback response

This feedback-response supplement links the [original submitted Milestone 2 report](../reports/Milestone2.pdf) to data, code, execution records, literature and conversations. Professor Houle requested provenance for the reported analysis, a literature inventory, an Ahmed et al. comparison and a clearer anticipated contribution. He stated that implementation was optional for this milestone.

| Feedback topic | Response and evidence | Scope |
|---|---|---|
| EDA, correlations and persistence | [Roles](student_contributions.md), [executed notebook](../notebooks/milestone2_analysis.ipynb), [calculation code](../src/analysis.py), [statistics](../results/eda_statistics.json), [manifest](../results/run_manifest.json) | Student-defined questions; AI-assisted code generation and execution, with dated reproductions. |
| Figures 2–4 | [Plotting code](../src/figures.py), [generated figures](../results/figures/), [claim map](../evidence/report_claims.csv) | Reproduced quantities and plotting procedure; retained report images remain separate. |
| Tables and hydraulic scope | [Source manifest](../data/source_manifest.json), [table checks](../results/table_checks.json), [topology/distances](../results/topology_audit.json) | Table structure, nominal sector membership and pipe-path lengths. Figure 1 is a functional schematic. |
| Literature inventory | [47 records](../literature/source_records.csv), [35 assignments](../literature/groups.csv), [screening notes](../literature/screening_notes.md), [counting code](../src/screening.py) | Focused screening and six detailed comparisons; historical search-query coverage is partial. |
| Ahmed et al. (2025) | [Source comparison](../literature/ahmed_feedback.md) | Five shared Area C signals; reconstruction-based leak detection versus proposed future n1 pressure and AMR_n1. |
| Anticipated contribution | [C1–C3 and evaluation plan](anticipated_contributions.md) | Proposed model comparison and joint auxiliary-signal test on common targets, chronological periods and MAE/RMSE. |
| Attribution | [Student/AI roles](student_contributions.md), [summary](../evidence/contribution_summary.csv), [source-linked guide](../evidence/ai_interactions/README.md) | Recorded decisions, AI recommendations and executions, retrospective accounts and recovery limits. |

The small descriptive persistence error motivates the proposed comparison with established regressors and n1 history. C3 tests the auxiliary signals jointly; it cannot attribute a gain specifically to AMR_n1. The plan retains validation-based settings and a planned final chronological assessment. These materials document the response for the instructor's review.

The [ChatGPT export supplement](../evidence/ai_interactions/chatgpt_export/README.md) supplies the fifteen previously pending replies and five untruncated messages. It also links student requests to five matching AI-drafted instruction files, extending source-level attribution without changing the submitted research scope.
