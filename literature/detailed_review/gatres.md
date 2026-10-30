# GATRes: reconstruction of current hidden pressures

Truong, H., Tello, A., Lazovik, A., & Degeler, V. (2024). *Graph Neural Networks for Pressure Estimation in Water Distribution Systems*. Water Resources Research, 60(7), e2023WR036741. [DOI](https://doi.org/10.1029/2023WR036741) · [Retained PDF](../papers/P15_GATRes_2024.pdf). Historical group `gatres`; sources `pdf-20`, `repo-50`.

## Task, preparation and model

The target is **current pressure at unobserved nodes**. Section 6.4 (PDF pp. 19–20) describes 10,000 generated L-Town snapshots, split 60/20/20 for training/validation/test, and comparison of pressure distributions with time-series test conditions. Its training states are newly generated simulations.

Known sensor readings form a graph input. Selected inputs are hidden with zeros; graph attention weights neighboring information, and residual connections help information pass through the network. The model reconstructs hidden pressures from the **same snapshot**. Random sensor placement during training supports estimation with different observed sensors. Graph attention is more advanced than the classical regression models proposed here.

## Implementation actually inspected

[Author repository](https://github.com/DiTEC-project/gnn-pressure-estimation/tree/bb287ed2ae091b29fa19f2417406756b57a45a1f), commit `bb287ed2ae091b29fa19f2417406756b57a45a1f`.

- [`utils/auxil.py`, lines 84–98](https://github.com/DiTEC-project/gnn-pressure-estimation/blob/bb287ed2ae091b29fa19f2417406756b57a45a1f/gnn_pressure_estimation/utils/auxil.py#L84): construct input/label from the same pressure data before masking.
- [`train.py`, lines 172–178 and 255–261](https://github.com/DiTEC-project/gnn-pressure-estimation/blob/bb287ed2ae091b29fa19f2417406756b57a45a1f/gnn_pressure_estimation/train.py#L172): mask inputs and evaluate the corresponding hidden label values.

These passages establish same-time reconstruction; the separate [data loader](https://github.com/DiTEC-project/gnn-pressure-estimation/blob/bb287ed2ae091b29fa19f2417406756b57a45a1f/gnn_pressure_estimation/utils/DataLoader.py) is also identified in the inspection record. Together they document the inspected data/masking procedure.

## Published result and interpretation

PDF p. 20, Table 10: L-Town **MAE 0.9501 ± 0.0086 m**, compared with **1.5928 ± 0.0050 m** for mGCN, over ten training runs. The ± value is the between-run standard deviation. The surrounding text describes one week, while the table caption says 24 hours; that duration discrepancy is retained.

## Contribution to the proposed study

The Table 10 result measures current hidden-pressure reconstruction and is retained as the authors' comparison used in Milestone 2. Its generated distributions, observation masks and evaluation settings identify the comparison context. The student's forecasting study uses its own common target, horizon and rows for model ranking. [Inspection evidence](../../evidence/literature_checks.json).
