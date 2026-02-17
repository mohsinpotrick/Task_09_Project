## System Architecture

### Data Flow

Raw Data (CSV)
→ Data Cleaning (src/preprocessing.py)
→ Feature Engineering
→ Log Transformation
→ Linear Regression Model (statsmodels)
→ Smearing Bias Correction
→ Risk Categorization
→ CLI Output

### Design Decisions

- Log-linear model used due to skewed insurance cost distribution
- Smearing estimator applied to correct retransformation bias
- Modular structure separates validation, modeling, and prediction
- Unit tests ensure reproducibility

### Dependencies

- pandas
- numpy
- statsmodels
- pytest

### Current Status

- Core modeling functional
- CLI operational
- QA tests implemented
- Ready for refinement and documentation polishing