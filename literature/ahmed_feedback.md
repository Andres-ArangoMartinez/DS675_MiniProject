# Ahmed et al. (2025): feedback-related comparison

Ahmed, S., Dustegor, D., Lazovik, A., & Wörtche, H. J. (2025). *Windowed Multivariate LSTM Autoencoder for Leak Detection in Water Distribution Networks*. The 21st Computing and Control in the Water Industry Conference (CCWI 2025). [DOI](https://doi.org/10.15131/shef.data.29921204.v1) · [Retained CC BY 4.0 PDF](papers/Ahmed_2025_Windowed_LSTM_Autoencoder.pdf).

Requested by the professor, this **feedback-response supplement** remains separate from the historical 47 records, 35 groups and six detailed selections.

## What overlaps and what differs

| Aspect | Ahmed et al. | Submitted n1(+15) proposal |
|---|---|---|
| Measurements | n1/n4/n31 pressures, T1 level, PUMP_1 flow | Same five plus AMR_n1 consumption |
| Target | Observed-window reconstruction for leak detection | Future recorded n1 pressure |
| Preparation | Overlapping 24-hour windows (288 five-minute samples), moving z-score normalization | Current reading plus 55-minute history; +15-minute labels; chronological periods |
| Model | LSTM versus CNN autoencoder | Gradient Boosting versus persistence, Ridge and Random Forest |
| Evaluation | Reconstruction error and detection timing | Planned forecast MAE/RMSE on common rows |

The autoencoder compresses and reconstructs observed multivariate windows. Training uses two selected normal-baseline segments, including one extending into January 2019, and randomly selects 15% of windows for validation. Testing starts January 15, 2019. The baseline includes a persistent background leak. Moving-normalization alignment and overlapping windows affect protocol comparisons (PDF pp. 2–4).

The authors report normal reconstruction errors **0.0732 (CNN)** and **0.0031 (LSTM)** in Table 1 (p. 4), and incipient-leak detection times **117 h 20 min (CNN)** and **43 h 55 min (LSTM)** in Table 2 (p. 5). These measure reconstruction/detection rather than n1(+15) forecast error; this review uses the published method and tables.

The proposed extension concerns the future n1 target, AMR_n1 as a candidate and [controlled C1–C3 comparisons](../docs/anticipated_contributions.md). C3 would test the auxiliary set jointly against n1 history with the same calendar inputs; it would not isolate AMR_n1's individual effect.
