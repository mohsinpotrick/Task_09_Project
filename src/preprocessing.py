import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and encode insurance dataset for modeling.
    Ensures all features are numeric for statsmodels.
    """
    df = df.copy()

    # Encode binary categorical variables
    df["smoker"] = df["smoker"].map({"yes": 1, "no": 0})
    df["sex"] = df["sex"].map({"male": 1, "female": 0})

    # One-hot encode region
    df = pd.get_dummies(df, columns=["region"], drop_first=True)

    # Force all columns to numeric
    df = df.apply(pd.to_numeric)

    return df
