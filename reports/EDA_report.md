## EDA Report

### Data Acquisition
- Dataset: Medical Cost Personal Dataset
- Source: Kaggle
- URL: https://www.kaggle.com/datasets/mirichoi0218/insurance
- Access Method: Manual download (Kaggle)
- License: Public dataset for research/education


### Data Dictionary – Insurance Dataset

| Column | Description |
|------|------------|
| age | Age of primary beneficiary |
| sex | Gender of beneficiary |
| bmi | Body Mass Index |
| children | Number of dependents |
| smoker | Smoking status (yes/no) |
| region | Residential region |
| charges | Annual medical insurance charges |


### Data Limitations

- The dataset is national in scope and not Syracuse-specific
- No income, race, or detailed health history variables
- Charges reflect insurance billing, not out-of-pocket costs
- Cross-sectional snapshot — no time series analysis possible
- Potential bias: smoking status and BMI may reflect structural health inequities

These limitations restrict the analysis to **educational and exploratory insights**, not personalized or local prediction.

### Preliminary Findings

1. Smoking status is the strongest visible driver of insurance charges.
2. Insurance charges increase with age, though variance grows significantly among older individuals.
3. BMI shows a positive but non-linear relationship with charges.
4. Family size has a weaker effect compared to health-related variables.


### LLM Prompt:
"Summarize the primary drivers of insurance costs based on this dataset and explain them in plain language for a non-technical audience."


### LLM Output Validation:
- Smoking identified as major cost driver → Confirmed via boxplots and summary statistics
- Age identified as secondary factor → Confirmed via scatter plot
- Family size noted as moderate → Confirmed weaker variance impact

No contradictions observed between LLM narrative and ground-truth analysis.

### Bias Review:
- Avoid framing smoking or BMI as purely individual choices
- Emphasize structural health factors
- Use neutral, non-judgmental language
