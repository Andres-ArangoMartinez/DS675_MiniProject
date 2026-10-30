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
