# Screening notes for all 35 groups

These notes organize the retained screening decisions using source records and evidence locators. All 35 groups have relevance notes, and six linked reviews provide the closer technical treatment used in the submitted comparison. The notes identify the screened tasks, methods, author-reported results and available horizon details.

Each category records the primary purpose. Intermediate future-pressure components are described alongside each work's primary objective. Group labels below are rendered in English; source identifiers, membership, links, checksum/commit fields and publication identities are retained. Complete metadata where recovered is in [bibliography.json](bibliography.json).

## LILA / Leakbusters
<!-- group: lila -->

**Primary task / category:** Current healthy-pressure reference and leak identification/localization (`leak`).
**Method screened:** Linear relationships among pressures and flow, cumulative residual detection and hydraulic localization.
**Relevance to n1(+15):** A same-time pressure-reference comparator; the detailed review describes its regression and flow transformation.

**Sources:** [pdf-5](https://doi.org/10.1061/(ASCE)WR.1943-5452.0001535); [pdf-6](https://doi.org/10.5281/zenodo.3924632); [repo-52](https://github.com/jorgeps86/LeakLocalization/tree/1c9493847bf37d609ae89310443bc61ee42206f8); [repo-55](https://github.com/SWN-group-at-TU-Berlin/LILA/tree/b488a60db1974b6f5b7887ce1cf5d31dff3dad68).

**Evidence locators retained:** P02 PDF p.4, Eqs.12-13: pressure from other pressures and squared flow in the same condition; current residual.

**Review coverage:** [Detailed technical review](detailed_review/lila.md). Published performance is attributed to the original authors.

## Under Pressure · dual model
<!-- group: under-pressure -->

**Primary task / category:** Leak detection and localization (`leak`).
**Method screened:** A dual hydraulic model uses measured pressure heads as fixed-head virtual-reservoir boundaries.
**Relevance to n1(+15):** Provides a pressure-based diagnosis approach for comparison with the proposed forecasting task.

**Sources:** [pdf-7](https://doi.org/10.1061/(ASCE)WR.1943-5452.0001515); [pdf-8](https://doi.org/10.5281/zenodo.3923907).

**Evidence locators retained:** P03 PDF pp.5-6: measured pressure heads become fixed-head virtual reservoir boundaries of the dual model.

**Review coverage:** Focused screening of the primary task, method and relevance to the proposed forecast.

## CIACUA
<!-- group: ciacua -->

**Primary task / category:** Leak detection and localization (`leak`).
**Method screened:** Genetic optimization adjusts emitter parameters; a pressure RMSE compares simulation with SCADA.
**Relevance to n1(+15):** The reported RMSE measures agreement between a hydraulic simulation and observed SCADA.

**Sources:** [pdf-9](https://doi.org/10.5281/zenodo.3923227).

**Evidence locators retained:** P04a PDF pp.2-4: genetic optimization of emitter parameters using simulated-vs-SCADA pressure RMSE.

**Review coverage:** Focused screening of the primary task, method and relevance to the proposed forecast.

## DHI Singapore
<!-- group: dhi-sg -->

**Primary task / category:** Pipe leakage classification (`leak`).
**Method screened:** A feedforward classifier maps 33 pressure inputs to 905 possible pipe-leak classes.
**Relevance to n1(+15):** Uses pressure inputs to classify the leaking pipe.

**Sources:** [pdf-10](https://doi.org/10.5281/zenodo.3902945).

**Evidence locators retained:** P06a PDF pp.3-4: 33 pressure inputs, 905 pipe leakage-class outputs; feedforward classifier.

**Review coverage:** Focused screening of the primary task, method and relevance to the proposed forecast.

## Wu_BSY
<!-- group: wu-bsy -->

**Primary task / category:** Leak diagnosis (`leak`).
**Method screened:** STL decomposition and statistical process control; pump flow and level change estimate tank outlet flow.
**Relevance to n1(+15):** Provides prior tank-balance engineering for interpreting the sector's measured inflow and storage.

**Sources:** [pdf-11](https://doi.org/10.5281/zenodo.3908525).

**Evidence locators retained:** P07a PDF pp.1-3: STL/SPC diagnosis; p.3 Eq.3 already derives tank outlet flow from pump flow and level change.

**Review coverage:** Focused screening of the primary task, method and relevance to the proposed forecast.

## Tsinghua · conference VAR / journal EILF
<!-- group: tsinghua -->

**Primary task / category:** Multistage leakage detection and isolation (`leak`).
**Method screened:** The conference report mentions VAR; its numerical lead remains unspecified. The journal EILF uses STL trends, tank balance, multiscale differences and hydraulic localization.
**Relevance to n1(+15):** Provides engineering context, with conference and journal methods documented separately.

**Sources:** [pdf-12](https://doi.org/10.5281/zenodo.3924109); [pdf-asce-2022](https://doi.org/10.1061/(ASCE)WR.1943-5452.0001558).

**Evidence locators retained:** P08a conference PDF pp.2-3, Sec.1.2: VAR normal pressure, no numerical lag/order/lead or exogenous timestamps. Journal 2022 PDF p.3 Eq.3: STL pressure decomposition; pp.7,9-10: 30-min tank balance and weekly-difference hydraulic localization. Journal p.11: code by request.

**Review coverage:** [Detailed technical review](detailed_review/eilf.md). Published performance is attributed to the original authors.

## DandW
<!-- group: dandw -->

**Primary task / category:** Leak detection and localization (`leak`).
**Method screened:** Calibrated same-condition pressure residuals and vector-angle localization.
**Relevance to n1(+15):** Current hydraulic mismatch differs from forecasting a later recorded pressure.

**Sources:** [pdf-13](https://doi.org/10.5281/zenodo.3925507).

**Evidence locators retained:** P09a PDF pp.2-3, Eq.3: same-condition calibrated pressure residual and vector-angle localization.

**Review coverage:** Focused screening of the primary task, method and relevance to the proposed forecast.

## Garðarsson · ChebNet
<!-- group: chebnet -->

**Primary task / category:** Leak detection/localization with an intermediate future-pressure model (`leak`).
**Method screened:** Chebyshev graph networks forecast the next pressure record and reconstruct current pressure; discrepancies support diagnosis.
**Relevance to n1(+15):** A true future-pressure component (+5 minutes) makes this a core temporal comparator, although the final objective is leakage.

**Sources:** [pdf-14](https://doi.org/10.1016/j.ifacol.2022.07.203); [repo-51](https://github.com/GardarGardarsson/GSP_for_Leak_Detection/tree/864a99041af6331375946a8fad3a71c633108eb8).

**Evidence locators retained:** P10 PDF pp.3-5; pinned data_loader.py:285-290: X ends at i-1, y[i]; five-minute sampling.

**Review coverage:** [Detailed technical review](detailed_review/chebnet.md). Published performance is attributed to the original authors.

## Liquor-HGNN
<!-- group: liquor -->

**Primary task / category:** Leaking-edge identification (`leak`).
**Method screened:** A hydraulic graph neural network assigns leakage labels to snapshot edges; NeuralProphet supplies demands.
**Relevance to n1(+15):** Demand completion supports the per-snapshot leaking-edge classification task.

**Sources:** [pdf-15](https://ceur-ws.org/Vol-3630/LWDA2023-paper40.pdf); [repo-54](https://github.com/MilanShao/Liquor-HGNN/tree/64ff247902e702d89400eac74f06aac45d2ea292).

**Evidence locators retained:** P11 PDF pp.3,5,7-9: per-snapshot leaking-edge labels; NeuralProphet fills demands, not future pressures.

**Review coverage:** Focused screening of the primary task, method and relevance to the proposed forecast.

## GSI + dictionary learning
<!-- group: gsi-dl -->

**Primary task / category:** Leak localization (`leak`).
**Method screened:** Graph signal interpolation estimates current heads; dictionary learning classifies leak location.
**Relevance to n1(+15):** Combines current-pressure reconstruction with leakage classification.

**Sources:** [pdf-16](https://doi.org/10.48550/arXiv.2110.06372); [pdf-17](https://doi.org/10.1109/CCTA49430.2022.9966160).

**Evidence locators retained:** P12 PDF pp.1-3: GSI interpolates current heads; dictionary classifier identifies leakage location.

**Review coverage:** Focused screening of the primary task, method and relevance to the proposed forecast.

## GAN + SSIM
<!-- group: gan -->

**Primary task / category:** Leak diagnosis (`leak`).
**Method screened:** Paired demand/pressure images from one timestamp support a pix2pix generative network and structural similarity comparison.
**Relevance to n1(+15):** Generating a pressure state from same-time conditions differs from temporal forecasting.

**Sources:** [pdf-18](https://doi.org/10.1016/j.watres.2023.120012).

**Evidence locators retained:** P13 manuscript PDF p.10, Secs.3.2-3.3: demand-pressure image pairs from one time step; pp.11-12: pix2pix/SSIM.

**Review coverage:** Focused screening of the primary task, method and relevance to the proposed forecast.

## GATRes
<!-- group: gatres -->

**Primary task / category:** Current pressure-state reconstruction (`state`).
**Method screened:** Graph attention with residual connections reconstructs pressure hidden by a same-snapshot input mask.
**Relevance to n1(+15):** Provides a graph-based current-pressure estimation comparator, with MAE evaluated on hidden readings.

**Sources:** [pdf-20](https://doi.org/10.1029/2023WR036741); [repo-50](https://github.com/DiTEC-project/gnn-pressure-estimation/tree/bb287ed2ae091b29fa19f2417406756b57a45a1f).

**Evidence locators retained:** P15 PDF pp.19-21, Tables10-11; pinned train.py:174-178,257-261: mask input, label same snapshot.

**Review coverage:** [Detailed technical review](detailed_review/gatres.md). Published performance is attributed to the original authors.

## Iterative mobile sensor
<!-- group: mobile -->

**Primary task / category:** Sensor placement for leak localization (`sensors`).
**Method screened:** Iterative relocation of a mobile pressure sensor improves spatial information for leak localization.
**Relevance to n1(+15):** Sensor selection contributes an observability perspective on the choice of available measurements.

**Sources:** [pdf-22](https://doi.org/10.48550/arXiv.2406.19900).

**Evidence locators retained:** P17 PDF pp.3-6: iterative relocation of mobile pressure sensor for leak localization.

**Review coverage:** Focused screening of the primary task, method and relevance to the proposed forecast.

## D-UKF-AW-GSI
<!-- group: dual-ukf -->

**Primary task / category:** Current network-state estimation (`state`).
**Method screened:** Dual unscented Kalman filtering with adaptive-weighted graph signal interpolation; head observations stay fixed across estimator iterations.
**Relevance to n1(+15):** The index identifies estimator iterations for a fixed set of head measurements.

**Sources:** [pdf-23](https://doi.org/10.48550/arXiv.2412.11687).

**Evidence locators retained:** P18 PDF pp.4,7: head measurement vector remains constant throughout estimator iterations; k is not physical lead.

**Review coverage:** Focused screening of the primary task, method and relevance to the proposed forecast.

## Topological signal processing
<!-- group: topological -->

**Primary task / category:** Leak/anomaly detection (`leak`).
**Method screened:** Topological signal processing analyzes dynamic edge-flow signals.
**Relevance to n1(+15):** The screened x[k+1] represents the edge-flow signal used for anomaly detection.

**Sources:** [pdf-24](https://www.eurasip.org/Proceedings/Eusipco/Eusipco2025/pdfs/0002407.pdf).

**Evidence locators retained:** P19 PDF pp.2-3: x[k+1] is an edge-flow signal, not a pressure label; dynamic flow anomaly detection.

**Review coverage:** Focused screening of the primary task, method and relevance to the proposed forecast.

## Li–Chen · interpretable ensemble
<!-- group: li-chen -->

**Primary task / category:** Leakage-region classification (`leak`).
**Method screened:** Interpretable stacking/voting ensemble classifiers take pressure measurements as inputs.
**Relevance to n1(+15):** Established boosting/classification use limits any claim that simply using boosting on L-Town is novel.

**Sources:** [pdf-25](https://doi.org/10.3390/w18172220).

**Evidence locators retained:** P20 PDF pp.1,8-9: stacking/voting classifiers of leakage regions; pressure measurements are inputs.

**Review coverage:** Focused screening of the primary task, method and relevance to the proposed forecast.

## Zhang–Fink · AIGNN
<!-- group: aignn -->

**Primary task / category:** Leak diagnosis with temporal pressure prediction (`leak`).
**Method screened:** An attention-based graph method maps past observations to the next five-minute pressure record before diagnosis.
**Relevance to n1(+15):** Contains a future-pressure component documented by brief screening. Its preprint and journal metrics retain their separate source contexts.

**Sources:** [pdf-28](https://doi.org/10.48550/arXiv.2408.02797); [html-aignn-2026](https://doi.org/10.1016/j.ress.2025.111494).

**Evidence locators retained:** P22 preprint PDF pp.15-19: x(t-T)...x(t-1) -> y(t), five-minute sampling; Table3 relative errors in percent. Published-version metrics not substituted. Published full HTML (2026): Secs.4.1/4.1.2 retain previous t-T...t-1 -> t; Sec.5.1 sampling5min; Table3 retains relative means and adds an MAE column without a printed physical unit. No repository link among article links; data statement only says open-source data.

**Review coverage:** Focused screening of the primary task, method and relevance to the proposed forecast.

## AE / VAE / LSTM-AE
<!-- group: autoencoders -->

**Primary task / category:** Leak/anomaly diagnosis (`leak`).
**Method screened:** AE, VAE and LSTM-AE encode/decode 144-sample (12-hour) sequences using same-sequence reconstruction loss.
**Relevance to n1(+15):** Reconstruction error measures agreement with the observed window used for anomaly detection.

**Sources:** [pdf-31](https://doi.org/10.2166/ws.2024.174).

**Evidence locators retained:** P25 PDF pp.5-7: decoder reconstructs x; MSE same-sequence loss, 144-sample (12-hour) input.

**Review coverage:** Focused screening of the primary task, method and relevance to the proposed forecast.

## SAM-kNN
<!-- group: sam -->

**Primary task / category:** Operational anomaly and sensor-fault detection (`anomaly`).
**Method screened:** Adaptive nearest-neighbor regression builds virtual sensors from peer pressure history and tracks prediction discrepancies.
**Relevance to n1(+15):** Its code establishes a next-record pressure target; see the paper/code window discrepancy in the detailed review.

**Sources:** [pdf-32](https://doi.org/10.1007/978-3-031-15934-3_62); [repo-48](https://github.com/andreArtelt/SAM-kNN-Regressor_OnlineLearning_WDNs/tree/9116ec99bf9f053e35401fe3e388062e8b979c54).

**Evidence locators retained:** P26 PDF pp.8-10; pinned LeakDbScenarioPreprocessing.py:19,24,27: mean first three rows, fourth-row pressure label; five-minute sampling.

**Review coverage:** [Detailed technical review](detailed_review/sam_knn.md). Published performance is attributed to the original authors.

## UNIFE
<!-- group: unife -->

**Primary task / category:** Leak detection and localization (`leak`).
**Method screened:** Hydraulic calibration and an enumerative leakage search compare simulated and observed SCADA.
**Relevance to n1(+15):** Uses simulation matching for leakage diagnosis.

**Sources:** [pdf-35](https://doi.org/10.5281/zenodo.3900989).

**Evidence locators retained:** Z3900989 PDF pp.1-3,6: hydraulic calibration and enumerative leakage search against measured SCADA.

**Review coverage:** Focused screening of the primary task, method and relevance to the proposed forecast.

## Artesia · ExtraTrees
<!-- group: artesia -->

**Primary task / category:** Leak diagnosis using pressure estimates (`leak`).
**Method screened:** ExtraTrees relates daily aggregates to mean night pressure, with 1,000 trees and ten contiguous-day folds.
**Relevance to n1(+15):** Estimates mean night pressure from daily aggregates; prospective issue-time and lead details remain unspecified in the screened report.

**Sources:** [pdf-36](https://doi.org/10.5281/zenodo.3906668).

**Evidence locators retained:** Z3906668 PDF pp.1-2: daily aggregates to mean night pressure with ExtraTrees1000 and ten contiguous-day folds. No issue time, prospective label shift or physical lead specified.

**Review coverage:** Focused screening of the primary task, method and relevance to the proposed forecast.

## Cubalytics
<!-- group: cubalytics -->

**Primary task / category:** Leak detection/localization (`leak`).
**Method screened:** Timestamp-joined scaled anomalies, interquartile-range/checksum matrices and pressure-dependent leakage signatures.
**Relevance to n1(+15):** Diagnoses deviations at observed times and supplies a same-time monitoring comparator.

**Sources:** [pdf-37](https://doi.org/10.5281/zenodo.3906850).

**Evidence locators retained:** Z3906850 PDF pp.2-3: timestamp-joined scaled anomalies, IQR/checksum matrix and PDD leakage signatures.

**Review coverage:** Focused screening of the primary task, method and relevance to the proposed forecast.

## Tongji
<!-- group: tongji -->

**Primary task / category:** Multiple-leak localization (`leak`).
**Method screened:** STL and K-means support detection; hydraulic pressure residuals support localization. Temporal prediction in the screened description concerns flow.
**Relevance to n1(+15):** The flow-prediction component supports the paper's leakage-diagnosis objective.

**Sources:** [pdf-38](https://doi.org/10.5281/zenodo.3911045).

**Evidence locators retained:** Z3911045 PDF pp.2-3: STL/Kmeans and same-time hydraulic pressure residual; temporal prediction concerns flow.

**Review coverage:** Focused screening of the primary task, method and relevance to the proposed forecast.

## DHI China
<!-- group: dhi-china -->

**Primary task / category:** Leakage-area classification and localization (`leak`).
**Method screened:** LSTM/LightGBM classify leakage areas using one-hour pressure deficits; genetic optimization then localizes leaks hydraulically.
**Relevance to n1(+15):** The learning output identifies a leakage region from measured inputs.

**Sources:** [pdf-39](https://doi.org/10.5281/zenodo.3911523).

**Evidence locators retained:** Z3911523 PDF p.3: LSTM/LightGBM output leakage-area class from one-hour pressure deficits; GA hydraulic localization.

**Review coverage:** Focused screening of the primary task, method and relevance to the proposed forecast.

## InfraSense
<!-- group: infrasense -->

**Primary task / category:** Leak hotspot localization (`leak`).
**Method screened:** Regularized inverse estimation uses thirteen readings in a one-hour window, updated every thirty minutes.
**Relevance to n1(+15):** The rolling window supports inverse leakage diagnosis.

**Sources:** [pdf-40](https://doi.org/10.5281/zenodo.3921800).

**Evidence locators retained:** Z3921800 PDF p.2: regularized inverse leak localization each 30min from 13 readings/one-hour window.

**Review coverage:** Focused screening of the primary task, method and relevance to the proposed forecast.

## KU hydrosystem
<!-- group: ku -->

**Primary task / category:** Leak detection and localization (`leak`).
**Method screened:** K-means and Western Electric rules identify abnormal periods; leakage sensitivities support spatial comparison.
**Relevance to n1(+15):** Statistical detection and sensitivity matching differ from future-pressure regression.

**Sources:** [pdf-41](https://doi.org/10.5281/zenodo.3922019).

**Evidence locators retained:** Z3922019 PDF pp.1-2: Kmeans and Western Electric rules for normal/abnormal periods; leakage sensitivity comparison.

**Review coverage:** Focused screening of the primary task, method and relevance to the proposed forecast.

## IRI
<!-- group: iri -->

**Primary task / category:** Leak localization (`leak`).
**Method screened:** Current-head graph signal interpolation is used in Area A; hydraulic models support Areas B and C.
**Relevance to n1(+15):** Current-state interpolation supplies an intermediate input to leakage diagnosis.

**Sources:** [pdf-42](https://doi.org/10.5281/zenodo.3923501).

**Evidence locators retained:** Z3923501 PDF p.2: current full-head GSI interpolation in Area A; hydraulic models in B/C.

**Review coverage:** Focused screening of the primary task, method and relevance to the proposed forecast.

## Zhiyun
<!-- group: zhiyun -->

**Primary task / category:** Burst localization (`leak`).
**Method screened:** Demand calibration and Pearson/Jaccard/Euclidean similarity compare measured and hydraulic leak signatures.
**Relevance to n1(+15):** A signature-matching location estimate differs from predicting a future recorded pressure.

**Sources:** [pdf-43](https://doi.org/10.5281/zenodo.3923929).

**Evidence locators retained:** Z3923929 PDF pp.1-2: demand calibration and Pearson/Jaccard/Euclidean matching of hydraulic leak signatures.

**Review coverage:** Focused screening of the primary task, method and relevance to the proposed forecast.

## Cheng00
<!-- group: cheng -->

**Primary task / category:** Leak event detection and isolation (`leak`).
**Method screened:** An ensemble of six multivariate change-point detectors identifies event times.
**Relevance to n1(+15):** The output identifies change points in observed behavior.

**Sources:** [pdf-44](https://doi.org/10.5281/zenodo.3964167).

**Evidence locators retained:** Z3964167 PDF pp.1-2: ensemble of six change-point detectors; outputs event times.

**Review coverage:** Focused screening of the primary task, method and relevance to the proposed forecast.

## FluIng
<!-- group: fluing -->

**Primary task / category:** Leak diagnosis (`leak`).
**Method screened:** Independent component analysis and particle-swarm hydraulic calibration compare pressure, flow and level at the same timestamp.
**Relevance to n1(+15):** The screened objective measures same-time hydraulic agreement.

**Sources:** [pdf-45](https://doi.org/10.5281/zenodo.4011894).

**Evidence locators retained:** Z4011894 PDF pp.1-2: ICA and PSO hydraulic calibration; loss compares pressure/flow/level at same t.

**Review coverage:** Focused screening of the primary task, method and relevance to the proposed forecast.

## SICAMS / SIAM
<!-- group: sicams -->

**Primary task / category:** Anomaly/sensor-fault diagnosis (`anomaly`).
**Method screened:** Mahalanobis whitening, classification and loss estimation identify current anomalies and leak counts.
**Relevance to n1(+15):** The output measures anomaly/count behavior, with the source and pinned SIAM code retained for tracing.

**Sources:** [pdf-46](https://doi.org/10.1016/j.eswa.2026.131450); [repo-siam](https://github.com/dorofeev2025/SIAM/tree/7e8970700212229ea6e715274790e6dc9536c03d).

**Evidence locators retained:** P30 PDF pp.5-8, Eqs.1-3 and Algorithm1: current anomaly/leak count, Mahalanobis whitening, classification and loss estimation.

**Review coverage:** Focused screening of the primary task, method and relevance to the proposed forecast.

## AGN · future nodal-head forecasting
<!-- group: agn -->

**Primary task / category:** Future nodal-head forecasting (`forecast`).
**Method screened:** Attention-augmented gated graph learning forecasts multistep states on modified L-Town.
**Relevance to n1(+15):** A core temporal comparator, evaluated through regional/window future-head errors.

**Sources:** [editorial-agn](https://doi.org/10.1016/j.rineng.2025.106911).

**Evidence locators retained:** Publisher full HTML read 2026-10-15: Sec.2.2 Eq.10 future nodal heads; Sec.3.1 five-minute sampling; Sec.3.2 output length equals history; Table1 windows12/24/48/96 => terminal leads60/120/240/480min.

**Review coverage:** [Detailed technical review](detailed_review/agn.md). Published performance is attributed to the original authors.

## GASTL · spatial transfer
<!-- group: gastl -->

**Primary task / category:** Current-state estimation under monitoring limits (`state`).
**Method screened:** Heterogeneous graph learning, learnable shifts and graph regularization transfer pressure estimation between networks using independent snapshots.
**Relevance to n1(+15):** The source explicitly distinguishes its independent snapshots from temporally correlated data.

**Sources:** [editorial-gastl](https://doi.org/10.1016/j.watres.2025.124475).

**Evidence locators retained:** Publisher full HTML Sec.3.2: pressures and pump/valve flows from SAME snapshot, single-step EPANET, 10000 snapshots (6000/2000/2000). Sec.5.3 explicitly says independent snapshots lack temporal correlation.

**Review coverage:** Focused screening of the primary task, method and relevance to the proposed forecast.

## CN119129798A · pressure Transformer
<!-- group: pressure-patent -->

**Primary task / category:** Future pressures at unmeasured nodes (`forecast`).
**Method screened:** A Transformer-based patent describes future pressure outputs, including an output step of twelve.
**Relevance to n1(+15):** The patent describes future-pressure outputs and an illustrative upload interval; the experimental physical horizon remains unspecified.

**Sources:** [pdf-patent](https://patents.google.com/patent/CN119129798A/zh).

**Evidence locators retained:** CN119129798A original Chinese PDF p.11 para0093 future pressure; p.12 paras0110-0112 future non-sensor pressures; p.17 Fig.4 output step12. Para0106 gives a hypothetical15min upload example but a48-element day-index one-hot vector; this does not establish the experimental sampling interval.

**Review coverage:** Focused screening of the primary task, method and relevance to the proposed forecast.

## AquaSentinel · Ridge and diagnosis
<!-- group: aquasentinel -->

**Primary task / category:** Leak diagnosis using a pressure reference (`leak`).
**Method screened:** Pinned Ridge residual code maps same-hour inflow, inflow squared, T1 and calendar inputs to same-hour pressure, with a 21-day reference and two-day training gap.
**Relevance to n1(+15):** Provides prior Ridge pressure estimation using same-hour inputs and labels.

**Sources:** [repo-aquasentinel](https://github.com/karytalks1/aquasentinel/tree/b9212d8071aa99ba798136ee675ee83fee3a1cf3).

**Evidence locators retained:** Pinned b9212d8071aa99ba798136ee675ee83fee3a1cf3 src/residuals.py:_design and residuals: same-hour inflow/inflow^2/T1/calendar -> same-hour pressure; 21-day Ridge reference with two-day training gap. No prospective target shift in this routine.

**Review coverage:** Focused screening of the primary task, method and relevance to the proposed forecast.
