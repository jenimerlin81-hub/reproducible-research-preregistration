# reproducible-research-preregistration
# Reproducible Research Question & Analysis Preregistration

## Project Overview

This project demonstrates a reproducible research workflow where a research question and analysis plan are defined before inspecting outcome patterns.

The project uses student study-hours and exam-score data to compare students who study at least 3 hours per day with students who study less than 3 hours per day.

## Research Question

Among students observed during one academic semester, do students who study at least 3 hours per day have higher exam scores than students who study less than 3 hours per day?

## Hypotheses

### Null Hypothesis (H0)

There is no meaningful difference in average exam scores between the two study-hour groups.

### Alternative Hypothesis (H1)

Students who study at least 3 hours per day have higher average exam scores.

## Study Design

- Population: Students
- Exposure: Study time of at least 3 hours per day
- Comparator: Study time below 3 hours per day
- Outcome: Exam score
- Observation Window: One academic semester

## Analysis

The project performs:

- Data cleaning
- Study group classification
- Welch's independent two-sample t-test
- Mean difference calculation
- 95% confidence interval
- Mann–Whitney U robustness check

## Project Structure

```text
data/
├── raw/
├── interim/
└── processed/

notebooks/

src/
├── analysis.py
└── pipeline.py

tests/
├── fixtures.py
└── test_pipeline.py

preregistration/
└── preregistration.md

reports/
└── results.csv

requirements.txt
README.md
