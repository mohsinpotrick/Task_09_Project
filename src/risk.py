def cost_band(cost):
    """
    Categorize predicted insurance cost into risk bands.
    """

    if cost < 8000:
        return "Low Risk"
    elif cost < 20000:
        return "Medium Risk"
    else:
        return "High Risk"