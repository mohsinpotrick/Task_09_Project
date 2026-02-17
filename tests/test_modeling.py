import pandas as pd
from src.modeling import train_linear_model
from src.validation import validate_input
from src.risk import cost_band


def test_model_executes():
    df = pd.read_csv("/workspaces/Task_09_Project/data/insurance_clean.csv")
    model = train_linear_model(df)
    assert model.rsquared > 0


def test_validation():
    valid_input = {
        "age": 30,
        "bmi": 25,
        "children": 1,
        "smoker": 0,
        "sex": 1
    }
    assert validate_input(valid_input) == True


def test_risk_band():
    assert cost_band(5000) == "Low Risk"
    assert cost_band(15000) == "Medium Risk"
    assert cost_band(40000) == "High Risk"