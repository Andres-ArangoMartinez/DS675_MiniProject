# Contributions and evidence responding to the Milestone 2 feedback

The student directed this supplement toward the professor's questions about provenance, literature coverage and the value of the proposed experiments. It connects the [submitted report](../reports/Milestone2.pdf) to source data, code, execution records and conversations. The original report remains the historical submission; the supplement adds traceable explanations and later reproductions.

| Feedback topic | Student contribution and supporting evidence | What the evidence establishes |
|---|---|---|
| EDA, correlations and persistence | Student-defined analysis questions and visual requirements; [roles](student_contributions.md), [executed notebook](../notebooks/milestone2_analysis.ipynb), [code](../src/analysis.py), [statistics](../results/eda_statistics.json), [manifest](../results/run_manifest.json) | A student-directed, AI-assisted descriptive analysis with traceable inputs, implementation and outputs. |
| Figures 2–4 | Student selection of plots and layout; [plotting code](../src/figures.py), [generated figures](../results/figures/), [claim map](../evidence/report_claims.csv) | Reproducible transformations and plotting procedures, with portable rendering and preserved submitted images. |
| Tables and hydraulic scope | Student's Area C reasoning; [source manifest](../data/source_manifest.json), [table checks](../results/table_checks.json), [nominal topology/distances](../results/topology_audit.json) | Verified table structure, sector membership and nominal pipe-path lengths; Figure 1 explains the functional supply route. |
| The 35-group classification | Student-defined objective/relevance criteria; [47 records](../literature/source_records.csv), [35 assignments](../literature/groups.csv), [notes](../literature/screening_notes.md), [recounting code](../src/screening.py) | Reproducible inventory counts and mappings, with focused screening and six closer technical reviews. |
| Ahmed et al. (2025) | [Comparison](../literature/ahmed_feedback.md) addressing the professor's requested source | Five shared Area C measurements connect the proposal to prior reconstruction-based leak detection; future n1 pressure and local AMR_n1 define the proposed extension. |
| Anticipated contribution | Student's control-engineering question and scoped choices; [C1–C3](anticipated_contributions.md) | A controlled study of forecast methods and the joint value of local auxiliary signals. |
| Fair comparison | [Preparation/evaluation plan](anticipated_contributions.md) | Common forecast targets/rows, chronological development and assessment, validation-based settings, and MAE/RMSE. |
| Student and AI roles | [Contribution statement](student_contributions.md), [summary](../evidence/contribution_summary.csv), [conversation guide](../evidence/ai_interactions/README.md) | Recorded student direction, decisions and critical review alongside AI recommendations, implementation, execution and drafting. |

The central question is whether the full local measurements add forecast value beyond a strong n1-history reference. The small descriptive persistence error gives the proposed comparison a demanding baseline. Reporting all outcomes will support a reasoned choice between a simpler predictor and the full signal set.

C3 measures the auxiliary signals jointly. A separate individual-signal analysis would be needed to attribute an effect specifically to AMR_n1. The Ahmed comparison helps define the learning-task extension and gives the student's feature choices a clear place in the prior work.

The repository supplies computational reproducibility and an organized record of AI collaboration. Its coverage information identifies the available conversations and recovery gaps, giving the instructor a concrete basis for reviewing the supplement.
