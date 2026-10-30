# Student research contributions and AI collaboration

## 1. Purpose and evidence standard

**The student's contribution is the engineering direction of the project:** Andres Arango Martinez connected a pressure-management problem from his control-engineering interests to a supervised-learning task, chose BattLeDIM/L-Town, proposed a hydraulically related sensor group, selected n1 and refined the six local signals. His questions and revisions also shaped the literature comparison, visual analysis and achievable course-level scope.

This guide makes those contributions easy to trace. It connects the unchanged [Milestone 1](../../reports/Milestone1.pdf) and [Milestone 2](../../reports/Milestone2.pdf) reports to student instructions, AI recommendations, technical executions and later explanations. The [feedback response](../../docs/professor_feedback.md) organizes the resulting evidence for the professor.

Three examples show the student's role in developing the research question:

- [Proposed n1/n4/n31 together with T1 and pump flow](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-021.txt#L3003) as a local hydraulic cohort.
- [Restricted the AMR scope and specified the figure layout](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-034.txt#L887) to keep the analysis focused and readable.
- [Defined objective-based literature screening](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-018.txt#L1191) and asked specifically about future-pressure components.

AI supported this direction with methodological proposals, source/code inspection, technical synthesis, generated/executed code and drafting. The chronological links show how recommendations and student choices developed together.

| Evidence type | What it contributes to the record |
|---|---|
| Direct student instruction | The student's recorded questions, proposals, decisions, technical explanations and revisions |
| AI recommendation | The model's visible formulation, methodological suggestion, interpretation or draft |
| Recorded execution | Tool inputs, completion status, outputs and file changes identifying the implementation/execution role |
| Retrospective student account | The student's dated explanation of personal work and reasoning, presented with that evidence type |
| Later reproduction | A dated, rerunnable calculation linking source data, code and output |

Attribution follows the content and sequence of the exchanges. This supports a clear account of student leadership and AI collaboration. Report-preparation exchanges and the October 27–29 feedback/repository work are identified by their recorded dates.

## 2. Evidence collection and navigation

The collection contains **16 readable views**: eleven partial ChatGPT conversations, three Codex session snapshots, a Codex database-supplement notice and **T16, a continuation of T02**. The Codex session set comprises two historical research sessions and a recovery/support session. The [conversation index](conversation_index.csv) links every view to its README and ordered text parts; [record_index.csv](record_index.csv) locates messages and events.

| Navigation | What it supplies |
|---|---|
| [A01–A10 crosswalk](contribution_links.md) / [CSV](contribution_links.csv) | 31 selected source locators supporting the ten research/report activities |
| [Repository-construction contributions](repository_construction_contributions.csv) | Five later activities R01–R05 with student, AI and available execution links |
| [T16 continuation](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03-repository-continuation/README.md) | Feedback-repository assembly and public-evidence decisions, captured through **2026-10-29 18:38:33.583 UTC** |
| [Redaction register](redactions.csv) | Source offsets/lines, category, reason, replacement marker and public locator for every changed span |
| [Integrity manifest](manifest.json) | Source-view fingerprints, ordered part ranges/hashes and raw-prefix continuity for T16 |
| [Source comparison](verification.json) | Preservation checks, including the earlier 15-view record and the added continuation |
| [Publication procedure](publication_procedure.md) | Preparation of the public derivatives and the appended continuation |

The **148 numbered `.txt` parts** preserve the source order; their numbers identify sequence positions. Concatenating each view's parts directly reconstructs its public derivative. Original languages, corrections, historical identifiers and available truncation notices are retained. New explanatory text is in English. Historical links and source-relative paths remain as recorded references; the indexes identify the files actually available publicly. The archived word “private” describes the original source copy, and the current README describes its authorized public derivative.

## 3. Detailed contribution evidence, A01–A10

### A01. Research direction and BattLeDIM/L-Town dataset selection

#### What the records show

The student defined an interest in dynamic control, multivariable/nonlinear modeling and predictive learning. ChatGPT organized a candidate-search specification, and the student explicitly selected BattLeDIM/L-Town. Milestone 1 records the pressure-forecasting motivation and the comparison with BATADAL.

#### Student contribution

The student established the engineering direction and explicitly chose the dataset. [Student request defining the control/modeling interest](chatgpt/6a92eec0-f09c-83e9-a9ed-29d95f24d41b/part-001.txt#L2841) and [Student decision to focus on BattLeDIM/L-Town](chatgpt/6ac80fb7-1dd8-83e9-a613-b73391e48697/part-001.txt#L44).

#### AI assistance

ChatGPT formulated the search prompt and possible supervised mappings, including prediction from current/past measurements. That formalization is visible AI work: [AI-generated dataset-search specification](chatgpt/6a92eec0-f09c-83e9-a9ed-29d95f24d41b/part-001.txt#L2848).

#### Technical or academic significance

The choice connects a supervised regression task to the student's pressure-management interests. The [dataset description](../../docs/research_scope.md) identifies simulated SCADA, five-minute sampling, available channels and the official source and the criteria for selecting a suitable predictive-learning dataset.

#### Direct source evidence

[Direction supplied by the student](chatgpt/6a92eec0-f09c-83e9-a9ed-29d95f24d41b/part-001.txt#L2841) · [AI search formulation](chatgpt/6a92eec0-f09c-83e9-a9ed-29d95f24d41b/part-001.txt#L2848) · [Explicit BattLeDIM choice](chatgpt/6ac80fb7-1dd8-83e9-a613-b73391e48697/part-001.txt#L44).

#### What this evidence establishes

The evidence establishes the student's research interests, explicit dataset choice and AI-assisted search formulation. The available exploratory conversations give context to that decision.

### A02. Area C selection and n1(+15-minute) forecasting target

#### What the records show

The +15-minute pressure horizon already appears in [Milestone 1](../../reports/Milestone1.pdf). The student then proposed n1/n4/n31, tank T1 and pump flow as a local cohort. Codex provided a sensor comparison and recommended n1; the student selected n1 and requested that setup in the document. This sequence records an engineering-led choice developed through technical collaboration.

#### Student contribution

The student proposed the local sensor cohort, made the final recorded target choice and later explained the tank-fed hydraulic scope: [Student proposal of the Area C cohort](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-021.txt#L3003), [Student adoption of n1(+15)](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-021.txt#L3590) and [Student explanation of the tank-fed sector](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-037.txt#L2601).

#### AI assistance

Codex supplied a sensor comparison, clarified that PUMP_1 fills T1, and recommended n1 using nominal pipe distance and observed pressure characteristics: [Codex comparison and n1 recommendation](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-021.txt#L3333). The current [topology outputs](../../results/topology_audit.json) and [scope explanation](../../docs/research_scope.md) make the later nominal-path calculation auditable.

#### Technical or academic significance

The resulting task is recorded n1 pressure three five-minute readings ahead, using information available at issue time. The tank boundary motivates a manageable local predictor set. n1 is the most distant of the **three measured pressure nodes by the stated nominal pipe-path calculation**; the calculation provides a spatial ranking of those observed nodes.

#### Direct source evidence

[Cohort proposal](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-021.txt#L3003) → [AI recommendation](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-021.txt#L3333) → [Student target selection](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-021.txt#L3590). [Later student explanation of the control-engineering motivation](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-073.txt#L640) refers to the student's practice and earlier paper; it records the student's later account of that engineering connection.

#### What this evidence establishes

The evidence supports the student's cohort proposal and final target choice, with Codex's intervening recommendation clearly attributed. Nominal distances and descriptive relationships provide the documented selection context.

### A03. Selection of the six local signals

#### What the records show

The student focused the feature set by questioning the need for all 82 AMRs and explaining the value of hydraulically related local measurements. His reasoning connected pump inflow, tank storage, remote pressure and target-node water use. The final six signals are documented in [Milestone 2](../../reports/Milestone2.pdf) and the [research scope](../../docs/research_scope.md).

#### Student contribution

The student narrowed the AMR scope and supplied the engineering rationale for retaining local signals: [Student objection to using all 82 AMRs](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-034.txt#L887) and [Student hydraulic explanation of the feature restriction](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-037.txt#L2601).

#### AI assistance

Codex identified available channels, compared sensors, clarified measurement meanings and converted the scope into documented calculations and figures. The [AI explanation of the pump–tank boundary](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-021.txt#L3333) predates the final narrower AMR choice. The [data/nominal-network code](../../src/analysis.py) and [topology audit](../../results/topology_audit.json) support the later technical clarification.

#### Technical or academic significance

| Final signal | Measurement | Engineering rationale for the planned comparison |
|---|---|---|
| n1 | Target-node pressure, m | Recent history of the value to be forecast |
| n4 | Area C pressure, m | A peer measurement that may describe shared operating variation |
| n31 | Area C pressure, m | A second observed pressure at a different nominal tank distance |
| T1 | Tank level, m | Available tank storage/head state |
| PUMP_1 | Pump flow, m³/h | Measured **tank inflow**, potentially informative about later level changes |
| AMR_n1 | Junction consumption, L/h | Water use assigned to the target junction; **target-junction demand** |

The hydraulic rationale gives the selection a clear local scope. PUMP_1 measures tank inflow; tank outlet flow would require a separate measurement or storage-balance estimate. PRV settings describe nominal regulation, while remote pressure behavior depends on the operating conditions. The current technical explanation gives these measurement meanings explicitly.

#### Direct source evidence

[AMR scope and plot instructions](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-034.txt#L887) · [Student explanation of the selected supply boundary](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-037.txt#L2601) · [AI clarification of measured inflow versus tank supply](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-021.txt#L3333) · [Final six-signal specification](../../docs/research_scope.md#target-and-selected-measurements).

#### What this evidence establishes

The contribution is a reasoned local feature selection. The next-stage C3 comparison will quantify the auxiliary set's joint forecast utility against n1 history and the same calendar variables.

### A04. EDA, calculations, and visualizations

#### What the records show

The student's instructions shaped the visual analysis: daily pressure overlays following a supplied example; n1/n4/n31 panels; T1 level and PUMP_1 flow; a correlation matrix; and a readable two-column layout. The resulting daily plots also show a clock-time mean. The source links below connect these requirements to AI-assisted code and execution.

#### Student contribution

The student defined the questions, selected the measurements and requested a practical visual arrangement. His revisions made the profiles and correlations easier to compare across the tank, pump and three pressure sensors.

#### AI assistance

Codex generated plotting code ([recorded daily-profile code change](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-021.txt#L3728)) and executed an audit with numerical outputs and exit code zero ([recorded EDA audit completion](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-045.txt#L3553)). A separate October 27 record shows a later read-only recalculation ([post-feedback recalculation](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-062.txt#L259)). The repository-building continuation separately records [seven-test execution](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03-repository-continuation/part-003.txt#L2934) and [repository validation](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03-repository-continuation/part-004.txt#L6).

#### Technical or academic significance

The [EDA explanation](../../docs/exploratory_analysis.md), [analysis code](../../src/analysis.py), [plotting code](../../src/figures.py), [executed notebook](../../notebooks/milestone2_analysis.ipynb) and [run manifest](../../results/run_manifest.json) now expose how the descriptive values and four figures are obtained. The historical audit reports 78,621 +15-minute pairs and persistence MAE about 0.0518 m; these are descriptive 2018 reference values. The dated source audit and later reproduction give separate, traceable execution records.

#### Direct source evidence

[Student pressure-plot request](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-021.txt#L3590) · [Student additional-plot request](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-022.txt#L887) · [Student arrangement request](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-034.txt#L887) · [AI-generated implementation](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-021.txt#L3728) · [Completed numerical audit](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-045.txt#L3553) · [Later verification](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-062.txt#L259).

#### What this evidence establishes

The student's instructions explain the analysis questions and visual decisions; dated AI code/execution records explain the implementation. The original report, preserved images and later reproductions supply a traceable history of the descriptive work.

### A05. Literature search, classification, and 35 related-work groups

#### What the records show

The student defined a literature classification by primary objective, followed by a separate search for future-pressure steps within those methods. His revisions clarified dataset relevance, counting units and the meaning of the chart. He selected the term “35 groups of related works” and requested an explanation of how those groups were formed.

#### Student contribution

The records show the relevance criteria and critical corrections: [Student objective-based and future-pressure screening request](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-018.txt#L1191), [Student challenge to denominators and unrelated works](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-048.txt#L2692) and [Student choice of the 35-group wording and explanation](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-049.txt#L3532).

#### AI assistance

Codex assisted discovery, extraction, grouping, code inspection and synthesis. The [AI literature synthesis and distinction between prediction tasks](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-013.txt#L736) records the AI-assisted technical synthesis. The [47-source inventory](../../literature/source_records.csv), [35 assignments](../../literature/groups.csv), [screening notes](../../literature/screening_notes.md) and [recounting code](../../src/screening.py) expose the retained classification.

#### Technical or academic significance

The current [recount](../../results/screening_summary.json) contains **47 source records → 35 related-work groups → six detailed selections**. A paper, a related conference/journal version and an associated repository may share a group; percentages use related-work groups as their denominator.

| Primary objective | Groups | Share of 35 | Selected groups |
|---|---:|---:|---:|
| Leak detection / localization | 27 | 77.1% | 3 |
| Current-state estimation | 3 | 8.6% | 1 |
| Pressure/head forecasting | 2 | 5.7% | 1 |
| Anomalies / sensor faults | 2 | 5.7% | 1 |
| Sensor placement | 1 | 2.9% | 0 |

The primary-purpose category can differ from an intermediate computation: ChebNet and SAM-kNN include temporal pressure learning despite diagnostic categories. The notes also record temporal components in other screened groups. [Ahmed et al.](../../literature/ahmed_feedback.md) was added for the feedback response and remains outside the historical 47/35/six denominators.

#### Direct source evidence

[Initial grouping criteria](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-018.txt#L1191) · [Correction of scope/count interpretation](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-048.txt#L2692) · [Accepted group terminology](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-049.txt#L3532) · [AI-assisted technical synthesis](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-013.txt#L736) · [Inventory and grouping limits](../../literature/README.md).

#### What this evidence establishes

The retained inventory supports a focused literature review with reproducible grouping and counts. Six studies receive the closer technical treatment used in the submitted table; the remaining notes document relevance screening.

### A06. Focused examination of the six selected studies

#### What the records show

The student's later account describes AI-assisted discovery, quick relevance screening and closer examination of six selected works. He identified two reading questions: “Data preparation and how the method works” and “Reported results and what they show.” The guide presents this retrospective reading account alongside the recorded Codex source/code inspections and the student's contemporary technical questions.

#### Student contribution

The student's [later explanation of the three-stage workflow and personal closer review](chatgpt/6ae0894a-6f50-83e9-a7ca-d4d3c8c50402/part-001.txt#L1136) records his retrospective account of the closer review. Contemporary questions separately demonstrate critical checking of dataset relevance: [Student question about SAM-kNN and BattLeDIM](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-053.txt#L4020) and [Student question about the AGN study and BattLeDIM](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-054.txt#L73). The student also requested clearer explanation of the two table columns ([Student request to improve the previous-author comparison](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-054.txt#L1214)).

#### AI assistance

Codex extracted and synthesized source material, inspected available code and helped rewrite the comparison. The [recorded inspection of SAM preprocessing, GATRes and Wang source passages](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-041.txt#L629) is an actual completed tool operation. [Paper locators and inspection records](../literature_checks.json) and [pinned-code byte checks](../code_link_checks.json) identify the AI-assisted checks and their dates.

#### Technical or academic significance

The six entries match [Milestone 2's previous-author table](../../reports/Milestone2.pdf#page=3). Their roles are different:

| Selected work | Preparation / how the method works | What its reported results show |
|---|---|---|
| [ChebNet](../../literature/detailed_review/chebnet.md) | Simulated healthy pressures and graph links; next-step predictor plus current reconstructor | Leak-diagnosis outcomes on the authors' evaluation task |
| [SAM-kNN](../../literature/detailed_review/sam_knn.md) | New Area A scenarios; adaptive memories and next-reading virtual pressure | Anomaly/leak alarm counts on the generated scenarios |
| [AGN](../../literature/detailed_review/agn.md) | Modified L-Town simulations; graph, recurrence and attention for future heads | Regional/window forecasting errors for future nodal heads |
| [LILA](../../literature/detailed_review/lila.md) | Released SCADA; same-time pressure/flow reference regression and accumulated deviations | Leak detection/localization using a current healthy-pressure reference |
| [GATRes](../../literature/detailed_review/gatres.md) | Newly simulated snapshots with hidden inputs; graph attention reconstructs current pressure | Same-time hidden-pressure reconstruction accuracy |
| [EILF / Wang et al.](../../literature/detailed_review/eilf.md) | Tank balance, demand references, trend separation and hydraulic diagnosis | Leak-diagnosis performance and prior tank-balance engineering |

Each detailed review links original sources, implementation where found, metrics and limitations. The distinction between released SCADA and newly generated L-Town data is essential to comparability. Published scores retain their original authorship and evaluation context.

#### Direct source evidence

[Student retrospective reading statement](chatgpt/6ae0894a-6f50-83e9-a7ca-d4d3c8c50402/part-001.txt#L1136) · [Completed AI source/code inspection](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-041.txt#L629) · [Student SAM-kNN question](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-053.txt#L4020) · [Student AGN question](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-054.txt#L73) · [Student request for clearer preparation/results explanations](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-054.txt#L1214).

#### What this evidence establishes

The evidence distinguishes the student's retrospective personal reading account, contemporary critical questions and recorded AI inspections. Published model scores remain attributed to their original authors, with implementation availability described in each review.

### A07. Proposed forecasting models and evaluation

#### What the records show

The student kept n1(+15) as the objective, asked for a different forecasting approach and requested complexity consistent with approximately week 7. Codex recommended Gradient Boosting, proposed the persistence/Ridge/Random Forest comparisons and explained preparation/evaluation details. The submitted C1–C3 plan captures the resulting proposed investigation.

#### Student contribution

The student set the retained target and complexity constraint: [Student course-level simplification request](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-049.txt#L3532) and [Student answer retaining n1(+15) while requesting another method](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-050.txt#L1865). The structured reply records the student's answer beside the AI question/recommendation; each is attributed to its speaker.

#### AI assistance

The chronology explicitly records [Codex recommendation of Gradient Boosting](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-050.txt#L1887), [AI proposal of persistence, Ridge and Random Forest comparators](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-050.txt#L2598) and [AI explanation of lagged preparation and chronological evaluation](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-056.txt#L840). These are the recorded AI methodological contributions to the student-directed plan.

#### Technical or academic significance

The controlling specification remains [Milestone 2, Section 3](../../reports/Milestone2.pdf#page=4) and [C1–C3](../../docs/anticipated_contributions.md): prepare past-only forecast rows; compare four methods; compare full-feature boosting with n1-history boosting using the same calendar variables and eligible rows. The plan uses 2018 development and a final chronological 2019 assessment, validation-only setting choices and MAE/RMSE. Ridge scaling is to be fitted on training data only.

#### Direct source evidence

[Student methodological requirement](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-050.txt#L1865) → [AI boosting proposal](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-050.txt#L1887) → [AI comparator proposal](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-050.txt#L2598); [AI preparation/evaluation explanation](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-056.txt#L840) and [submitted evaluation plan](../../docs/anticipated_contributions.md#chronological-evaluation).

#### What this evidence establishes

The result at this milestone is the proposed C1–C3 experiment. Descriptive EDA supplies the completed groundwork; training, model selection and final chronological forecast assessment are the next research stage.

### A08. Research gap and anticipated original contribution

#### What the records show

The student connected the proposed forecast to anticipating pressure responses in control engineering. The literature discussion separated future-pressure learning, current reconstruction and leak diagnosis. AI suggestions helped turn that motivation into a controlled comparison of forecast methods and the joint value of auxiliary measurements.

#### Student contribution

The control/modeling direction is contemporary evidence ([Student engineering interest](chatgpt/6a92eec0-f09c-83e9-a9ed-29d95f24d41b/part-001.txt#L2841)); the later [student account of critical-node control motivation](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-073.txt#L640) provides additional explanation of anticipated practical use. The request to retain n1(+15) while seeking another approach is direct ([Student requirement for the proposed task](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-050.txt#L1865)).

#### AI assistance

Codex contributed the [early auxiliary-sensor research hypothesis](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-003.txt#L704), [distinction between prior prediction tasks](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-013.txt#L736) and [bounded boosting-gap formulation](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-050.txt#L2598). These recommendations are recorded alongside the student's task requirements and control-engineering motivation.

#### Technical or academic significance

The proposed study combines a common **released-SCADA n1(+15) target**, six hydraulically selected measurements and a chronological evaluation. It asks whether established regressors improve on strong references and whether the auxiliary measurements add value beyond n1 history. The [Ahmed comparison](../../literature/ahmed_feedback.md) identifies the prior use of five principal Area C signals and helps locate the extension in the future-pressure task. C3 evaluates the auxiliary set jointly.

#### Direct source evidence

[AI-origin auxiliary-signal hypothesis](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-003.txt#L704) · [Prior-work distinctions](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-013.txt#L736) · [Qualified gap proposal](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-050.txt#L2598) · [Later student engineering explanation](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-073.txt#L640) · [Anticipated contributions and limits](../../docs/anticipated_contributions.md).

#### What this evidence establishes

The anticipated contribution is a controlled application and comparison of established methods within the reviewed literature context. It aims to produce evidence about forecast accuracy and the practical value of the selected signals.

### A09. Writing, technical corrections, and structured prompts

#### What the records show

The student supplied substantive wording, requested English drafting and improved the technical explanations through questions and corrections. AI generated structured research prompts, source-based summaries and report/repository prose. The source sequence identifies supplied content, recommendations and adopted wording.

#### Student contribution

The student supplied a dataset-selection rationale for translation ([Student wording explaining the two dataset candidates](chatgpt/6aac63db-6148-83ea-a1d0-229cd3614df3/part-001.txt#L64)) and questioned the dataset relevance and clarity of previous-work summaries ([SAM-kNN relevance question](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-053.txt#L4020), [AGN relevance question](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-054.txt#L73), [Request for understandable preparation/results columns](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-054.txt#L1214)). These are concrete technical/editorial interventions.

#### AI assistance

The [AI-generated structured search prompt](chatgpt/6a92eec0-f09c-83e9-a9ed-29d95f24d41b/part-001.txt#L2848) is visible model-written material. Codex's [recorded technical source inspection](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-041.txt#L629) supports source-based revisions, while the [later repository-document revision execution](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03-repository-continuation/part-003.txt#L1647) separately records AI-assisted rewriting after feedback.

#### Technical or academic significance

Readable explanations help distinguish what each author prepared, how a model operates and what its evaluation measures. The supplied wording is credited to the student, and AI drafting/translation/organization is disclosed. The original submitted PDFs remain unchanged; the appendix supplies the linked account of their preparation and attribution.

#### Direct source evidence

[Student-supplied rationale](chatgpt/6aac63db-6148-83ea-a1d0-229cd3614df3/part-001.txt#L64) · [AI prompt formulation](chatgpt/6a92eec0-f09c-83e9-a9ed-29d95f24d41b/part-001.txt#L2848) · [Student table-revision request](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-054.txt#L1214) · [AI source-check execution](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03/part-041.txt#L629).

#### What this evidence establishes

Attribution follows the recorded wording, requests, recommendations and technical checks. The original languages and dated messages preserve how the technical content and its presentation developed.

### A10. Scope control, feedback response, and AI interaction recovery

#### What the records show

The student kept the repository aligned with the submitted milestone and course level, requested the retained literature inventory and six focused reviews, and initiated the review and recovery of AI interactions. Later exchanges document his request for a feedback-response repository, his questions about conversation evidence and his authorization of minimally redacted public transcripts.

#### Student contribution

The student supplied scope constraints ([Student objection to unexplained experiments and request for the full inventory](chatgpt/6ae334d1-a604-83e9-a039-dd29a3c1856b/part-001.txt#L64)), requested [review of possible university-rule risks](chatgpt/6ae334d1-a604-83e9-a039-dd29a3c1856b/part-001.txt#L86), and asked for [separate ChatGPT and Codex recovery prompts](chatgpt/6ae334d1-a604-83e9-a039-dd29a3c1856b/part-001.txt#L108). The later [repository-building request](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03-repository-continuation/part-003.txt#L544) explicitly uses the transcript-based student/AI division as the basis for the supplement.

#### AI assistance

AI organized scope corrections, recovered available records, created evidence mappings, implemented reproducibility checks and prepared public derivatives. Available completed operations include [repository assembly](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03-repository-continuation/part-003.txt#L1384), [test execution](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03-repository-continuation/part-003.txt#L2934) and [original-versus-public transcript validation](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03-repository-continuation/part-007.txt#L1266). These dated operations document the AI-assisted construction of the feedback supplement.

#### Technical or academic significance

The repository responds with claims linked to data/code/results, an auditable inventory, accurate role descriptions and available conversations. The student then asked whether summaries alone supplied the required conversation evidence and explicitly authorized public derivatives. The separate five-row construction table below traces the later feedback-response stage.

#### Direct source evidence

[Scope correction](chatgpt/6ae334d1-a604-83e9-a039-dd29a3c1856b/part-001.txt#L64) · [Recovery request](chatgpt/6ae334d1-a604-83e9-a039-dd29a3c1856b/part-001.txt#L108) · [Question about missing actual transcripts](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03-repository-continuation/part-005.txt#L2188) · [Authorization for minimally redacted public conversations](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03-repository-continuation/part-006.txt#L827) · [Request to include the repository-building dialogue and its attribution](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03-repository-continuation/part-007.txt#L2901).

#### What this evidence establishes

The evidence establishes student direction of scope, feedback response and public disclosure, together with AI-assisted recovery, implementation and validation. Collection coverage is documented in Section 6.

### Repository construction after the feedback: R01–R05

These activities document the student-directed **feedback supplement and its evidence**. They are also available as [structured attribution rows](repository_construction_contributions.csv).

| Activity | Student contribution | AI assistance and recorded evidence |
|---|---|---|
| R01 · Purpose and attribution | [Requested the feedback repository using the transcript-based allocation of roles](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03-repository-continuation/part-003.txt#L544) | [AI planned the package](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03-repository-continuation/part-003.txt#L1348) and [assembled it from retained artifacts and revised documentation](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03-repository-continuation/part-003.txt#L1384) |
| R02 · Reproducibility | Set an accessible, evidence-based response as the goal | [AI-executed seven-test completion](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03-repository-continuation/part-003.txt#L2934) and [repository validation](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03-repository-continuation/part-004.txt#L6); [code/notebook trail](../../docs/reproducibility.md) |
| R03 · Disclosure and privacy | [Asked whether actual transcripts were included](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03-repository-continuation/part-005.txt#L2188) and [questioned keeping them private](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03-repository-continuation/part-006.txt#L189) | [AI explained the initial contribution summary](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03-repository-continuation/part-006.txt#L73) and [explained the privacy/publication distinction](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03-repository-continuation/part-006.txt#L705) |
| R04 · Public transcript evidence | [Authorized minimal, documented public redactions](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03-repository-continuation/part-006.txt#L827) | [AI compared derivatives with originals](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03-repository-continuation/part-007.txt#L1266), [checked the published commit](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03-repository-continuation/part-007.txt#L1957) and [checked the successful public workflow](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03-repository-continuation/part-007.txt#L2727) |
| R05 · Construction record and guide | [Requested these construction exchanges and the student/AI attributions](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03-repository-continuation/part-007.txt#L2901); [supplied guide specification](repository_construction_request.json) | [AI began the bounded recovery and guide update](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03-repository-continuation/part-007.txt#L2927); the current manifest and guide document the later completed artifacts; the capture has the cutoff stated in Section 6 |

The student extended the supplement from a contribution summary to public conversation evidence through explicit questions and authorization. AI prepared the redacted derivatives, code and validation under that direction. The [supplied structured request](repository_construction_request.json) preserves the instructions for the expanded guide, with its fingerprint in the manifest. The manifest identifies it as a student-supplied instruction artifact, and the associated chat records its use for this guide.

## 4. Milestone 2 academic scope and anticipated contribution

The student's central contribution is a feasible engineering question developed into a controlled predictive-learning proposal. [Milestone 2, Section 3](../../reports/Milestone2.pdf#page=4) and [C1–C3](../../docs/anticipated_contributions.md) define the next stage: prepare past-only forecast rows; compare Gradient Boosting, persistence, Ridge and Random Forest; and quantify auxiliary-signal value against n1 history with the same calendar variables and evaluation rows.

The completed groundwork comprises descriptive EDA, nominal-network checks, the literature inventory and four figures. These outputs make the proposal concrete and reproducible. The [work-status record](../work_status.json) identifies completed analysis, author-reported literature results and proposed model experiments.

The review distinguishes leak diagnosis, current reconstruction and future forecasting, giving the student's selected task a clear reference context. The [Ahmed comparison](../../literature/ahmed_feedback.md) connects the shared Area C measurements to earlier reconstruction-based leak detection. The proposed contribution is the task-specific preparation, fair comparison and understanding of auxiliary-signal utility within this focused review. Both a useful gain and support for a simpler predictor would inform the engineering question.

## 5. Student contributions and AI assistance

The [contribution statement](../../docs/student_contributions.md), [A01–A10 summary](../contribution_summary.csv) and direct links above document complementary roles:

- **Student research leadership:** control-engineering motivation; explicit dataset choice; local cohort proposal; final n1 selection; hydraulic rationale; AMR restriction; questions and visual requirements; literature-relevance criteria; technical corrections; course-level scope; feedback response and public-disclosure decisions.
- **AI methodological and technical support:** candidate/formulation comparisons; the concrete n1 recommendation; Gradient Boosting/comparator and preparation/evaluation recommendations; source/code inspection; generated and executed code; drafting; organization; validation and synchronization.
- **Student retrospective account:** the student's explanation of personally reviewing the six papers gives his account of that activity; dated AI inspections supply the separate tool-level record.

The chronological sources show the student's choices developing with technical support, including recommendations followed by adoption and refinement. They preserve the engineering ideas, questions, decisions and implementation roles that produced the project and its repository.

## 6. Collection coverage and privacy

**ChatGPT coverage:** eleven recovered conversations contain 82 message items. The index identifies fifteen assistant references whose readable bodies await recovery. Five longer retrieval items have separately labeled browser-rendered supplements. This partial recovery preserves the available dialogue and its acquisition form; a fuller account export could extend the collection.

**Codex coverage:** two historical research sessions and one recovery/support session were initially preserved. T16 continues T02 from raw record **11414**, immediately after its earlier **11413** records; the old raw-prefix fingerprint matched during capture. T16 ends at record **12601**, on **2026-10-29 at 18:38:33.583 UTC**. The capture therefore supplies the previously absent repository-building exchanges with a precise start, end and continuity record. Later guide artifacts and Git commits identify work completed after that cutoff.

The original Codex audit recorded **231 tool-output truncation notices**, including repeated representations. This is a historical output-coverage counter. Separately, the current public derivatives contain **231 registered redaction spans**: 200 in T01–T15 and 31 in T16. The two counts describe different things. The database supplement preserves a reasoning-record identifier and source notice. The public dialogue covers student messages, visible AI replies and tool events; the raw archives retain additional technical metadata privately.

Role interpretation is explicit: [the application open-page record](codex/01a12b61-e72c-7da1-bb50-45bff9d85d03-repository-continuation/part-001.txt#L901) is classified as application context. The contribution map uses the student's actual instructions and answers, with duplicate representations and embedded AI questions identified through the source sequence.

**Privacy treatment:** the [register](redactions.csv) documents five password values, fifteen literal password fragments in earlier checks/quoted output, 82 access-token/signature/temporary access-key values, 31 restricted class-recording/meeting links and 98 inline image payloads. These are occurrences, including repetitions. Image payload markers preserve surrounding tool text and locators. Public files retain academic passages, original languages, corrections, feedback and source references. Untouched originals support authorized private comparison.

The [current plaintext request](repository_construction_request.json) is a separately supplied attachment with its own fingerprint. Historical attachment references remain identified by their recorded locators. Binary attachments, raw databases and unredacted session archives are retained privately.

This organized evidence supports the instructor's review of provenance and LLM collaboration within the documented collection coverage. Source fingerprints establish copy integrity and registered text preservation; the contribution links identify the recorded decisions, recommendations and executions.

## 7. Verification and reproducibility

From the repository root, with Python 3.12 or newer:

```bash
python scripts/validate_ai_interactions.py
python scripts/validate_repository.py
```

An authorized holder of the recovered archives can also run `python scripts/validate_ai_interactions.py --originals /private/path/to/archives`. It reads originals locally, checks their fingerprints, reconstructs public text using exactly the registered half-open Unicode-character spans and verifies T16's raw snapshot/prefix. The manifest identifies the separate private archive used for T16.

Public validation checks ordered part ranges/hashes, redaction markers/locators, contribution links and selected credential/image patterns. [verification.json](verification.json) retains the initial collection's results and the added continuation checks. The privacy scan has the pattern scope stated by the validator, and the coverage section identifies available and pending recovery material.

The [guide validation record](guide_validation.json) records the executed source comparison and link/anchor checks, with the guide fingerprint and validation time. [Scientific reproduction instructions](../../docs/reproducibility.md) and the [executed notebook](../../notebooks/milestone2_analysis.ipynb) separately document source data, calculations, four figures and numerical comparisons. Together these artifacts make the completed groundwork and the proposed next stage easy to review.
