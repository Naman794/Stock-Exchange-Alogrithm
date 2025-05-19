# filters/quarterly_trend.py

def score_quarterly_growth(q1, q2, q3):
    """
    Scores 5 if Q1 < Q2 < Q3 (steady growth),
    3 if 2 out of 3 show growth,
    0 if inconsistent or decline.
    """
    growth_count = 0
    if q2 > q1:
        growth_count += 1
    if q3 > q2:
        growth_count += 1
    if q3 > q1:
        growth_count += 1

    if growth_count == 3:
        return 5
    elif growth_count == 2:
        return 3
    return 0

def calculate_quarterly_trend_score(stock):
    sales_score = score_quarterly_growth(
        stock['sales_q1'], stock['sales_q2'], stock['sales_q3']
    )
    profit_score = score_quarterly_growth(
        stock['profit_q1'], stock['profit_q2'], stock['profit_q3']
    )
    return sales_score + profit_score  # Max 10
