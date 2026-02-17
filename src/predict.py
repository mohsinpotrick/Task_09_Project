import numpy as np
import pandas as pd
from src.validation import validate_input
from src.risk import cost_band


def predict_insurance_cost(model, user_input):
    """
    Predict insurance cost using log-linear model
    and apply smearing correction.
    """

    # Validate input
    validate_input(user_input)

    # Convert to DataFrame
    import pandas as pd
    user_df = pd.DataFrame([user_input])

    # Predict log cost
    log_pred = model.predict(user_df)[0]

    # Smearing correction
    residuals = model.resid
    smearing_factor = np.mean(np.exp(residuals))

    cost_pred = np.exp(log_pred) * smearing_factor

    return {
        "predicted_log_cost": float(log_pred),
        "predicted_annual_cost": float(cost_pred),
        "smearing_factor": float(smearing_factor),
        "risk_category": cost_band(cost_pred)
    }