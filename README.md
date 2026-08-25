# AuditLens

This is AuditLens, a financial analytics project built on real SEC data. It pulls actual financial filings from 12 public companies across 8 sectors: Apple, Microsoft, Alphabet, Amazon, Meta, Tesla, NVIDIA, Adobe, Uber, Lockheed Martin, MetLife, and Boeing. It calculates real financial ratios and shows real financial trends.

**Live Dashboard:** [AuditLens: Financial Analytics Dashboard](https://public.tableau.com/app/profile/alexmaz.203/)

Built with Python, SQL, and Tableau. Used SEC as the only data source.

## What does it do?

- Pulls real GAAP financial data (Revenue, Net Income, Assets, Liabilities) directly from SEC for 12 public companies spanning 8 sectors: Technology, Automotive, Semiconductors, Software, Defense, Insurance, Aerospace, and Transportation
- Calculates real financial ratios: net profit margin, debt-to-assets ratio, year-over-year growth
- Sorts and cleans up the raw SEC data so numbers don't get counted twice
- Visualizes the data through 5 interactive Tableau charts

## Tech Stack

| Layer | Tool |
|---|---|
| Data source | SEC EDGAR XBRL API |
| Ingestion | Python (requests, psycopg2) |
| Database | PostgreSQL |
| Visualization | Tableau Public |

```
SEC EDGAR API → Python script →      SQL
                                      ↓
                              SQL views (cleaning,
                              ratio calculations)
                                      ↓
                              Tableau Public dashboard
```


## Database Schema

- **companies** — company metadata (name, ticker, sector)
- **filings** — SEC filings
- **financial_facts** — every reported GAAP value, tagged by period
- **company_ratios** — calculated financial ratios per company per year

## Dashboard

The published dashboard includes 5 interactive visualizations:

- **Revenue Growth by Company** — revenue over time for 12 companies (2008-2026)
- **Net Profit Margin Trends** — profit margin over time across all 12 companies
- **Average Profit Margin by Sector** — profitability compared across sectors
- **Debt-to-Assets Trend** — tracks how much debt each company carries over time
- **Revenue Share by Sector** — shows what percent each sector makes up

## What's next?

- Adding a Django REST API layer to make the data accessible outside of Tableau
- Expand sector coverage beyond the current companies

---

This project pulls real financial data, using actual SEC filings and real GAAP concepts.

**Connect:** [LinkedIn](https://www.linkedin.com/in/alexanderguadalupe) · [GitHub](https://github.com/Alexcoder67)