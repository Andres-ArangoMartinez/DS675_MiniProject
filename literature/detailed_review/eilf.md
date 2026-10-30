# Wang et al.: estimation, identification and localization framework

Wang, X., Li, J., Liu, S., Yu, X., & Ma, Z. (2022). *Multiple Leakage Detection and Isolation in District Metering Areas Using a Multistage Approach*. Journal of Water Resources Planning and Management, 148(6), 04022021. [Journal DOI](https://doi.org/10.1061/%28ASCE%29WR.1943-5452.0001558). Historical group `tsinghua`; sources `pdf-12`, `pdf-asce-2022`.

EILF means **estimation, identification and localization framework** (journal p. 2). This identifies the Wang et al. hydraulic framework; Li–Chen 2026 is a separate ensemble study. The licensed [Tsinghua conference report](../papers/P08a_Tsinghua-Team.pdf), [Zenodo source](https://doi.org/10.5281/zenodo.3924109), is distinct from the journal paper; the journal is accessible through its official DOI.

## Task, data preparation and engineering method

The task is overlapping-leak detection and isolation, with 2018 development and 2019 evaluation (journal p. 6). STL separates pressure trends from recurring variation; sustained changes and multiscale differences support detection, followed by hydraulic localization. The journal's pressure-trend equation (p. 3, Equation 3) describes the STL decomposition used for diagnosis; its numerical future-pressure lead remains unspecified.

For Area C, pump inflow minus the tank-storage change rate estimates sector outflow, with summed AMRs as a demand reference. Thirty-minute aggregation reduces level-rounding/inaccuracy effects (p. 7). This prior engineering contribution supports the student's interpretation of Area C. The final forecast proposal retains measured T1, pump flow and local AMR_n1 as its selected inputs.

## Implementation and published result

The journal's data-availability statement (p. 11) offers code on author request. The review uses the journal method and source passages. The earlier conference report separately mentions VAR; numerical lag/order and prospective pressure-lead details remain unspecified in the screened report.

Journal p. 11, Conclusions: **true-positive rate 47.83%, five false positives and EUR 167,981**. These are the authors' competition leak-diagnosis measures, interpreted using the competition's accepted-match criteria.

## Contribution to the proposed study

The source supports the hydraulic interpretation of Area C's pump/tank boundary and documents prior use of local engineering signals. The student's proposed extension focuses on the released-SCADA future n1 target and controlled forecast evaluation. The review retains the authors' reported diagnosis performance and the inspected source passages. [Source locators](../../evidence/literature_checks.json) distinguish the checked journal document from its conference predecessor.
