import requests
import pandas as pd
import time
import json
from datetime import datetime

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}

BASE_URL = "https://www.nseindia.com/api"

def get_stock_financials(symbol):
    url = f"{BASE_URL}/quote-equity?symbol={symbol}"
    session = requests.Session()
    session.headers.update(HEADERS)
    session.get("https://www.nseindia.com", timeout=5)  # sets cookies

    response = session.get(url, timeout=10)
    if response.status_code != 200:
        print(f"Failed to fetch {symbol}")
        return None

    data = response.json()
    info = data.get("info", {})
    financials = data.get("financials", {}).get("data", [])

    return {
        "name": info.get("companyName"),
        "symbol": symbol,
        "sector": info.get("industry"),
        "market_cap": float(info.get("marketCap", "0").replace(",", "")) / 1e7,  # ₹cr
        "promoter_holding": info.get("promotorHolding"),
        "roe": info.get("returnOnEquity"),
        "debt_to_equity": info.get("debtEquity"),
        "revenue_growth": info.get("revenueGrowth"),
        "profit_growth": info.get("profitGrowth"),
    }

def main():
    symbols = ["TCS", "HDFCBANK", "RELIANCE", "LT", "INFY"]
    rows = []

    for sym in symbols:
        data = get_stock_financials(sym)
        if data:
            rows.append(data)
        time.sleep(2)  # prevent blocking

    df = pd.DataFrame(rows)
    df.to_csv("data/stocks_data.csv", index=False)
    print("✅ Saved to data/stocks_data.csv")

if __name__ == "__main__":
    main()
