# filters/policy_adjuster.py

# These sectors are expected to benefit from policy trends
POLICY_FAVORED_SECTORS = {
    "Renewable Energy": 5,
    "Electric Vehicles": 5,
    "Railways": 4,
    "Defense": 4,
    "Capital Goods": 3,
    "Infra": 3,
    "Manufacturing": 3,
    "Semiconductors": 4,
    "Green Hydrogen": 5
}

def get_policy_bonus(sector_name):
    """
    Returns a policy bonus score (0-5) based on sector alignment with upcoming reforms.
    """
    return POLICY_FAVORED_SECTORS.get(sector_name, 0)
