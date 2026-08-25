AuditLens

This is AuditLens, it pulls actual financial filings from 12 public companies across 8 sectors: Apple, Microsoft, Alphabet, Amazon, Meta, Tesla, NVIDIA, Adobe, Uber, Lockheed Martin, MetLife and Boeing. Calculating real financial ratios, and showing real financial events.

Live Dashboard: AuditLens: Financial Analytics Dashboard

Built with Python, SQL, and Tableau. Used SEC as the only data source.

What does it do?

* Pulls real GAAP financial data (Revenue, Net Income, Assets, Liabilites) directly from SEC for 12 public companies spanning 8 sectors: Technology, Automotive, Semiconductors, Software, Defense, Insurance, Aerospace, and Transportation

* Calculates real financial ratios: net profit margic, debt-to-assets ratio, yoy growth

* Sorts and cleans up the raw SEC data so numbers don't get counted twice

* Visualizes data through 5 interactive Tableau charts, including hover-trigged annotations that explain real events at the exact data point they occurred

Tech Stack

Layer	Tool
Data source	SEC EDGAR XBRL API
Ingestion	Python (requests, psycopg2)
Database	PostgreSQL
Analytics	SQL (window functions, deduplication logic)
Visualization	Tableau Public

SEC EDGAR API → Pythn script →eSL)
         				      ↓
                                    SQL views (deduplication,
                                    ratio calculations, trends)
                                              ↓
                                    Tableau Public dashboard 

Database Schema

* company metadata - (Name, ticker, sector)
* filings - SEC filings
* financials - every reported GAAP value tagged by period
* company ratios - calculated financial ratios per company per yet
* yoy changes / peer_comparison - trend calculations

Dashboard

The published dashboards include 5 interactive visualizations:

* Revenue Growth by Compamy - revenue over time for 12 companies (2008-2026)
* Net Profit Margin Trends - used hover annotations explaining real anomalies at companies, Alphabet, Uber, NVIDIA, and Tesla
* Average Profit Margin by Sector - cross-sector profitability across sectors
* Debt-to-Assets Trend - tracks how much debt each company carries over time, across the 12 companies
* Revenue Share by Sector - show's what percent each sector makes up

Whats next?

* Adding a Django REST API layer to make the data accessible outside of Tableau

* Expand sector coverage beyond the current companies


This project pulls real financial data, using actual SEC filings, real GAAP concepts, and genuine historical events.

Connect: [LinkedIn](https://www.linkedin.com/in/alexanderguadalupe) · [GitHub](https://github.com/Alexcoder67)
