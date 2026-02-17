import pandas as pd
from src.modeling import train_linear_model
from src.predict import predict_insurance_cost

# Load cleaned dataset
df = pd.read_csv("/workspaces/Task_09_Project/data/insurance_clean.csv")

# Train log model
import numpy as np
df["log_charges"] = np.log(df["charges"])

model = train_linear_model(df.drop(columns=["charges"]), target="log_charges")

# Example user input
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

print("\nInsurance Cost Estimate")
print("---------------------------")
print(f"Estimated Annual Cost: ${prediction['predicted_annual_cost']:.2f}")
print(f"Risk Category: {prediction['risk_category']}")