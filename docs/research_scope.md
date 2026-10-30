# Dataset and learning task

The student selected a pressure-management question and developed a hydraulically focused study of Area C with AI-assisted analysis; see [student contributions and collaboration](student_contributions.md). The controlling specification is [Milestone 2, Section 1](../reports/Milestone2.pdf#page=1). The original source is [Vrachimis et al., Dataset of BattLeDIM](https://doi.org/10.5281/zenodo.4017659), supported by the [2022 benchmark paper](https://doi.org/10.1061/%28ASCE%29WR.1943-5452.0001601). L-Town is a simulated drinking-water network inspired by Cyprus, released for leak detection and localization. Its simulated SCADA observations provide a documented setting for studying the proposed forecast.

Each year, 2018 and 2019, has 105,120 five-minute records: **210,240 timestamps and 119 numerical channels** overall. The channels are 33 pressures (m water head), three flows (m³/h), one T1 level (m) and 82 AMR consumptions (L/h). AMR records junction consumption. All eight annual tables have matching unique timestamps within their year and complete values, as checked by [the analysis code](../src/analysis.py) and [table results](../results/table_checks.json). The benchmark describes ideal telemetry and two-decimal rounding; recorded pressure averages the preceding five minutes. Application to field sensors would require validation under their measurement and operating conditions.

The nominal model contains 782 demand junctions, two reservoirs, one tank, 905 pipes, one pump and three PRVs. Nominal and generator parameters differ; this repository's path and sector checks use the released **nominal** `L-TOWN.inp`.

## Target and selected measurements

The supervised regression label is `p_n1(u + 15 minutes)`, three records after forecast origin `u`. It is the recorded five-minute average ending at that future time, under the simulated operating and leakage conditions. This is a continuous regression target. Predictors comprise the selected measurements and calendar information available when the forecast is issued.

| Selected signal | Unit | Student's engineering rationale |
|---|---|---|
| n1 pressure | m | History of the target pressure. |
| n4 and n31 pressures | m | Two additional observed pressures in Area C. |
| T1 level | m | Tank storage state at the sector boundary. |
| PUMP_1 flow | m³/h | Measured tank inflow; may inform later storage changes. |
| AMR_n1 demand | L/h | Consumption assigned directly to the target junction. |

Area C is tank-fed and contains 92 junctions, three pressure sensors and 82 AMRs. The reduction is **119 channels → 87 Area C/boundary candidates → six signals**. The 87 consist of three pressures, one level, 82 demands and pump flow. PRV-3's sector has only one measured pressure, whereas C offers related peer measurements. The tank boundary gives the student a clear engineering basis for a manageable local feature set, while upstream operation remains part of the system context.

Shortest initially open pipe paths from T1 to measured nodes are **891.3208 m (n1), 573.7565 m (n4), 307.7926 m (n31)**. Dijkstra's algorithm sums nominal pipe lengths, excludes pump/PRV links and treats the pipe graph as undirected. This calculation ranks n1 as the most distant of the three measured pressure nodes along the stated nominal pipe paths.

[Figure 1](../results/figures/figure1_supply_boundary.png) is an interpretive schematic of the functional supply route. PRV settings 40/50/35 m describe the nominal model; remote pressure behavior also depends on network operating conditions. [Topology outputs](../results/topology_audit.json) record the connections, settings and path calculations.

The [EDA](exploratory_analysis.md) explains why the task is feasible and persistence is demanding. [C1–C3](anticipated_contributions.md) will quantify the auxiliary signals' joint forecast value, building on the descriptive associations and hydraulic reasoning.
