# filters/balance_sheet_analyzer.py

def debt_to_equity_score(debt, equity):
    if equity == 0:
        return 0
    ratio = debt / equity
    if ratio < 0.5:
        return 5
    elif ratio <= 1.0:
        return 3
    return 0

def fcf_vs_capex_score(fcf, capex):
    return 5 if fcf > capex else 0

def fat_score(revenue, fixed_assets):
    if fixed_assets == 0:
        return 0
    ratio = revenue / fixed_assets
    if ratio > 2:
        return 5
    elif ratio >= 1:
        return 2
    return 0

def working_capital_score(current_assets, current_liabilities):
    return 5 if current_assets - current_liabilities > 0 else 0

def asset_vs_liability_score(total_assets, total_liabilities):
    return 5 if total_assets > total_liabilities else 0

def calculate_balance_sheet_score(data):
    """
    Input: dict with relevant balance sheet fields
    Output: balance sheet score (max 25)
    """
    score = 0
    score += debt_to_equity_score(data['total_debt'], data['total_equity'])
    score += fcf_vs_capex_score(data['free_cash_flow'], data['capex'])
    score += fat_score(data['revenue'], data['fixed_assets'])
    score += working_capital_score(data['current_assets'], data['current_liabilities'])
    score += asset_vs_liability_score(data['total_assets'], data['total_liabilities'])
    return score
