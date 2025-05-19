# scorer.py

import pandas as pd
from app import evaluate_stock

def score_all_stocks(stock_csv, sector_json):
    df = pd.read_csv(stock_csv)
    sector_data = pd.read_json(sector_json)

    scored_list = []

    for _, row in df.iterrows():
        stock = row.to_dict()
        result = evaluate_stock(stock, sector_data)
        if result:
            scored_list.append(result)

    scored_list.sort(key=lambda x: x['score'], reverse=True)
    return scored_list

def save_rankings(scored_list, filepath="ranked_stocks.csv"):
    import csv
    keys = scored_list[0].keys()
    with open(filepath, 'w', newline='') as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(scored_list)

def score_stock(stock_data):
    """Scores a single stock dict for use in Flask dashboard."""
    import json
    with open("data/sector_averages.json") as f:
        sector_data = json.load(f)

    result = evaluate_stock(stock_data, sector_data)
    return result["score"] if result else 0


if __name__ == "__main__":
    ranked = score_all_stocks("data/stocks_data.csv", "data/sector_averages.json")
    save_rankings(ranked)
    print("Scoring complete. Results saved to ranked_stocks.csv")
