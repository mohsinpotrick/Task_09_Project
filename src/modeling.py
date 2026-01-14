import pandas as pd
import statsmodels.api as sm

def train_linear_model(df: pd.DataFrame, target: str = "charges"):
    """
    Train interpretable linear regression model.
    Handles boolean dummy variables safely.
    """

    y = df[target].astype(float)

    X = df.drop(columns=[target])

    # Convert booleans → int
    X = X.apply(lambda col: col.astype(int) if col.dtype == "bool" else col)

    # Keep numeric only
    X = X.select_dtypes(include=["number"]).astype(float)

    X = sm.add_constant(X, has_constant="add")

    model = sm.OLS(y, X).fit()
    return model
