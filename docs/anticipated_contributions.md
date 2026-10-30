# Your anticipated contributions

The student's proposed contribution is a **controlled pressure-forecasting study motivated by local hydraulic knowledge**. It asks whether recorded n1 pressure at +15 minutes can be forecast more accurately using the selected Area C signals and a manageable set of classical regressors. [Milestone 2, Section 3](../reports/Milestone2.pdf#page=4) records the plan; the [contribution statement](student_contributions.md) traces student choices and AI methodological recommendations.

The focused review provides related next-step predictors, longer-window head forecasts, current-state reconstruction and hydraulic diagnosis. The proposed investigation adds a common n1(+15) target, released SCADA, six local signals and an explicit auxiliary-signal comparison to that reviewed context. Its contribution is the **specific experimental question, reproducible preparation and understanding gained from controlled comparisons**. Gradient Boosting is an established method, also used for L-Town leakage classification.

| Planned contribution | What will be prepared or compared | How its value will be judged |
|---|---|---|
| **C1 · Prepared forecast data** | Match available past measurements with n1 three five-minute readings ahead. | Correct timestamp alignment, units and period boundaries, with predictors available at forecast time. |
| **C2 · Model comparison** | Gradient Boosting against persistence, Ridge and Random Forest. | MAE on identical forecast rows, supplemented by RMSE and practical tradeoffs. |
| **C3 · Value of extra signals** | Full-signal Gradient Boosting against n1-history Gradient Boosting with the **same calendar variables**. | Improvement relative to the reduced model and persistence, with all comparison outcomes reported. |

**Current stage:** descriptive EDA and a persistence reference are completed. **Next stage:** the C1–C3 learning experiments and final chronological assessment.

## Data preparation and learning models

Start with the current reading and the previous **55 minutes at five-minute intervals**: twelve readings for each signal, at lags 0, 5, …, 55 minutes. Include time of day and day of week. Calendar encoding and model settings will be specified during implementation. Eligible rows have complete predictor histories and a target within their assigned period. Fit Ridge scaling on training data. Hydraulic reasoning and correlations motivate the candidates; C3 will measure their joint incremental value.

[Gradient Boosting](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html) adds small decision trees that correct earlier prediction errors. Persistence repeats current n1. [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html) fits a penalized linear relationship. [Random Forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html) averages many trees. This comparison builds on regression and ensemble ideas at a manageable project scale.

## Chronological evaluation

Train on January–September 2018, select settings using October–December 2018, then refit on eligible 2018 rows and assess 2019. Since 2019 has already received limited inspection, it is described as the **final chronological assessment**. Model-setting decisions use the development/validation periods.

Every model predicts the same recorded target on the same eligible rows. Report **MAE** and **RMSE** in metres: average absolute error and a measure that gives larger errors greater weight. A boosting advantage requires lower MAE than all three comparators. C3 holds the model family, calendar variables and rows fixed to evaluate the auxiliary set jointly; individual-signal attribution requires its own comparison.

Expected outputs are an annotated preparation/model notebook, a comparison table and forecast/error plots. Results showing either a useful auxiliary-signal gain or comparable performance with a simpler predictor will help answer the student's engineering question.
