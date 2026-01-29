## LLM Integration Documentation

### Purpose and Scope

Large Language Models (LLMs) were used conceptually as an assistive tool to
support interpretation, explanation, and documentation of statistical model
outputs. LLMs were not used for data processing, modeling, or prediction.
Instead, they were applied to improve clarity, accessibility, and narrative
quality of project deliverables.

This approach aligns with responsible AI use by ensuring that all quantitative
results remain grounded in verifiable statistical analysis.

---

### Intended LLM Use Cases

LLM assistance was applied in the following areas:

- Translating regression outputs into plain-language explanations  
- Drafting narrative descriptions of model behavior and limitations  
- Improving readability of technical documentation  
- Structuring civic-focused explanations for non-technical audiences  

At no point were LLMs used to generate numerical results or make analytical
decisions.

---

### Example Prompt Design

The following prompts were used to guide narrative refinement:


### Prompt 1: Model Interpretation

**Prompt**
> Explain the key drivers of insurance cost in a log-linear regression model
> using clear, non-technical language. Avoid causal claims and do not introduce
> any new numerical results.

**LLM Output**
The model suggests that certain personal characteristics are associated with
higher or lower insurance costs. Smoking status has the strongest relationship
with increased costs, followed by body mass index and age. These factors are
commonly linked to higher healthcare utilization, which may explain their
influence in the model. Other variables, such as region and number of children,
have smaller but still observable associations.

---

### Prompt 2: High Prediction Explanation

**Prompt**
> A model produced a high estimated insurance cost for a given individual.
> Explain why this might occur without implying an error or making individual
> guarantees.

**LLM Output**
A high estimated cost typically reflects a higher-risk profile rather than a
problem with the model. Certain characteristics, such as smoking or elevated
body mass index, are strongly associated with increased healthcare expenses in
the data used to train the model. When these factors are present together, the
model produces higher estimates to reflect increased relative risk.

---


### Prompt 3: Uncertainty Communication

**Prompt**
> Explain how to describe model uncertainty to a non-technical audience.

**LLM Output**
Model estimates are best understood as approximate ranges rather than exact
values. Because individual circumstances vary and no model captures every
factor, predictions include uncertainty. Presenting results as comparative or
illustrative helps avoid overconfidence and supports more responsible
interpretation.

-------

### Validation and Quality Control

All LLM-assisted outputs were validated using the following safeguards:

- Numerical values were cross-checked against model outputs  
- No new claims or inferences were introduced by the LLM  
- Language was reviewed to avoid overgeneralization or misleading precision  
- Explanations were compared directly with statistical summaries  

Any narrative content not supported by the underlying analysis was discarded.

---

### Limitations and Risk Mitigation

LLM-generated text may introduce interpretive bias or overconfidence if used
without validation. To mitigate this risk, the project limits LLM usage to
post-analysis communication tasks and explicitly avoids automated decision-making
or prediction generation.

---

### Conclusion

Instead of being an analytical tool, LLMs were utilized as a communication and documentation tool. This strategy maintains methodological integrity, transparency, and compliance with civic data ethics while improving accessibility and clarity.