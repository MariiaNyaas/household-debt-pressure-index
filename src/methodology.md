# Methodology and audit trail

## Sources / observation dates
- SSB financial accounts for households in 2024: https://www.ssb.no/en/nasjonalregnskap-og-konjunkturer/finansregnskap/artikler/financial-accounts-for-households-in-2024
- SSB interest rates in banks and mortgage companies, updated 29 October 2026: https://www.ssb.no/en/bank-og-finansmarked/finansinstitusjoner-og-andre-finansielle-foretak/statistikk/renter-i-banker-og-kredittforetak
- Distribution reference (not merged or used as microdata): https://www.ssb.no/en/statbank1/table/06468/

## Interest / mortgage accounting
Annual effective *assumed nominal* mortgage rate r in percent; monthly r/1200. Monthly annuity M = P × i / (1 − (1+i)^(−12Y)). For r=0, M=P/(12Y). Rate from SSB is used as an illustrative baseline; the annuity calculation assumes monthly compounding and may differ from lenders’ effective interest calculations.

Monthly post-shock disposable income = annual disposable income × (1 + assumed income shock/100)/12.
Monthly residual = post-shock income − monthly annuity payment − essential non-debt monthly costs.
Payment-to-income ratio = annuity payment / post-shock monthly disposable income.
The monthly residual is a scenario cash flow, not a calibrated probability of default.

## Important denominator caveat
The aggregate household debt-income ratio and aggregate banking-sector interest-expense burden use disposable income and are macro financial-account indicators, not debt service ratios for an individual household. Model debt / income is a hypothetical borrower's mortgage balance divided by user-entered disposable income, and is not comparable to regulatory gross-income DTI ceilings.

## Boundaries
This project is descriptive macro evidence plus deterministic scenario modelling. No forecast performance, causal claims, loan-level outcomes, actual bank policy thresholds or representative household distributions are asserted. Inputs are user-set and synthetic. No confidential material.
