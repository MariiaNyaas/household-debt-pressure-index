# Household Debt Pressure Index

**Independent research — Mariia Nyaas**

[Live dashboard](https://mariianyaas.github.io/household-debt-pressure-index/) (after GitHub Pages deployment)

## Executive question
Can falling aggregate household leverage coexist with rising debt-service pressure?

## Evidence
- Debt / disposable income: 242.1% in H2 2021; 221.9% at end-2024.
- Banking-sector interest expense / disposable income: 9.8% in 2023; 10.9% in 2024.
- Outstanding mortgage interest rate: 5.31% in September 2026 (monthly sample).
- Floating mortgage share: 96.1% in Q3 2026 (quarterly census).

Sources and provenance: `data/ssb_reference_points.json`, `src/methodology.md`.

## Decision tool
`docs/index.html` contains a fully self-contained browser-based affordability simulator. Change income, mortgage, mortgage rate, remaining term, essential spending and income shock. Outputs are hypothetical, not SSB household microdata.

## Publish
Create public repository `household-debt-pressure-index`. Upload these folders and files. In repository Settings > Pages, select Deploy from a branch > main > /docs.

## Limitations
Not a borrower risk score, validated PD model, underwriting system or regulatory affordability test. Macro ratios and scenario outcomes have different definitions and are not statistically linked. Do not interpret as forecasts or bank portfolio observations.

## Attribution
Data: Statistics Norway (SSB), URLs in `data/ssb_reference_points.json`, accessed 2026-11-01. Independent analytical framework and visualization by Mariia Nyaas.
