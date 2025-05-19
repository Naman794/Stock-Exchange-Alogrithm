import threading
import time
import pandas as pd
from fetch.stock_api_fetcher import fetch_and_update_data
from app import evaluate_stock  # scoring logic
from webapp.app import create_app

# === CONFIG ===
STOCK_CSV = "data/stocks_data.csv"
SECTOR_JSON = "data/sector_averages.json"

# === 1️⃣ Stock Engine Runner ===
def run_stock_engine():
    print("[⏳] Running scoring engine...")

    df = pd.read_csv(STOCK_CSV)
    sector_data = pd.read_json(SECTOR_JSON)

    ranked_stocks = []

    for _, row in df.iterrows():
        stock_data = row.to_dict()
        result = evaluate_stock(stock_data, sector_data)
        if result:
            ranked_stocks.append(result)

    ranked_stocks.sort(key=lambda x: x["score"], reverse=True)

    print("\n📈 Top 10 Investment Candidates:")
    for i, stock in enumerate(ranked_stocks[:10], 1):
        print(f"{i}. {stock['stock_name']} - Score: {stock['score']:.2f}")

    print("[✅] Scoring complete.")

# === 2️⃣ Flask Dashboard Runner ===
def run_dashboard():
    app = create_app()
    app.run(debug=False, use_reloader=False)

# === 🔁 Multi-threaded Runner ===
if __name__ == "__main__":
    print("🚀 Launching Stock Engine + Web Dashboard...\n")

    thread_dashboard = threading.Thread(target=run_dashboard)
    thread_engine = threading.Thread(target=run_stock_engine)

    thread_dashboard.start()
    thread_engine.start()

    thread_dashboard.join()
    thread_engine.join()
