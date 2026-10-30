# SAM-kNN: adaptive virtual pressure sensors

Jakob, J., Artelt, A., Hasenjäger, M., & Hammer, B. (2022). *SAM-kNN Regressor for Online Learning in Water Distribution Networks*. In Artificial Neural Networks and Machine Learning – ICANN 2022, pp. 752–762. Springer. [DOI](https://doi.org/10.1007/978-3-031-15934-3_62). Historical group: `sam`; sources `pdf-32`, `repo-48`. The inspected author preprint is linked through the official publication; the official link provides access to that source.

## Task, data and method

The authors detect leaks and sensor faults using virtual pressure sensors. They generated **ten three-month Area A scenarios**, with 29 pressure sensors and five-minute sampling: five leak cases and five sensor-fault cases. The evaluation uses newly generated L-Town simulations (preprint PDF pp. 8–10).

SAM-kNN keeps recent examples in short-term memory, older useful examples in long-term memory, and a combined-memory predictor. It chooses the memory with the lowest tracked prediction error and updates online. Predicted-versus-observed pressure deviations support anomaly detection. Adaptive memories extend ordinary nearest-neighbor regression.

## Implementation actually inspected

[Author code](https://github.com/andreArtelt/SAM-kNN-Regressor_OnlineLearning_WDNs/tree/9116ec99bf9f053e35401fe3e388062e8b979c54), commit `9116ec99bf9f053e35401fe3e388062e8b979c54`.

- [`LeakDbScenarioPreprocessing.py`, lines 19–27](https://github.com/andreArtelt/SAM-kNN-Regressor_OnlineLearning_WDNs/blob/9116ec99bf9f053e35401fe3e388062e8b979c54/Implementation/LeakDbScenarioPreprocessing.py#L19): for window length four, average the first three rows and label with the fourth. The latest input is therefore five minutes before the label.
- [`FaultDetection.py`, lines 40–49](https://github.com/andreArtelt/SAM-kNN-Regressor_OnlineLearning_WDNs/blob/9116ec99bf9f053e35401fe3e388062e8b979c54/Implementation/FaultDetection.py#L40): exclude a target sensor from its own predictor inputs.
- [`experiments.py`](https://github.com/andreArtelt/SAM-kNN-Regressor_OnlineLearning_WDNs/blob/9116ec99bf9f053e35401fe3e388062e8b979c54/Implementation/experiments.py#L153): predict the batch before adapting.

The paper describes four-sample averaging; the inspected code averages three values before the fourth-row label. The review records both the paper description and the inspected implementation.

## Published result and interpretation

Preprint PDF p. 10, Table 1: all five leak cases are detected; SAM false-alarm counts are **48, 20, 3, 20, 17**, versus **17,057, 19,216, 11,146, 19,082, 18,751** for ordinary online kNN. These counts measure the anomaly-detection task on the authors' scenarios.

## Contribution to the proposed study

SAM contributes an example of temporal pressure learning with adaptive memories, peer sensors and new Area A scenarios. The student's proposal studies classical regressors on the released SCADA. Evidence for SAM consists of the paper, inspected preprocessing/model code and author-reported scores; the scenario data remain outside the available inspected materials. [Inspection evidence](../../evidence/literature_checks.json) identifies the checked bytes and locators.
