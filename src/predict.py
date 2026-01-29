import numpy as np
import pandas as pd

def predict_insurance_cost(model, user_input: dict):
    """
    Generate bias-corrected insurance cost prediction
    using Duan's smearing estimator.
    """

    df = pd.DataFrame([user_input])
    features = model.model.exog_names
    df = df.reindex(columns=features, fill_value=0)

    # Log prediction
    log_pred = model.predict(df)[0]

    # Smearing factor
    residuals = model.resid
    smearing_factor = np.mean(np.exp(residuals))

    # Bias-corrected prediction
    cost_pred = np.exp(log_pred) * smearing_factor

    return {
        "predicted_log_cost": float(log_pred),
        "predicted_annual_cost": float(cost_pred),
        "smearing_factor": float(smearing_factor)
    }
