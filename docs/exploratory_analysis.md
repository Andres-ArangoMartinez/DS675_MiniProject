# Completed exploratory analysis

This page supports [Milestone 2, Sections 1.1–1.3 and Figures 1–4](../reports/Milestone2.pdf). The student defined the local measurements, visual questions and panel arrangement. AI-assisted code implements and executes the descriptive calculations. The [contribution statement](student_contributions.md) and source-linked guide document this collaboration.

## Source and calculations

The pipeline verifies the eleven files in the [official-source manifest](../data/source_manifest.json): eight annual SCADA tables, the nominal model, sensor configuration and README. It checks the 2018 and 2019 table structure and computes the descriptive pressure-pair errors and correlations for **January–September 2018**. The later 2019 model evaluation is a planned final chronological assessment.

[Data loading and calculations](../src/analysis.py) use the six selected signals directly in their recorded units. The period is cropped before `n1.shift(-3)` creates the future label. Eligible pairs retain their future label within September, leaving the last three origins outside the paired table. This produces 78,621 pairs from 78,624 timestamps. These pairs support descriptive correlations and persistence. The planned learning matrix will add 55-minute histories and apply the corresponding history-availability checks.

For error `e = n1(u + 15) − n1(u)`, MAE is the mean of `abs(e)` and RMSE is the square root of the mean of `e²`. Pearson correlations use the same aligned pairs. Each row keeps its current predictors separate from the future target.

| Quantity | Reproduced value |
|---|---:|
| Days / timestamps | 273 / 78,624 |
| Valid +15-minute pairs | 78,621 |
| n1 minimum / maximum | 25.67 / 29.36 m |
| Persistence MAE | 0.05177624298851451 m |
| Persistence RMSE | 0.06849175638676988 m |
| Current n1 / future n1 correlation | 0.9923104288422752 |
| T1 / future n1 correlation | 0.9230382756150443 |
| PUMP_1 / future n1 correlation | −0.036721113537145696 |
| AMR_n1 / future n1 correlation | −0.1573783306135834 |

[Statistics](../results/eda_statistics.json) · [complete correlation table](../results/correlations.csv) · [numerical verification](../results/verification.json)

## Four figures

**Figure 1 · Functional supply boundary.** The [nominal model check](../src/analysis.py) identifies boundaries, pump endpoints and pressure sensors; [plotting code](../src/figures.py) lays out the interpretive diagram. Arrows summarize the intended functional supply route.

![Functional hydraulic supply boundary](../results/figures/figure1_supply_boundary.png)

**Figure 2 · Daily profiles.** Thin lines show each of the 273 days; the red line is the mean at each clock time. The left tank/pump panels span the same total height as the three right pressure panels. The nominal controls open PUMP_1 below 2.4 m and close it above 3.9 m. The plot shows daily variation in the local signals and supports the student's interest in their temporal relationships.

![Daily tank, pump and pressure profiles](../results/figures/figure2_daily_profiles.png)

**Figure 3 · Correlations.** The gold boundary separates the future label from six current signals. Persistence's small descriptive error and high n1 autocorrelation make it a strong reference. These pairwise associations motivate the planned comparison of lagged predictors, where C3 will measure additional value beyond n1 history.

![Six-signal and future-label correlation matrix](../results/figures/figure3_correlations.png)

**Figure 4 · Literature groups.** Counts are recomputed by joining source IDs and group assignments. Gold bars identify selected groups within each category. They are selected subsets of the five objective categories. The chart counts related-work groups. A diagnostic method can contain a future-pressure step while remaining in the leak category.

![Historical literature category counts](../results/figures/figure4_historical_screening.png)

The [screening notes](../literature/screening_notes.md) distinguish brief screening from the six detailed readings. Counting code verifies inventory membership and numerical consistency; the notes explain the focused review and its scholarly classifications. The [execution manifest](../results/run_manifest.json) records inputs, code, environment and outputs. [Submitted image bytes](../evidence/submitted_figures/) are retained separately: regenerated figures present the same quantities and layout using portable fonts.
