# Insurance Cost Modeling & Risk Classification System

## Project Motivation

Healthcare affordability is a critical financial issue affecting individuals and communities.  
This project builds an interpretable statistical modeling pipeline to analyze key drivers of annual insurance costs and translate them into accessible financial risk insights.

The system demonstrates reproducible analysis, bias-aware modeling, and responsible AI integration.

---

## Features

- Reproducible raw → clean → model pipeline
- Log-linear regression with smearing bias correction
- Risk categorization (Low / Medium / High)
- Input validation and edge-case handling
- Command-line working prototype
- Unit testing with pytest
- LLM-assisted documentation (validated)

---

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Data Source

Medical Cost Personal Dataset (Kaggle)
Public synthetic dataset representing national insurance pricing patterns.

## Limitations

- National dataset; not region-specific
- Predictive, not causal
- Educational prototype; not financial advice
- Simplified feature set

## Known Future Improvements

- Web-based dashboard
- Cross-validation
- Fairness auditing
- Model comparison