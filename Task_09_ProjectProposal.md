# Project Title

**Health Insurance Costs and Financial Planning Risk: A Data-Driven Framework with Community-Level Implications for Syracuse**



## Project Title and Summary

Health insurance expenses are a significant and often unpredictable component of household financial planning. This project analyzes a national health insurance cost dataset to identify the primary drivers of insurance charges and financial risk at the individual and household level. Using statistical analysis and interpretable modeling techniques, the project will quantify how factors such as age, family size, health indicators, and smoking status influence insurance costs. Syracuse Open Data will be used only as a contextual extension, allowing findings from the primary analysis to be interpreted through the lens of local demographic patterns and community needs. The final deliverable will provide educational insights that support financial planning, health literacy, and policy discussion without relying on Syracuse data as a primary analytical input.



## Problem Statement

Households across the United States face increasing pressure from rising health insurance costs, making financial planning more complex and uncertain. While many public datasets capture demographic or health-related information, fewer resources clearly explain which factors most strongly drive insurance costs and how these risks should be understood by non-technical audiences. As a result, residents, community organizations, and policymakers often lack accessible, data-driven insights that translate insurance cost structures into practical financial planning considerations.

This project addresses the question: **What are the dominant drivers of health insurance costs, and how can these insights inform community-level financial planning and health literacy efforts?** The primary audience includes individuals seeking to understand insurance cost dynamics, nonprofit organizations focused on financial education, and public-sector stakeholders interested in the broader implications of insurance affordability. Syracuse Open Data is incorporated only at the recommendation stage, helping frame how nationally observed insurance cost drivers may be relevant to Syracuse residents and organizations, without treating local data as predictive or primary evidence.



## Data Sources

### Primary Analytical Dataset (External)

**Medical Cost Personal Dataset (Kaggle)**

- **Variables:** age, sex, BMI, number of children, smoking status, region, insurance charges  
- **Strengths:** Clean, well-documented, widely used for insurance cost analysis and modeling  
- **Limitations:** Synthetic/national scope; does not represent Syracuse specifically; limited health detail

### Contextual and Interpretive Data (Non-Primary)

**Syracuse Open Data (Selected Demographic Indicators)**

- Used only to contextualize findings and discuss potential local relevance  
- No record-level merging or predictive use  
- **Limitations:** Aggregate-level data, not suitable for individual inference

All conclusions will clearly distinguish analytical results from contextual interpretation.



## Technical Approach

The analysis will begin with comprehensive exploratory data analysis (EDA) of the insurance dataset using Python and Pandas. This phase will assess distributions, missing values, and relationships among variables, with a particular focus on identifying which features are most strongly associated with insurance charges. Visualization techniques such as box plots, stratified distributions, and correlation matrices will be used to surface key patterns. Interpretable statistical models, including linear regression and feature importance analysis, will be applied to quantify the relative contribution of each factor.

Large Language Models (LLMs) will be integrated as analytical support tools to assist in interpreting and communicating results. LLMs will be used to generate multiple narrative explanations of model outputs, translate statistical findings into plain-language financial planning insights, and surface potential framing biases. All LLM-generated content will be validated against ground-truth calculations and documented using prompt engineering and validation techniques developed in prior research tasks. Syracuse Open Data will be referenced only during the recommendation phase to illustrate how observed cost drivers may intersect with local demographic trends.



## Deliverable Description

The final deliverable will be a standalone analytical report and interactive visualization dashboard focused on insurance cost drivers and financial planning risk. The dashboard will allow users to explore how insurance charges vary by key factors and view explanatory visualizations. A dedicated section will translate these findings into community-level recommendations, using Syracuse Open Data solely to contextualize potential relevance for local residents and organizations. The deliverable will be explicitly educational and exploratory, avoiding personalized predictions or prescriptive advice.



## Success Criteria

- Clear, statistically supported identification of insurance cost drivers  
- Transparent separation between primary analysis and local contextual interpretation  
- Ethical and validated use of LLM-assisted narrative generation  
- Accessible communication of complex financial concepts to non-technical audiences  
- A polished, reproducible project suitable for public sharing and portfolio use



## Timeline

**Weeks 1–2**  
Finalize proposal and dataset selection

**Weeks 3–4**  
Data acquisition and exploratory data analysis

**Weeks 5–7**  
Statistical modeling and interpretability analysis

**Weeks 8–9**  
LLM-assisted narrative generation and validation

**Weeks 10–11**  
Dashboard and report development

**Weeks 12–13**  
Refinement, documentation, and presentation preparation



## Risks and Mitigations

- **Misinterpretation of national data as local prediction**  
  *Mitigation:* Clear disclaimers and separation of analysis vs. context

- **Overgeneralization of cost drivers**  
  *Mitigation:* Conservative language and uncertainty communication

- **Narrative bias introduced by LLMs**  
  *Mitigation:* Prompt auditing and validation against statistical results

