
Paste:

```markdown
# Technical Documentation

## Architecture Overview

Raw CSV
→ Preprocessing
→ Feature Encoding
→ Log Transformation
→ OLS Regression
→ Smearing Bias Correction
→ Risk Categorization
→ CLI Output

---

## Development Setup

Python 3.12 recommended.

Install dependencies:

pip install -r requirements.txt

---

## Code Organization

src/
- data_loader.py
- preprocessing.py
- modeling.py
- predict.py
- validation.py
- risk.py
- evaluation.py

tests/
- test_modeling.py

main.py – CLI entry point

---

## API Documentation

### train_linear_model(df, target)
Returns fitted OLS model.

### predict_insurance_cost(model, user_input)
Returns:
- predicted_log_cost
- predicted_annual_cost
- smearing_factor
- risk_category

### validate_input(user_input)
Raises ValueError if invalid.

### cost_band(cost)
Returns risk label.

---

## Testing

Run:

pytest tests/

All tests must pass before deployment.

---

## Deployment Guide

Currently CLI-based.

Future deployment:
- Streamlit web interface
- Docker containerization
- Cloud hosting