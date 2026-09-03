# Reproducible Research Question & Analysis Preregistration

## 1. Research Question

Among students observed during one academic semester, do students who study at least 3 hours per day have higher exam scores than students who study less than 3 hours per day?

## 2. Population

The population consists of students included in the study dataset during one academic semester.

## 3. Exposure

The exposure is daily study time.

Students will be classified as:

* Exposed group: study_hours >= 3
* Comparator group: study_hours < 3

## 4. Comparator

The comparator group consists of students who study less than 3 hours per day.

## 5. Primary Outcome

The primary outcome is final exam score, measured from 0 to 100.

## 6. Observation Window

The observation window is one academic semester.

## 7. Hypotheses

### Null Hypothesis (H0)

There is no difference in mean exam score between students studying at least 3 hours per day and students studying less than 3 hours per day.

### Alternative Hypothesis (H1)

Students studying at least 3 hours per day have a higher mean exam score than students studying less than 3 hours per day.

## 8. Exclusion Rules

A record will be excluded if:

1. study_hours is missing.
2. exam_score is missing.
3. study_hours is negative.
4. exam_score is below 0.
5. exam_score is above 100.

No additional exclusion rules will be introduced after inspecting the outcome results.

## 9. Data Transformation

The original `study_hours` variable will be converted into a binary exposure variable:

* study_hours >= 3 → exposed
* study_hours < 3 → comparator

The `exam_score` variable will not be transformed.

## 10. Primary Statistical Test

The primary analysis will compare the mean exam scores between the exposed and comparator groups using an independent two-sample Welch's t-test.

The significance level will be:

alpha = 0.05

## 11. Effect Size

The primary effect size will be the difference in mean exam scores:

mean(exposed) - mean(comparator)

A 95% confidence interval will also be reported.

## 12. Robustness Checks

The following robustness checks will be performed:

1. Report the sample size of each group.
2. Check for missing values.
3. Perform a Mann–Whitney U test.
4. Repeat the analysis after removing study-hour values above the 99th percentile.

## 13. Missing Data

Records with missing values for `study_hours` or `exam_score` will be excluded from the primary analysis.

The number of excluded records will be reported.

## 14. Reproducibility

The analysis will be implemented using Python.

The required Python packages and their versions will be recorded in `requirements.txt`.

The analysis code will be stored in the `src/` directory.

## 15. Data-Blind Pipeline Check

Before analysing the outcome pattern of the dataset, the analysis pipeline will be tested using synthetic data.

The synthetic test will verify:

* Data cleaning
* Exposure group creation
* Statistical analysis
* Expected result fields
* Valid sample sizes

## 16. Expected Output Contract

The analysis pipeline must produce:

* exposed_n
* comparator_n
* exposed_mean
* comparator_mean
* mean_difference
* Welch t-statistic
* Welch p-value
* Mann–Whitney p-value

The processed dataset will be saved in:

`data/processed/`

The analysis results will be saved in:

`reports/`

## 17. Analysis Lock

The research question, hypotheses, exclusion rules, transformations, statistical tests, effect size, and robustness checks defined in this document will be fixed before inspecting outcome patterns in the final analysis.

Any later changes must be documented separately rather than silently replacing this preregistration.
