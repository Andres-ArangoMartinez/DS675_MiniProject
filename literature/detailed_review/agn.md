# AGN: multistep future nodal heads

Zou, Z., Long, Z., Zhu, Z., Shao, Y., & Yu, T. (2025). *Explainable graph neural network for real-time demand states forecasting in water distribution system*. Results in Engineering, 27, 106911. [DOI / publisher](https://doi.org/10.1016/j.rineng.2025.106911). Group `agn`; source `editorial-agn`.

**Task/data/preparation.** The submitted table describes future nodal heads (pressure head plus elevation), using one generated year on modified L-Town, 104 demand patterns, five-minute records and chronological 70/20/10 splits (Sections 2–3).

**Method/implementation.** Graph propagation, recurrent units and attention combine network/history information. The report describes progressively reduced input hiding. Implementation evidence for this review is the inspected article's method description and its data-on-request statement. The inspected version supplied the paper-based evidence; identifying an executable author repository remains an open source-access item.

**Published results.** Section 3.2/Table 1 uses 12/24/48/96-step outputs: terminal leads of 1/2/4/8 hours. At 12 steps, regional MAE is 0.859/0.327/32.7 m for high/medium/low elevation. These aggregate scores describe entire forecast windows and elevation regions.

**Contribution to the proposed study.** AGN provides a multistep future-head approach using modified data and network-wide targets. Its regional/window evaluation illustrates the importance of matching data, targets and horizons when comparing scores. The review uses indexed full-text inspection, with formula/figure coverage identified in the source records. Reported scores retain their author attribution. [Inspection locators](../../evidence/literature_checks.json).
