# Dataset and learning task

The student selected BattLeDIM/L-Town and a local pressure-forecasting task; [recorded contributions](student_contributions.md) identify his choices and AI assistance. [Milestone 2, Section 1](../reports/Milestone2.pdf#page=1) specifies the task. The [official dataset](https://doi.org/10.5281/zenodo.4017659) and [2022 benchmark paper](https://doi.org/10.1061/%28ASCE%29WR.1943-5452.0001601) describe a simulated drinking-water network inspired by Cyprus, released for leak detection and localization.

2018 and 2019 each contain **105,120 five-minute records**: **210,240 timestamps and 119 numerical channels** overall. Channels comprise 33 pressures (m water head), three flows (m³/h), one T1 level (m) and 82 AMR junction consumptions (L/h). [Code](../src/analysis.py) and [table checks](../results/table_checks.json) verify complete values and matching unique timestamps within each year across all eight tables. The benchmark describes ideal telemetry and two-decimal rounding; each pressure record averages the preceding five minutes. Field-sensor use would require validation under actual measurement and operating conditions.

The released **nominal** `L-TOWN.inp` used for sector/path checks contains 782 demand junctions, two reservoirs, one tank, 905 pipes, one pump and three PRVs. Nominal and generator parameters differ.

## Target and selected measurements

The continuous supervised-regression label is `p_n1(u + 15 minutes)`: the recorded five-minute average ending three samples after forecast origin `u`, under simulated operating and leakage conditions. Predictors use measurements and calendar information available at issue time.

| Signal | Unit | Engineering rationale |
|---|---|---|
| n1 pressure | m | Target history. |
| n4 and n31 pressures | m | Peer Area C observations. |
| T1 level | m | Tank storage state at the sector boundary. |
| PUMP_1 flow | m³/h | Tank inflow; a candidate indicator of later storage changes. |
| AMR_n1 demand | L/h | Consumption assigned to the target junction. |

Tank-fed Area C contains 92 junctions, three pressure sensors and 82 AMRs. The selection narrows **119 channels → 87 Area C/boundary candidates → six signals**. The 87 candidates are three pressures, one level, 82 demands and pump flow. PRV-3's sector has one measured pressure; Area C provides peer measurements and a local tank boundary. Upstream operation remains part of the system context.

Shortest initially open pipe paths from T1 measure **891.3208 m (n1), 573.7565 m (n4), 307.7926 m (n31)**. Dijkstra's algorithm sums nominal lengths on an undirected pipe graph, excluding pump/PRV links. n1 is the most distant of these three measured pressure nodes by this calculation. These are nominal path lengths, not measured hydraulic delays.

[Figure 1](../results/figures/figure1_supply_boundary.png) depicts the functional supply route. PRV settings **40/50/35 m** describe the nominal model; remote pressures also depend on operating conditions. [Topology outputs](../results/topology_audit.json) document settings, connections and paths. The [descriptive exploratory analysis](exploratory_analysis.md) provides observed associations; [C1–C3](anticipated_contributions.md) propose testing the auxiliary signals' joint forecast value.
