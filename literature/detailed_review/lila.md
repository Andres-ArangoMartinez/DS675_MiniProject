# LILA: current healthy-pressure estimation and leak diagnosis

Daniel, I., Pesantez, J., Letzgus, S., Khaksar Fasaee, M. A., Alghamdi, F., Berglund, E., Mahinthakumar, G., & Cominola, A. (2022). *A Sequential Pressure-Based Algorithm for Data-Driven Leakage Identification and Model-Based Localization in Water Distribution Networks*. Journal of Water Resources Planning and Management, 148(6), 04022025. [Journal DOI](https://doi.org/10.1061/%28ASCE%29WR.1943-5452.0001535). Group `lila`; sources `pdf-5`, `pdf-6`, `repo-52`, `repo-55`.

The separately licensed [2020 Leakbusters report](../papers/P02a_Leakbusters.pdf), [Zenodo DOI](https://doi.org/10.5281/zenodo.3924632), is an earlier document. The journal results below come from the journal, accessed through its official publication link.

## Task, preparation and model

Using released SCADA, the method estimates a **current healthy-pressure reference**, detects leaks and then localizes them hydraulically. Pressure/flow analysis informs reference-sensor choice. Healthy calibration periods and some per-leak node combinations are manually selected. Journal pp. 3–4, Equations 12–13, express current pressure using peer pressures and squared flow. A linear regression provides the reference; CUSUM accumulates sustained residual changes, followed by hydraulic localization. Its regression estimates a reference for the current condition.

## Implementation actually inspected

[LILA author repository](https://github.com/SWN-group-at-TU-Berlin/LILA/tree/b488a60db1974b6f5b7887ce1cf5d31dff3dad68), commit `b488a60db1974b6f5b7887ce1cf5d31dff3dad68`.

[`_utils/BattLeDIM_utils.py`, lines 219–226 and 266–293](https://github.com/SWN-group-at-TU-Berlin/LILA/blob/b488a60db1974b6f5b7887ce1cf5d31dff3dad68/_utils/BattLeDIM_utils.py#L219) passes the PUMP_1 column directly to the same-time regression, as a direct predictor in that routine. The paper's squared-flow expression and this inspected routine differ. The observation is specific to this inspected routine; upstream processing is a separate implementation question. The historical collection also retains a [related localization repository](https://github.com/jorgeps86/LeakLocalization/tree/1c9493847bf37d609ae89310443bc61ee42206f8).

## Published result and interpretation

Journal p. 7, Table 1: for **19 new 2019 leaks** (four inherited events excluded), **17 true positives, two false positives, zero false negatives; precision 0.895, recall 1.000, F1 0.944 and EUR 307,852**. Two locations outside 300 m count as false positives under this accounting. Recall and the 300 m location criterion describe complementary parts of leakage-diagnosis performance.

## Contribution to the proposed study

LILA shows useful same-time pressure/flow modeling and the importance of a reference condition. It contributes a current-state comparator with reference regression, CUSUM and hydraulic localization. Calibration decisions and paper/code differences are documented to guide interpretation. The review draws on inspected source passages and the authors' reported diagnosis scores. [Source-check evidence](../../evidence/literature_checks.json).
