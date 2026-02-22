import pandas as pd
import numpy as np
from src.modeling import train_linear_model
from src.predict import predict_insurance_cost

print("\n=== Insurance Cost Estimator ===\n")

try:
    df = pd.read_csv("/workspaces/Task_09_Project/data/insurance_clean.csv")

    df["log_charges"] = np.log(df["charges"])
    model = train_linear_model(df.drop(columns=["charges"]), target="log_charges")

    user = {
        "const": 1,
        "age": 40,
        "sex": 0,
        "bmi": 28,
        "children": 2,
        "smoker": 0,
        "region_northwest": 0,
        "region_southeast": 1,
        "region_southwest": 0
    }

    prediction = predict_insurance_cost(model, user)

    print("Estimated Annual Cost: "
          f"${prediction['predicted_annual_cost']:.2f}")
    print("Risk Category:", prediction["risk_category"])

except Exception as e:
    print("\nAn error occurred:")
    print(str(e))