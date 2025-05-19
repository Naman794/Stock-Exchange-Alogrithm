import json
import pandas as pd
from app import evaluate_stock

PORTFOLIO_FILE = "data/portfolio.json"
SCORE_HISTORY_FILE = "data/score_history.json"
STOCKS_DATA_FILE = "data/stocks_data.csv"
SECTOR_DATA_FILE = "data/sector_averages.json"

def load_portfolio():
    with open(PORTFOLIO_FILE, "r") as f:
        return json.load(f)

def load_score_history():
    with open(SCORE_HISTORY_FILE, "r") as f:
        return json.load(f)

def save_score_history(score_history):
    with open(SCORE_HISTORY_FILE, "w") as f:
        json.dump(score_history, f, indent=2)

def prune_and_rebalance():
    portfolio = load_portfolio()
    score_history = load_score_history()
    df = pd.read_csv(STOCKS_DATA_FILE)
    sector_data = pd.read_json(SECTOR_DATA_FILE)

    to_sell = []
    to_hold_or_buy_more = []

    for stock_name in portfolio:
        stock_data = df[df["name"] == stock_name].to_dict(orient='records')
        if not stock_data:
            print(f"⚠️ {stock_name} data missing.")
            continue
        stock_data = stock_data[0]

        result = evaluate_stock(stock_data, sector_data)
        if not result:
            print(f"⚠️ {stock_name} failed filters.")
            continue

        new_score = result["score"]
        old_score = score_history.get(stock_name, {}).get("score", None)

        if old_score is not None:
            diff = new_score - old_score
            if diff < -5:
                to_sell.append((stock_name, old_score, new_score))
            else:
                to_hold_or_buy_more.append((stock_name, old_score, new_score))
        else:
            # No old score, treat as hold for now
            to_hold_or_buy_more.append((stock_name, None, new_score))

        # Update score history
        score_history[stock_name] = {"score": new_score, "breakdown": result.get("breakdown", {})}

    save_score_history(score_history)

    print("Prune and Rebalance Report:")
    print("To SELL:")
    for s, old, new in to_sell:
        print(f" - {s}: Score dropped from {old:.2f} to {new:.2f}")
    print("To HOLD/BUY MORE:")
    for s, old, new in to_hold_or_buy_more:
        print(f" - {s}: Score changed from {old} to {new:.2f}")

if __name__ == "__main__":
    prune_and_rebalance()
