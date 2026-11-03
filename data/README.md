# Frozen data

`raw/INDPRO_2026-10-22.csv` is a byte-for-byte copy of the original full-history FRED download (1,293 monthly rows). The analysis explicitly selects October 2006–September 2026, exactly 240 observations. The CSV date labels the monthly reference period, not a daily observation. No COVID observations are removed or altered.

Publisher: Board of Governors of the Federal Reserve System (US). Distributor: FRED, Federal Reserve Bank of St. Louis. Series: **Industrial Production: Total Index (INDPRO)**; monthly, seasonally adjusted, Index 2017=100.

Source: https://fred.stlouisfed.org/series/INDPRO  
Original download endpoint: https://fred.stlouisfed.org/graph/fredgraph.csv?id=INDPRO  
Snapshot retrieved: October 22, 2026 (America/New_York). Download completion: October 23, 2026, 03:34:07 UTC.

The notebook validates SHA-256 against `reference_results.json`. Historical FRED observations may be revised. There is intentionally no automatic data refresh: this snapshot defines the submitted analysis.

`reference_results.json` records numerical benchmarks from the original executed analysis and report. It is used only for validation, never to replace fitted coefficients or generated predictions. Bootstrap references were printed to four decimals in the original notebook.

Suggested attribution: Board of Governors of the Federal Reserve System (US), Industrial Production: Total Index [INDPRO], retrieved from FRED, Federal Reserve Bank of St. Louis, October 22, 2026. No license for third-party data or the report is implied by this repository.
