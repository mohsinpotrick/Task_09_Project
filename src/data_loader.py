import pandas as pd

def load_raw_data(path: str) -> pd.DataFrame:
    """
    Load raw insurance dataset.
    """
    return pd.read_csv(path)
