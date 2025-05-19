# webapp/routes.py

from flask import Blueprint, render_template, request, jsonify
from fetch.stock_api_fetcher import fetch_and_update_data
from scorer.ranker import score_stock  # assuming score_stock(dict) returns score
import pandas as pd
import os

main = Blueprint("main", __name__)

DATA_PATH = "data/stocks_data.csv"

@main.route("/")
def dashboard():
    return render_template("dashboard.html")

@main.route("/fetch", methods=["POST"])
def fetch_and_score():
    symbol = request.json.get("symbol")
    if not symbol:
        return jsonify({"error": "Missing symbol"}), 400

    stock_data = fetch_and_update_data(symbol)
    if not stock_data:
        return jsonify({"error": "Unable to fetch stock data"}), 500

    score = score_stock(stock_data)
    stock_data["score"] = score

    # Save to CSV
    df = pd.DataFrame([stock_data])
    if os.path.exists(DATA_PATH):
        df.to_csv(DATA_PATH, mode='a', index=False, header=False)
    else:
        df.to_csv(DATA_PATH, index=False)

    return jsonify(stock_data)

@main.route("/list")
def list_ranked_stocks():
    df = pd.read_csv("data/stocks_data.csv")
    df = df[df["score"] > 70]  # or top N logic
    df = df.sort_values("score", ascending=False)
    return jsonify(df.to_dict(orient="records"))
