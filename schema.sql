CREATE TABLE IF NOT EXISTS companies (
    cik VARCHAR(10) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    ticker VARCHAR(10),
    sector VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS filings (
    accession_number VARCHAR(20) PRIMARY KEY,
    cik VARCHAR(10) REFERENCES companies(cik),
    form_type VARCHAR(10),
    fiscal_year INTEGER,
    fiscal_period VARCHAR(5),
    filed_date DATE
);

CREATE TABLE IF NOT EXISTS financial_facts (
    id SERIAL PRIMARY KEY,
    cik VARCHAR(10) REFERENCES companies(cik),
    accession_number VARCHAR(20) REFERENCES filings(accession_number),
    concept VARCHAR(100),
    period_start DATE,
    period_end DATE,
    value NUMERIC,
    unit VARCHAR(10)
);

CREATE INDEX IF NOT EXISTS idx_financial_facts_cik_concept ON financial_facts(cik, concept);
CREATE INDEX IF NOT EXISTS idx_financial_facts_period ON financial_facts(period_end);