CREATE OR REPLACE VIEW yoy_changes AS
SELECT
    name,
    ticker,
    fiscal_year,
    net_profit_margin,
    debt_to_assets_ratio,
    LAG(net_profit_margin) OVER (PARTITION BY ticker ORDER BY fiscal_year) AS prior_year_margin,
    ROUND(
        (net_profit_margin - LAG(net_profit_margin) OVER (PARTITION BY ticker ORDER BY fiscal_year))
        / NULLIF(ABS(LAG(net_profit_margin) OVER (PARTITION BY ticker ORDER BY fiscal_year)), 0) * 100,
        1
    ) AS margin_pct_change
FROM company_ratios
ORDER BY ticker, fiscal_year;

CREATE OR REPLACE VIEW peer_comparison AS
SELECT
    name,
    ticker,
    fiscal_year,
    net_profit_margin,
    ROUND(AVG(net_profit_margin) OVER (PARTITION BY fiscal_year), 4) AS peer_avg_margin,
    ROUND(net_profit_margin - AVG(net_profit_margin) OVER (PARTITION BY fiscal_year), 4) AS margin_diff_from_peers
FROM company_ratios
WHERE net_profit_margin IS NOT NULL
ORDER BY fiscal_year, ticker;