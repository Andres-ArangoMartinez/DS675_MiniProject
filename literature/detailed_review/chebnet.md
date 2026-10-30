# ChebNet: next-step pressure inside leak diagnosis

Garðarsson, G. Ö., Boem, F., & Toni, L. (2022). *Graph-Based Learning for Leak Detection and Localisation in Water Distribution Networks*. IFAC-PapersOnLine, 55(6), 661–666. [DOI](https://doi.org/10.1016/j.ifacol.2022.07.203) · [Original permitted PDF](../papers/P10_Graph_based_learning_2022.pdf). Historical group: `chebnet`; sources `pdf-14`, `repo-51`.

## Task, data and method

The ultimate task is L-Town leak detection/localization. The method includes a **+5-minute pressure predictor** and a current-pressure reconstructor. It trains on leak-free nominal simulations and network connections, using three past five-minute pressure readings and an 80/20 training/validation split. Two networks, each with four Chebyshev graph-convolution layers, use network links to share pressure information. Differences between predicted healthy pressure and current reconstruction are processed over seven days to help locate leaks. The paper compares graph/scaling alternatives (PDF pp. 3–5).

## Implementation actually inspected

[Author repository](https://github.com/GardarGardarsson/GSP_for_Leak_Detection/tree/864a99041af6331375946a8fad3a71c633108eb8), pinned commit `864a99041af6331375946a8fad3a71c633108eb8`.

- [`data_loader.py`, lines 266–293](https://github.com/GardarGardarsson/GSP_for_Leak_Detection/blob/864a99041af6331375946a8fad3a71c633108eb8/04%20Leakage%20Detection/utils/data_loader.py#L266): the input ends at row `i-1`; prediction uses `y[i]`, reconstruction uses `y[i-1]`. With five-minute sampling, the predictor's next row is +5 minutes.
- [`predict.py`, lines 120–131](https://github.com/GardarGardarsson/GSP_for_Leak_Detection/blob/864a99041af6331375946a8fad3a71c633108eb8/04%20Leakage%20Detection/predict.py#L120): data cleaning/scaling occurs before the 80/20 split. The inspected implementation records this cleaning/scaling → split sequence.

## Published result and interpretation

Paper Table 1 (PDF pp. 5–6) reports **19 accepted matches, 138 false alarms, four missed leaks, recall 82.61% and EUR 326,521** for 2019 diagnosis. An accepted location must be within 300 m while the leak is active. These numbers quantify leak-diagnosis outcomes, including the false-alarm burden.

## Contribution to the proposed study

This is a core example of temporal pressure learning inside another task. It differs from the proposed released-SCADA n1(+15) regression in training data, horizon, model and evaluation target. Graph filtering is more advanced than the planned classical regression comparison. The review uses the authors' reported alarm scores and the inspected implementation as its evidence. [Source inspection evidence](../../evidence/literature_checks.json) records paper locators and code hashes.
