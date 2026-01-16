import pandas as pd
from src.modeling import train_linear_model

def test_model_executes():
    df = pd.read_csv("data/insurance_clean.csv")
    model = train_linear_model(df)
    assert model.rsquared > 0
