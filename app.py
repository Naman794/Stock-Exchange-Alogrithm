from filters.shareholding_filter import calculate_shareholding_score
from filters.balance_sheet_analyzer import calculate_balance_sheet_score
from filters.sector_filter import is_sector_allowed, get_sector_penalty
from filters.policy_adjuster import get_policy_bonus
from filters.peer_comparison import calculate_peer_score
from filters.core_financials import calculate_core_financial_score
from filters.quarterly_trend import calculate_quarterly_trend_score
from filters.final_scoring import calculate_final_score


# You can later import more:
# from filters.core_financials import ...
# from filters.quarterly_trend import ...
# from filters.final_scoring import ...

def evaluate_stock(stock_data, sector_data):
    # Step 1: Sector check
    if not is_sector_allowed(stock_data['sector']):
        return None  # Exclude stock

    total_score = 0

    # Step 2: Shareholding Filter
    total_score += calculate_shareholding_score(
        fii=stock_data['fii_holding'],
        dii=stock_data['dii_holding'],
        public=stock_data['public_holding'],
        promoter=stock_data['promoter_holding'],
        num_shareholders=stock_data['num_shareholders']
    )

    # Step 3: Balance Sheet Filter
    total_score += calculate_balance_sheet_score(stock_data)

    # Step 4: Sector penalty
    total_score += get_sector_penalty(stock_data['sector'])

    # Step 5: Policy bonus
    total_score += get_policy_bonus(stock_data['sector'])

    # Step 6: Peer Comparison
    total_score += calculate_peer_score(
        stock_metrics={
            'pe': stock_data['pe'],
            'roce': stock_data['roce'],
            'roe': stock_data['roe']
        },
        sector_metrics=sector_data.get(stock_data['sector'], {})
    )

    return {
        "stock_name": stock_data["name"],
        "score": total_score
    }


def evaluate_stock(stock_data, sector_data):
    if not is_sector_allowed(stock_data['sector']):
        return None

    total_score = 0

    total_score += calculate_shareholding_score(
        fii=stock_data['fii_holding'],
        dii=stock_data['dii_holding'],
        public=stock_data['public_holding'],
        promoter=stock_data['promoter_holding'],
        num_shareholders=stock_data['num_shareholders']
    )

    total_score += calculate_balance_sheet_score(stock_data)
    total_score += get_sector_penalty(stock_data['sector'])
    total_score += get_policy_bonus(stock_data['sector'])

    total_score += calculate_peer_score(
        stock_metrics={
            'pe': stock_data['pe'],
            'roce': stock_data['roce'],
            'roe': stock_data['roe']
        },
        sector_metrics=sector_data.get(stock_data['sector'], {})
    )

    total_score += calculate_core_financial_score(stock_data)

    return {
        "stock_name": stock_data["name"],
        "score": total_score
    }


def evaluate_stock(stock_data, sector_data):
    if not is_sector_allowed(stock_data['sector']):
        return None

    total_score = 0

    total_score += calculate_shareholding_score(...)
    total_score += calculate_balance_sheet_score(stock_data)
    total_score += get_sector_penalty(stock_data['sector'])
    total_score += get_policy_bonus(stock_data['sector'])
    total_score += calculate_peer_score(...)
    total_score += calculate_core_financial_score(stock_data)
    total_score += calculate_quarterly_trend_score(stock_data)

    return {
        "stock_name": stock_data["name"],
        "score": total_score
    }


def evaluate_stock(stock_data, sector_data):
    if not is_sector_allowed(stock_data['sector']):
        return None

    scores = {}

    scores["shareholding"] = calculate_shareholding_score(
        fii=stock_data['fii_holding'],
        dii=stock_data['dii_holding'],
        public=stock_data['public_holding'],
        promoter=stock_data['promoter_holding'],
        num_shareholders=stock_data['num_shareholders']
    )
    scores["balance_sheet"] = calculate_balance_sheet_score(stock_data)
    scores["sector_penalty"] = get_sector_penalty(stock_data['sector'])
    scores["policy_bonus"] = get_policy_bonus(stock_data['sector'])
    scores["peer_comparison"] = calculate_peer_score(
        stock_metrics={
            'pe': stock_data['pe'],
            'roce': stock_data['roce'],
            'roe': stock_data['roe']
        },
        sector_metrics=sector_data.get(stock_data['sector'], {})
    )
    scores["core_financials"] = calculate_core_financial_score(stock_data)
    scores["quarterly_trend"] = calculate_quarterly_trend_score(stock_data)

    final_score = calculate_final_score(scores)

    return {
        "stock_name": stock_data["name"],
        "score": final_score,
        "breakdown": scores
    }
