# Literature collection

The historical collection supporting [Milestone 2, Section 2](../reports/Milestone2.pdf#page=3) contains **47 source records assigned to 35 groups of related works** on L-Town or explicit modifications. Different papers, journal/conference versions and related code may share a group because they describe the same method. Percentages use related-work groups as their denominator.

The student directed the relevance criteria and critical review; AI assisted discovery, source/code inspection and technical synthesis. This focused search started from the dataset, benchmark and competition reports, following citations and author repositories. Search topics included BattLeDIM/L-Town pressure prediction, forecasting, reconstruction, leak diagnosis and available implementations. The collection is a focused review supported by retained source records and grouping decisions. Those records provide the basis for reproducing the inventory; historical search-query coverage remains partial.

[All 47 sources](source_records.csv) · [35 group assignments](groups.csv) · [notes for every group](screening_notes.md) · [paper/download index](papers/README.md) · [full recovered metadata](bibliography.json)

| Primary objective | Groups | Share of 35 | Detailed selections |
|---|---:|---:|---|
| Leak detection / localization | 27 | 77.1% | ChebNet, LILA, EILF |
| Current-pressure estimation | 3 | 8.6% | GATRes |
| Future pressure / head forecasting | 2 | 5.7% | AGN |
| Anomaly / sensor-fault detection | 2 | 5.7% | SAM-kNN |
| Sensor placement | 1 | 2.9% | None |

The category describes the main purpose. ChebNet and SAM-kNN have future-pressure components despite diagnostic primary tasks. Brief screening also identifies next-record pressure prediction in AIGNN; the six selected groups form the focused comparison in the submitted report. AGN and the patent form the primary-forecast category; the patent reports future-pressure outputs, with physical-horizon detail remaining unspecified in the screened evidence. [Counting code](../src/screening.py) validates membership and totals; the source notes explain each classification.

## Six detailed studies

| Study | Why selected / relation to the proposal |
|---|---|
| [ChebNet](detailed_review/chebnet.md) | Next-step pressure learning inside leak diagnosis; shows a temporal graph approach. |
| [SAM-kNN](detailed_review/sam_knn.md) | Adaptive online virtual-sensor regression with a next-record pressure target. |
| [AGN](detailed_review/agn.md) | Multistep future heads on modified L-Town; differs in data and output scope. |
| [LILA](detailed_review/lila.md) | Same-time healthy-pressure reference, useful for distinguishing estimation from forecasting. |
| [GATRes](detailed_review/gatres.md) | Graph reconstruction of current hidden pressures from available sensor readings. |
| [Wang et al. EILF](detailed_review/eilf.md) | Existing pump/tank-balance reasoning relevant to the selected sector. |

The reviews separate data/preparation, model, inspected code, reported score and relevance to n1(+15). Scores are the original authors' published results. The submitted table is preserved in the original PDF, and the reviews retain relevant paper/code differences. Paper and code hashes/locators are recorded in [source checks](../evidence/literature_checks.json).

## Feedback-related supplement and archived material

[Ahmed et al. (2025)](ahmed_feedback.md) was specifically requested by the professor. It is a separate feedback supplement alongside the historical 47-record, 35-group inventory and six selected studies. Its five Area C signals overlap with this proposal; its reconstruction-based leak detection differs from the proposed regression target.

The [48-entry paper catalog](papers_catalog.csv) includes permitted PDFs, official links and additional supporting/background items retained from the collection. The counted inventory is defined separately by the 47 source records and their 35 group assignments. The paper catalog also preserves supporting reviews, external networks and tools. Historical group labels have been translated into English; source IDs, mappings, locators, hashes, commits and actual publication titles are preserved. Original publication edition identifiers remain in bibliographic metadata.

Public PDFs remain unmodified and are included only with license evidence. Restricted journal papers are linked, even when an earlier openly licensed conference report is available. Automated publisher access blocks are documented in [link checks](../evidence/external_links.json); they identify the actual retrieval conditions. See [redistribution terms](../NOTICE.md).
