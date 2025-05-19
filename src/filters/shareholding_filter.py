# filters/shareholding_filter.py

def is_promoter_strong(promoter_holding):
    if promoter_holding >= 75:
        return 5
    elif promoter_holding >= 65:
        return 3
    else:
        return 0

def is_fii_dii_absent(fii, dii):
    if fii == 0 and dii == 0:
        return 5
    elif fii < 1 and dii < 1:
        return 2
    else:
        return 0

def is_public_shareholding_small(public_count):
    if public_count < 2500:
        return 5
    elif public_count < 5000:
        return 2
    else:
        return 0

def calculate_shareholding_score(stock_data):
    """
    Input: dict with promoter_holding, fii_holding, dii_holding, public_shareholders_count
    Output: shareholding score (max 15)
    """
    score = 0
    score += is_promoter_strong(stock_data['promoter_holding'])
    score += is_fii_dii_absent(stock_data['fii_holding'], stock_data['dii_holding'])
    score += is_public_shareholding_small(stock_data['public_shareholders_count'])
    return score
