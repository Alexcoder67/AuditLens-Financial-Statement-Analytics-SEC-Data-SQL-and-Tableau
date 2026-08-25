import os
import requests
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get('DATABASE_URL')
USER_AGENT = os.environ.get('SEC_USER_AGENT')

COMPANIES = [
    {"cik": "0000320193", "name": "Apple Inc.", "ticker": "AAPL", "sector": "Technology"},
    {"cik": "0000789019", "name": "Microsoft Corporation", "ticker": "MSFT", "sector": "Technology"},
    {"cik": "0001652044", "name": "Alphabet Inc.", "ticker": "GOOGL", "sector": "Technology"},
    {"cik": "0001018724", "name": "Amazon.com, Inc.", "ticker": "AMZN", "sector": "Technology"},
    {"cik": "0001326801", "name": "Meta Platforms, Inc.", "ticker": "META", "sector": "Technology"},
    {"cik": "0001318605", "name": "Tesla, Inc.", "ticker": "TSLA", "sector": "Automotive"},
    {"cik": "0001045810", "name": "NVIDIA Corporation", "ticker": "NVDA", "sector": "Semiconductors"},
    {"cik": "0000796343", "name": "Adobe Inc.", "ticker": "ADBE", "sector": "Software"},
    {"cik": "0001543151", "name": "Uber Technologies, Inc.", "ticker": "UBER", "sector": "Transportation"},
    {"cik": "0000936468", "name": "Lockheed Martin Corporation", "ticker": "LMT", "sector": "Defense"},
    {"cik": "0001136352", "name": "MetLife, Inc.", "ticker": "MET", "sector": "Insurance"},
    {"cik": "0000012927", "name": "The Boeing Company", "ticker": "BA", "sector": "Aerospace"},
]

CONCEPTS = ["Revenues", "NetIncomeLoss", "Assets", "Liabilities"]

def get_connection():
    return psycopg2.connect(DATABASE_URL)

def insert_companies():
    conn = get_connection()
    cur = conn.cursor()
    for company in COMPANIES:
        cur.execute(
            """
            INSERT INTO companies (cik, name, ticker, sector)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (cik) DO NOTHING
            """,
            (company["cik"], company["name"], company["ticker"], company["sector"])
        )
    conn.commit()
    cur.close()
    conn.close()
    print(f"Inserted {len(COMPANIES)} companies.")

def fetch_company_concept(cik, concept):
    url = f"https://data.sec.gov/api/xbrl/companyconcept/CIK{cik}/us-gaap/{concept}.json"
    headers = {"User-Agent": USER_AGENT}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def insert_filings_from_data(cik, data):
    conn = get_connection()
    cur = conn.cursor()
    seen = set()
    count = 0
    for entry in data["units"]["USD"]:
        accn = entry["accn"]
        if accn in seen:
            continue
        seen.add(accn)
        cur.execute(
            """
            INSERT INTO filings (accession_number, cik, form_type, fiscal_year, fiscal_period, filed_date)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (accession_number) DO NOTHING
            """,
            (accn, cik, entry["form"], entry["fy"], entry["fp"], entry["filed"])
        )
        count += 1
    conn.commit()
    cur.close()
    conn.close()
    print(f"Inserted {count} filings.")

def insert_financial_facts(cik, concept, data):
    conn = get_connection()
    cur = conn.cursor()
    count = 0
    for entry in data["units"]["USD"]:
        cur.execute(
            """
            INSERT INTO financial_facts (cik, accession_number, concept, period_start, period_end, value, unit)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (cik, entry["accn"], concept, entry.get("start"), entry["end"], entry["val"], "USD")
        )
        count += 1
    conn.commit()
    cur.close()
    conn.close()
    print(f"Inserted {count} facts for {concept}.")

if __name__ == "__main__":
    insert_companies()
    for company in COMPANIES:
        cik = company["cik"]
        for concept in CONCEPTS:
            print(f"Fetching {concept} for {company['name']}...")
            try:
                data = fetch_company_concept(cik, concept)
                insert_filings_from_data(cik, data)
                insert_financial_facts(cik, concept, data)
            except requests.exceptions.HTTPError:
                print(f"  Skipped: {concept} not found for {company['name']}")