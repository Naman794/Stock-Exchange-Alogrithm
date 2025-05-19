# fetch/stock_api_fetcher.py

import requests
import pandas as pd
import time
from app import evaluate_stock
from config import API_BASE, API_KEY

HEADERS = {
    "Authorization": f"Bearer {API_KEY}"
}

def get_most_active_stocks():
    try:
        res = requests.get(f"{API_BASE}/NSE_most_active", headers=HEADERS, timeout=10)
        if res.status_code == 200:
            return res.json().get("data", [])
        return []
    except Exception as e:
        print("Error:", e)
        return []

def get_stock_details(name):
    try:
        res = requests.get(f"{API_BASE}/stock", params={"name": name}, headers=HEADERS, timeout=10)
        if res.status_code == 200:
            return res.json()
        return None
    except Exception as e:
        print(f"Error fetching details for {name}:", e)
        return None

def fetch_and_update_data():
    print("[📡] Fetching top active stocks...")
    active_stocks = get_most_active_stocks()
    if not active_stocks:
        print("[❌] No active stocks received.")
        return

    sector_data = {
        "IT": {"pe": 25, "roce": 20, "roe": 18},
        "Finance": {"pe": 18, "roce": 14, "roe": 13},
        "Energy": {"pe": 12, "roce": 15, "roe": 12}
    }

    results = []
    for stock in active_stocks[:10]:  # limit to 10 to stay under quota
        name = stock.get("name")
        print(f"[→] Fetching: {name}")
        stock_details = get_stock_details(name)
        time.sleep(1.2)  # 1 request/sec throttle

        if not stock_details:
            continue

        stock_data = {
            "name": name,
            "symbol": stock_details.get("symbol"),
            "sector": stock_details.get("sector", "Misc"),
            "promoter_holding": stock_details.get("promoterHolding", 50),
            "public_holding": 100 - stock_details.get("promoterHolding", 50),
            "fii_holding": stock_details.get("fii", 0),
            "dii_holding": stock_details.get("dii", 0),
            "num_shareholders": stock_details.get("shareholders", 5000),
            "total_debt": stock_details.get("totalDebt", 0),
            "total_equity": stock_details.get("totalEquity", 100),
            "free_cash_flow": stock_details.get("fcf", 100),
            "capex": stock_details.get("capex", 50),
            "revenue": stock_details.get("revenue", 1000),
            "fixed_assets": stock_details.get("fixedAssets", 400),
            "current_assets": stock_details.get("currentAssets", 600),
            "current_liabilities": stock_details.get("currentLiabilities", 300),
            "total_assets": stock_details.get("totalAssets", 1500),
            "total_liabilities": stock_details.get("totalLiabilities", 800),
            "pe": stock_details.get("peRatio", 20),
            "roce": stock_details.get("roce", 15),
            "roe": stock_details.get("roe", 14),
            "current_ratio": stock_details.get("currentRatio", 1.8),
            "net_margin": stock_details.get("netMargin", 12),
            "eps_growth_3y": stock_details.get("epsGrowth", 10),
            "revenue_growth_3y": stock_details.get("revenueGrowth", 10),
            "debt_equity": stock_details.get("deRatio", 0.5),
            "sales_q1": stock_details.get("qSales1", 400),
            "sales_q2": stock_details.get("qSales2", 450),
            "sales_q3": stock_details.get("qSales3", 500),
            "profit_q1": stock_details.get("qProfit1", 50),
            "profit_q2": stock_details.get("qProfit2", 55),
            "profit_q3": stock_details.get("qProfit3", 65)
        }

        result = evaluate_stock(stock_data, sector_data)
        if result:
            results.append(result)

    if results:
        df = pd.DataFrame(results)
        df.to_csv("data/stocks_data.csv", index=False)
        print(f"[✅] Saved {len(results)} scored stocks.")
    else:
        print("[⚠️] No valid results to save.")
