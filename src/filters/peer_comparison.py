# filters/peer_comparison.py

def pe_score(stock_pe, sector_pe):
    if stock_pe == 0 or sector_pe == 0:
        return 0
    if stock_pe < sector_pe * 0.75:
        return 5
    elif stock_pe < sector_pe:
        return 3
    return 0

def roce_score(stock_roce, sector_roce):
    if stock_roce > sector_roce * 1.25:
        return 5
    elif stock_roce > sector_roce:
        return 3
    return 0

def roe_score(stock_roe, sector_roe):
    if stock_roe > sector_roe * 1.25:
        return 5
    elif stock_roe > sector_roe:
        return 3
    return 0

def calculate_peer_score(stock_metrics, sector_metrics):
    """
    Input:
      stock_metrics: dict with 'pe', 'roce', 'roe'
      sector_metrics: dict with 'pe', 'roce', 'roe'
    Output:
      score (max 15)
    """
    score = 0
    score += pe_score(stock_metrics['pe'], sector_metrics['pe'])
    score += roce_score(stock_metrics['roce'], sector_metrics['roce'])
    score += roe_score(stock_metrics['roe'], sector_metrics['roe'])
    return score
