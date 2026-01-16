## Development Report  

### Project Context

The development work finished during Weeks 5 and 6 of the Syracuse Open Data Civic Project is compiled in this document. This phase focused on implementing interpretable statistical models, establishing quality assurance procedures in line with professional data science norms, and moving from exploratory analysis into a reproducible modeling pipeline.

Syracuse Open Data is only used for contextual interpretation, not primary modeling, as the research examines national health insurance cost data to uncover important determinants of financial risk and insurance charges.

---

### 1. Modeling Pipeline Overview

A reproducible analysis pipeline was implemented with clear separation between:

- **Data acquisition** (external dataset ingestion)
- **Data preprocessing** (cleaning and encoding)
- **Statistical modeling**
- **Evaluation and interpretation**
- **Quality assurance**

All modeling logic is encapsulated in reusable Python modules under the `src/` directory and executed through Jupyter notebooks for transparency and documentation.

---

### 2. Model Selection and Rationale

### Baseline Model
An ordinary least squares (OLS) linear regression model was selected due to its:
- Interpretability
- Alignment with financial planning use cases
- Suitability for explaining marginal cost drivers

### Log-Transformed Model
Insurance charges exhibit strong right skew. To address this:

- A log transformation of the target variable (`charges`) was applied
- The transformed model improves residual behavior and interpretability
- Coefficients can be interpreted as approximate percentage changes in cost

This transformation aligns with standard econometric practices for cost modeling.

---

### 3. Final Model Specification

**Target Variable**
- `log_charges = log(charges)`

**Predictor Variables**
- Age
- Sex (binary encoded)
- Body Mass Index (BMI)
- Number of children
- Smoking status
- Region indicators (one-hot encoded)

All predictors were validated to ensure numeric types prior to modeling.

---

## 4. Model Summary (Log-Transformed)

Key outputs from the fitted model include:

- Statistically significant coefficients for smoking status, age, and BMI
- Strong overall explanatory power (R² substantially greater than zero)
- Improved residual symmetry compared to the raw-cost model

Coefficient estimates were converted into **percentage impact interpretations** using:

## 3. Final Model Specification

**Target Variable**
- `log_charges = log(charges)`

**Predictor Variables**
- Age
- Sex (binary encoded)
- Body Mass Index (BMI)
- Number of children
- Smoking status
- Region indicators (one-hot encoded)

All predictors were validated to ensure numeric types prior to modeling.

---

## 4. Model Summary (Log-Transformed)

Key outputs from the fitted model include:

- Statistically significant coefficients for smoking status, age, and BMI
- Strong overall explanatory power (R² substantially greater than zero)
- Improved residual symmetry compared to the raw-cost model

Coefficient estimates were converted into **percentage impact interpretations** using:

percent_change ≈ (exp(coefficient) − 1) × 100


This enables direct translation into financial planning insights (e.g., “smoking is associated with over 100% higher insurance costs, holding other factors constant”).

---

### 5. Model Diagnostics

Several diagnostic checks were performed:

- **Residual distribution**: approximately symmetric around zero
- **Predicted vs. actual plots**: show reasonable alignment without severe heteroskedasticity
- **Model comparison**: log-transformed model demonstrates superior stability relative to raw-cost regression

These diagnostics support the appropriateness of the modeling approach.

---

## 6. Architecture and Design Decisions

### System Architecture

Raw Data

↓

Preprocessing (cleaning, encoding)

↓

Model Training (OLS / log-OLS)

↓

Evaluation & Interpretation

↓

Narrative & Visualization Outputs

#
### Key Design Decisions
- Prioritized interpretability over complex predictive models
- Avoided use of Syracuse data as a modeling input to prevent false local inference
- Centralized modeling logic in reusable Python modules
- Used notebooks only for orchestration and documentation

---

### 7. Quality Assurance Implementation

#### Unit Testing

A unit test was implemented using `pytest` to validate model execution.

**Test Location**

tests/test_modeling.py


**Test Objective**
- Ensure the regression model runs successfully on cleaned data
- Confirm that the model produces a meaningful explanatory result (R² > 0)

**Test Code**
```python
import pandas as pd
from src.modeling import train_linear_model

def test_model_executes():
    df = pd.read_csv("data/processed/insurance_clean.csv")
    model = train_linear_model(df)
    assert model.rsquared > 0
```

**Test Execution**

Tests are executed from the project root using:

```python
pytest tests/
```


A `conftest.py` file was added to manage Python import paths in a reproducible, standards-compliant manner.

All tests passed successfully.


### 8. Limitations Identified

- The dataset is national and synthetic in nature; results are not predictive for Syracuse residents

- Insurance pricing mechanisms may include unobserved variables not captured in the data

- Linear models capture marginal effects but not complex nonlinear interactions

These limitations are explicitly documented to prevent overinterpretation.