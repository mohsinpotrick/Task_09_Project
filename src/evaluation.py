import pandas as pd

def get_feature_importance(model) -> pd.Series:
    """
    Return sorted model coefficients.
    """
    return model.params.sort_values()
