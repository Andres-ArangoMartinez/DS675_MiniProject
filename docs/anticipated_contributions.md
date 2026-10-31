# Your anticipated contributions

The proposed study asks whether established regressors and six local Area C signals can improve **recorded n1 pressure forecasts at +15 minutes**. [Milestone 2, Section 3](../reports/Milestone2.pdf#page=4) records the plan; [student/AI attribution](student_contributions.md) distinguishes the student's task and scope decisions from AI methodological recommendations.

The focused review covers next-step predictors, longer-window head forecasting, current-state reconstruction and leak diagnosis. The proposed extension is a common released-SCADA n1(+15) task with hydraulically selected signals and controlled comparisons. Its intended contribution is evidence about forecast accuracy and auxiliary-signal utility within that reviewed context. Gradient Boosting is established and has also been used for L-Town leakage classification.

| Proposed experiment | Preparation or comparison | Evaluation criterion |
|---|---|---|
| **C1 · Forecast data** | Pair available measurements with n1 three five-minute readings ahead. | Correct timestamps, units and period boundaries; predictors available at forecast time. |
| **C2 · Model comparison** | Gradient Boosting versus persistence, Ridge and Random Forest. | MAE on identical rows, supplemented by RMSE and practical tradeoffs. |
| **C3 · Auxiliary signals** | Full-signal versus n1-history Gradient Boosting, with the **same calendar variables**. | Error differences relative to the reduced model and persistence; report all outcomes. |

Descriptive exploratory analysis and the persistence reference are completed. **C1–C3 training, selection and the planned final chronological assessment remain proposed.**

## Data preparation and learning models

Use the current reading and previous **55 minutes at five-minute intervals**: twelve readings per signal, at lags 0, 5, …, 55 minutes. Include time of day and day of week; specify encoding and model settings during implementation. Eligible rows require complete histories and a target within their assigned period. Fit Ridge scaling on training data only. Keep leak labels outside the predictors.

[Gradient Boosting](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html) adds trees that correct earlier errors. Persistence repeats current n1; [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html) fits a penalized linear relationship; [Random Forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html) averages trees.

## Chronological evaluation

Train on January–September 2018, select settings using October–December 2018, then refit on eligible 2018 rows and assess 2019. Because 2019 has received limited inspection, retain the term **planned final chronological assessment**. Use development/validation periods for model-setting decisions.

Compare identical targets and eligible rows using **MAE** and **RMSE** in meters: average absolute error and a measure giving larger errors greater weight. A boosting advantage requires lower MAE than all three comparators. C3 holds model family, calendar variables and rows fixed to test the auxiliary set jointly; individual-signal attribution requires a separate comparison. Auxiliary-signal value requires lower MAE than the reduced model and persistence; report RMSE tradeoffs and cases with no gain.

Planned outputs are an annotated preparation/model notebook, a comparison table and forecast/error plots. Either an auxiliary-signal gain or comparable performance from a simpler predictor would answer part of the proposed question.

## Additional Engineering Hypothesis Identified After Milestone 2 Feedback

The small persistence error reported in the descriptive analysis raises an operational question: the persistence method depends on the availability and accuracy of the n1 pressure measurement. Its good performance under valid telemetry conditions does not guarantee its reliability when the sensor becomes unavailable, biased, or frozen at a fixed value.

This motivates a possible extension of the proposed forecasting study: to evaluate whether the five auxiliary Area C signals can maintain useful n1 pressure forecasts when the target sensor is unreliable. This extension would examine two complementary indicators:

- Temporal residual: the difference between the current n1 pressure measurement and its value recorded 15 minutes earlier.
- Cross-sensor consistency residual: the difference between the current n1 pressure measurement and an independent estimate of the current pressure based on n4, n31, T1, PUMP_1, and AMR_n1.

The joint patterns of these two residuals could provide a basis for formulating hypotheses about hydraulic changes and measurement inconsistencies, as summarized in the following table:

| Temporal Residual | Consistency Residual | Hypothesis to Test|
|---|---|---|
| Low | Low | Measurements are consistent with both references. |
| High | Low | Temporal variation also explained by the auxiliary signals; possible real hydraulic change. |
| Low | High | Inconsistency with auxiliary signals; possible frozen, biased, or faulty sensor. |
| High | High | Ambiguous event requiring additional information. |
| n1 unavailable | Not calculable | Loss of telemetry; evaluate forecasting using the five remaining signals. |

A controlled experimental extension would allow a separately trained forecasting model that uses only the auxiliary signals to be compared against relevant reference methods during simulated n1 sensor outages and faults. The original, uncorrupted measurements would be retained for evaluation. Available leakage-event records could support retrospective analysis of hydraulic events, but they would not be used to establish sensor-fault labels or provided to the predictor as future information.

Forecast accuracy would be evaluated using MAE (Mean Absolute Error) and RMSE (Root Mean Squared Error) over matched chronological periods. Any fault-detection component would require separately defined detection thresholds, false-alarm rates, detection rates, and detection delays.

Existing research on virtual pressure sensors, pressure estimation at unmeasured locations, and residual-based anomaly detection—including SAM-kNN, GATRes, and LILA—provides relevant precedents. Therefore, the potential contribution consists of conducting a controlled assessment of the relationship between forecast accuracy, dependence on the target sensor, and the reliability of auxiliary measurements for the selected Area C forecasting task.

Status and Scope: This hypothesis emerged after reviewing the Milestone 2 feedback. It was not part of the originally submitted experiments, and no sensor-fault model, residual-based classifier, or auxiliary-only forecasting model has yet been implemented or evaluated. Components C1–C3 remain the defined Milestone 2 proposal.
