# 📈 Stock Exchange Algorithm

A modular algorithm that screens, filters, scores, and tracks stocks based on financial fundamentals, sector performance, and policy trends. Designed for clarity and extensibility.

---

## 🗂️ Project Structure

### Root Files

- `main.py` – Entry point for executing the stock analysis pipeline.
- `app.py` – Bootstraps secondary processes or APIs.
- `config.py` – Central configuration management.
- `README.md` – Project documentation.
- `LICENSE` – Licensing info.

---

## 📁 Key Modules

### `src/data/`

- Static and pre-processed stock data:
  - `stocks_data.csv`, `policy_tags.json`, `sector_tags.json`, `sector_averages.json`, `trending.json`
- `fetch_nse_data.py` – Downloads/upgrades NSE stock data.

### `src/fetch/`

- Data fetchers for stock information:
  - `nse_fetcher.py` – Fetches real-time data from NSE.
  - `stock_api_fetcher.py` – External API integration for stock metrics.

### `src/db/`

- MongoDB storage handlers:
  - `mongo.py` – Manages MongoDB operations.
  - `snapshot.py` – Loads/saves periodic data snapshots.

### `src/filters/`

- Core filtering logic for stock selection:
  - `balance_sheet_analyzer.py`
  - `core_financials.py`
  - `final_scoring.py`
  - `peer_comparison.py`
  - `policy_adjuster.py`
  - `quarterly_trend.py`
  - `sector_filter.py`
  - `shareholding_filter.py`

### `src/scorer/`

- Scoring logic:
  - `ranker.py` – Ranks stocks based on combined filter output.

### `src/tracker/`

- Portfolio maintenance tools:
  - `prune_rebalance.py` – Removes underperformers and reallocates.
  - `quarterly_monitor.py` – Tracks updates and financial releases.

### `src/webapp/`

- Basic Flask dashboard:
  - `app.py` – Web server.
  - `routes.py` – API/view routing.
  - `templates/dashboard.html` – Frontend dashboard.

---

## 🔁 Algorithm Workflow

1. 📥 Fetch stock and sector data.
2. 🔍 Apply filters based on balance sheets, shareholding, trends, and peer comparisons.
3. 🧠 Score and rank filtered stocks.
4. 📊 Monitor performance and rebalance periodically.
5. 🌐 Visualize results via a web dashboard.

---

## 🛠️ Notes

- Built with modularity in mind — each filter and fetcher is easily extendable.
- Flask dashboard is minimal and designed for internal metrics display.

---

