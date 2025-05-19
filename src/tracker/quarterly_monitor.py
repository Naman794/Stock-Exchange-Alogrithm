import json
import pandas as pd
from app import evaluate_stock

PORTFOLIO_FILE = "data/portfolio.json"
SCORE_HISTORY_FILE = "data/score_history.json"
STOCKS_DATA_FILE = "data/stocks_data.csv"
SECTOR_DATA_FILE = "data/sector_averages.json"

THRESHOLD_ALERT = 5  # Points change to trigger alert

def load_portfolio():
    with open(PORTFOLIO_FILE, "r") as f:
        return json.load(f)

def load_score_history():
    try:
        with open(SCORE_HISTORY_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_score_history(score_history):
    with open(SCORE_HISTORY_FILE, "w") as f:
        json.dump(score_history, f, indent=2)

def monitor_quarterly():
    portfolio = load_portfolio()
    score_history = load_score_history()
    df = pd.read_csv(STOCKS_DATA_FILE)
    sector_data = pd.read_json(SECTOR_DATA_FILE)

    alerts = []

    for stock_name in portfolio:
        stock_data = df[df["name"] == stock_name].to_dict(orient="records")
        if not stock_data:
            print(f"⚠️ Data missing for {stock_name}")
            continue
        stock_data = stock_data[0]

        result = evaluate_stock(stock_data, sector_data)
        if not result:
            print(f"⚠️ {stock_name} did not pass filters this quarter.")
            continue

        new_score = result["score"]
        old_score = score_history.get(stock_name, {}).get("score", None)

        if old_score is not None:
            change = new_score - old_score
            if abs(change) >= THRESHOLD_ALERT:
                alert_type = "Improved" if change > 0 else "Declined"
                alerts.append({
                    "stock": stock_name,
                    "change": change,
                    "old_score": old_score,
                    "new_score": new_score,
                    "alert": alert_type
                })

        score_history[stock_name] = {
            "score": new_score,
            "breakdown": result.get("breakdown", {}),
        }

    save_score_history(score_history)

    print("=== Quarterly Monitoring Report ===")
    if alerts:
        for alert in alerts:
            arrow = "⬆️" if alert["alert"] == "Improved" else "⬇️"
            print(f"{arrow} {alert['stock']}: {alert['alert']} by {alert['change']:.2f} points "
                  f"(Old: {alert['old_score']:.2f}, New: {alert['new_score']:.2f})")
    else:
        print("No significant changes detected this quarter.")

if __name__ == "__main__":
    monitor_quarterly()
