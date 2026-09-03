import pandas as pd
import numpy as np
from scipy.stats import ttest_ind, mannwhitneyu


def clean_data(df):
    df = df.copy()

    df = df.dropna(subset=["study_hours", "exam_score"])

    df = df[df["study_hours"] >= 0]

    df = df[
        (df["exam_score"] >= 0) &
        (df["exam_score"] <= 100)
    ]

    return df


def create_groups(df):
    df = df.copy()

    df["group"] = (df["study_hours"] >= 3).map({
        True: "exposed",
        False: "comparator"
    })

    return df


def run_analysis(df):

    exposed = df.loc[
        df["group"] == "exposed",
        "exam_score"
    ]

    comparator = df.loc[
        df["group"] == "comparator",
        "exam_score"
    ]

    # Welch t-test
    t_statistic, p_value = ttest_ind(
        exposed,
        comparator,
        equal_var=False
    )

    # Mean difference
    mean_difference = (
        exposed.mean() - comparator.mean()
    )

    # Mann-Whitney U test
    u_statistic, mann_whitney_p = mannwhitneyu(
        exposed,
        comparator,
        alternative="two-sided"
    )

    # Standard error
    se = np.sqrt(
        exposed.var(ddof=1) / len(exposed)
        +
        comparator.var(ddof=1) / len(comparator)
    )

    # 95% approximate CI
    ci_lower = mean_difference - 1.96 * se
    ci_upper = mean_difference + 1.96 * se

    results = {

        "exposed_n": len(exposed),

        "comparator_n": len(comparator),

        "exposed_mean": exposed.mean(),

        "comparator_mean": comparator.mean(),

        "mean_difference": mean_difference,

        "ci_lower": ci_lower,

        "ci_upper": ci_upper,

        "welch_t_statistic": t_statistic,

        "welch_p_value": p_value,

        "mann_whitney_p_value": mann_whitney_p

    }

    return results