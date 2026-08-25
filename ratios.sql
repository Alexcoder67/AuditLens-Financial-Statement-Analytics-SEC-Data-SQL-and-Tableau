CREATE OR REPLACE VIEW primary_facts AS
SELECT DISTINCT ON (ff.cik, ff.concept, ff.period_start, ff.period_end)
    ff.cik,
    ff.concept,
    ff.period_start,
    ff.period_end,
    ff.value,
    ff.accession_number,
    f.filed_date,
    f.fiscal_year
FROM financial_facts ff
JOIN filings f ON f.accession_number = ff.accession_number
WHERE f.form_type = '10-K'
ORDER BY ff.cik, ff.concept, ff.period_start, ff.period_end, f.filed_date ASC;

CREATE OR REPLACE VIEW company_ratios AS
SELECT
    c.name,
    c.ticker,
    c.sector,
    EXTRACT(YEAR FROM r.period_end)::INTEGER AS fiscal_year,
    r.value AS revenue,
    n.value AS net_income,
    a.value AS total_assets,
    l.value AS total_liabilities,
    ROUND(n.value / NULLIF(r.value, 0), 4) AS net_profit_margin,
    ROUND(l.value / NULLIF(a.value, 0), 4) AS debt_to_assets_ratio
FROM companies c
JOIN primary_facts r ON r.cik = c.cik AND r.concept = 'Revenues'
JOIN primary_facts n ON n.cik = c.cik AND n.concept = 'NetIncomeLoss' AND n.period_start = r.period_start AND n.period_end = r.period_end
JOIN primary_facts a ON a.cik = c.cik AND a.concept = 'Assets' AND a.period_end = r.period_end
LEFT JOIN primary_facts l ON l.cik = c.cik AND l.concept = 'Liabilities' AND l.period_end = r.period_end
WHERE (r.period_end - r.period_start) > 300
ORDER BY c.name, fiscal_year;