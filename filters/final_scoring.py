# filters/final_scoring.py

def calculate_final_score(scores_dict):
    """
    scores_dict keys:
      - shareholding
      - balance_sheet
      - sector_penalty (negative or zero)
      - policy_bonus
      - peer_comparison
      - core_financials
      - quarterly_trend

    Apply weights if desired and sum.

    Returns final score (float).
    """

    weights = {
        "shareholding": 1.0,
        "balance_sheet": 1.0,
        "sector_penalty": 1.0,
        "policy_bonus": 1.0,
        "peer_comparison": 1.0,
        "core_financials": 1.0,
        "quarterly_trend": 1.0
    }

    final_score = 0
    for key, weight in weights.items():
        final_score += scores_dict.get(key, 0) * weight

    return final_score
