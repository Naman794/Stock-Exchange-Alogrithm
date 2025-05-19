# filters/core_financials.py

def score_current_ratio(current_ratio):
    if current_ratio >= 2:
        return 5
    elif current_ratio >= 1.5:
        return 3
    return 0

def score_net_margin(net_margin):
    if net_margin >= 15:
        return 5
    elif net_margin >= 10:
        return 3
    return 0

def score_growth(value):
    if value >= 20:
        return 5
    elif value >= 10:
        return 3
    return 0

def score_debt_equity(de_ratio):
    if de_ratio <= 0.5:
        return 5
    elif de_ratio <= 1:
        return 3
    return 0

def calculate_core_financial_score(stock):
    score = 0
    score += score_current_ratio(stock['current_ratio'])
    score += score_net_margin(stock['net_margin'])
    score += score_growth(stock['eps_growth_3y'])
    score += score_growth(stock['revenue_growth_3y'])
    score += score_debt_equity(stock['debt_equity'])
    return score  # Max 25
