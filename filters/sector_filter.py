# filters/sector_filter.py

# List of sectors to **exclude entirely**
EXCLUDED_SECTORS = {
    "Airlines", "Telecom", "PSU Banks", "Hotels", "Shipping", "Oil Marketing"
}

# Optional: sectors that are **weak or out of favor**
WEAK_SECTOR_PENALTY = {
    "Real Estate": -3,
    "FMCG": -2,
    "Media": -2,
    "IT Services": -2,
    "Construction": -3
}

def is_sector_allowed(sector_name):
    """
    Check if the stock should be excluded based on sector.
    Returns False if sector is in excluded list.
    """
    return sector_name not in EXCLUDED_SECTORS

def get_sector_penalty(sector_name):
    """
    Returns penalty (0 or negative) based on weak sector list.
    """
    return WEAK_SECTOR_PENALTY.get(sector_name, 0)
