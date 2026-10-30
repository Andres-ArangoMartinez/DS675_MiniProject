# Literature collection

The inventory supporting [Milestone 2, Section 2](../reports/Milestone2.pdf#page=3) contains **47 source records assigned to 35 related-work groups** on L-Town or explicit modifications. Papers, conference/journal versions and associated code may share a method group. Percentages use groups as the denominator.

The student defined objective-based and future-pressure relevance criteria; AI assisted discovery, source/code inspection and synthesis. Retained records document the sources, grouping decisions and screening notes. **Historical search-query coverage is partial**, so the inventory establishes a focused review rather than a complete search chronology. [Recorded criteria and later account](../evidence/ai_interactions/README.md).

[47 sources](source_records.csv) · [35 assignments](groups.csv) · [group notes](screening_notes.md) · [paper index](papers/README.md) · [recovered metadata](bibliography.json)

| Primary objective | Groups | Share of 35 | Detailed selections |
|---|---:|---:|---|
| Leak detection / localization | 27 | 77.1% | ChebNet, LILA, EILF |
| Current-pressure estimation | 3 | 8.6% | GATRes |
| Future pressure / head forecasting | 2 | 5.7% | AGN |
| Anomaly / sensor-fault detection | 2 | 5.7% | SAM-kNN |
| Sensor placement | 1 | 2.9% | None |

Primary objectives differ from intermediate computations: ChebNet and SAM-kNN include future-pressure steps within diagnostic methods. Screening also identifies next-record prediction in AIGNN. AGN and the patent form the primary-forecast category; the patent's physical prediction horizon is unspecified in the screened evidence. [Counting code](../src/screening.py) checks membership/totals; notes explain classifications.

## Six detailed studies

| Study | Selection rationale |
|---|---|
| [ChebNet](detailed_review/chebnet.md) | Next-step graph pressure learning within leak diagnosis. |
| [SAM-kNN](detailed_review/sam_knn.md) | Adaptive online regression with a next-record virtual-pressure target. |
| [AGN](detailed_review/agn.md) | Multistep future heads on modified L-Town data. |
| [LILA](detailed_review/lila.md) | Same-time healthy-pressure regression, distinguishing estimation from forecasting. |
| [GATRes](detailed_review/gatres.md) | Reconstruction of current hidden pressures from sensor readings. |
| [Wang et al. EILF](detailed_review/eilf.md) | Pump/tank-balance reasoning relevant to Area C. |

Reviews separate task, preparation, model, inspected implementation, published metrics and relevance to n1(+15). Scores remain author-reported; paper/code differences and unavailable implementations retain their qualifications. [Inspection records](../evidence/literature_checks.json) preserve locators and fingerprints. The original report table remains in the retained PDF.

## Feedback-related supplement and archived material

The professor requested [Ahmed et al. (2025)](ahmed_feedback.md). It remains **outside the historical 47/35/six inventory**. Its five shared Area C signals support reconstruction-based leak detection, distinct from the proposed forecast.

The [48-entry paper catalog](papers_catalog.csv) also contains background studies, external networks and tools. It is separate from the counted inventory. English group labels preserve source IDs, mappings, publication titles, editions, locators, hashes and commits.

The catalog records declared licenses and supporting evidence for unmodified public PDFs. Restricted papers retain official links, including where a separately licensed conference predecessor is available. [External-link checks](../evidence/external_links.json) record retrieval/access conditions; the [source notice](../NOTICE.md) states the evidence basis.
