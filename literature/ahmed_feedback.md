# Ahmed et al. (2025): feedback-related comparison

Ahmed, S., Dustegor, D., Lazovik, A., & Wörtche, H. J. (2025). *Windowed Multivariate LSTM Autoencoder for Leak Detection in Water Distribution Networks*. The 21st Computing and Control in the Water Industry Conference (CCWI 2025). [Official DOI](https://doi.org/10.15131/shef.data.29921204.v1) · [Unmodified CC BY 4.0 PDF](papers/Ahmed_2025_Windowed_LSTM_Autoencoder.pdf).

The professor explicitly requested this source. It is a **separate feedback supplement** alongside the historical 47-record, 35-group inventory and six selected studies.

## What overlaps and what differs

| Aspect | Ahmed et al. | Submitted n1(+15) proposal |
|---|---|---|
| Measurements | n1/n4/n31 pressure, T1 level, PUMP_1 flow | Same five plus AMR_n1 local consumption |
| Target | Reconstruction of an observed multivariate window; error supports leak detection | Recorded future pressure at one node |
| Preparation | Overlapping 24-hour windows (288 five-minute samples), moving z-score normalization | Current plus previous 55 minutes; +15-minute labels; chronological periods |
| Model | LSTM autoencoder compared with CNN autoencoder | Gradient Boosting compared with persistence, Ridge and Random Forest |
| Evidence of success | Reconstruction errors and leak detection timing | Planned forecast MAE/RMSE on common rows |

The autoencoder compresses and reconstructs its observed multivariate window. Training uses two selected normal-baseline segments, including a segment extending into January 2019, with a random 15% validation selection of windows; testing starts January 15, 2019. The normal-baseline definition includes a persistent background leak. Moving-normalization alignment and overlapping-window dependence matter when comparing protocols (PDF pp. 2–4).

Published Table 1 (p. 4) reports normal reconstruction errors **0.0732 (CNN)** and **0.0031 (LSTM)**. Table 2 (p. 5) reports time to detect the incipient leak of **117 h 20 min (CNN)** and **43 h 55 min (LSTM)**. These author-reported results quantify reconstruction and detection. The comparison uses the paper's method, data description and published tables as its evidence.

The shared measurements connect the student's proposal to established Area C work. His proposed contribution focuses on the future n1 target, AMR_n1 as a candidate signal and C1–C3's controlled comparisons. The report's C3 full-versus-n1-history comparison, with the same calendar inputs, will test whether the auxiliary set helps. That comparison measures the auxiliary set jointly; individual AMR_n1 attribution would require a separate comparison. [Anticipated contributions](../docs/anticipated_contributions.md).
