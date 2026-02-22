# Methodology Documentation

## Data Processing

1. Loaded raw insurance dataset
2. Encoded categorical variables
3. Converted boolean columns to numeric
4. Saved cleaned dataset
5. Applied log transformation to charges

---

## Analytical Approach

A log-linear Ordinary Least Squares (OLS) regression was used due to right-skewed cost distribution.

Model form:

log(charges) = β0 + β1(age) + β2(bmi) + β3(smoker) + ...

---

## Bias Correction

Predictions were retransformed using Duan's smearing estimator to correct log-scale bias.

This prevents systematic overestimation.

---

## LLM Usage

LLMs were used only for:
- Narrative drafting
- Interpretation explanation
- Uncertainty communication

All numerical outputs were validated manually.

---

## Statistical Methods

- OLS regression
- Log transformation
- Smearing estimator
- R² evaluation
- Residual diagnostics

---

## Limitations

- Synthetic dataset
- Limited features
- No interaction terms
- No cross-validation yet
- Not causal inference

---

## Ethical Considerations

- No automated decision-making
- No personal data
- Transparent modeling choices
- Explicit uncertainty communication