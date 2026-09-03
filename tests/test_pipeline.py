import sys

sys.path.append("src")

from analysis import clean_data
from analysis import create_groups
from analysis import run_analysis

from fixtures import create_synthetic_data


def test_cleaning():

    df = create_synthetic_data()

    cleaned = clean_data(df)

    # All 6 records should be valid
    assert len(cleaned) == 6

    # Exam scores must be between 0 and 100
    assert cleaned["exam_score"].between(0, 100).all()

    # Study hours must not be negative
    assert (cleaned["study_hours"] >= 0).all()


def test_group_creation():

    df = create_synthetic_data()

    cleaned = clean_data(df)

    grouped = create_groups(cleaned)

    # Group column must exist
    assert "group" in grouped.columns

    # Both groups must exist
    assert set(grouped["group"].unique()) == {
        "exposed",
        "comparator"
    }


def test_analysis_contract():

    df = create_synthetic_data()

    cleaned = clean_data(df)

    grouped = create_groups(cleaned)

    results = run_analysis(grouped)

    expected_keys = {
        "exposed_n",
        "comparator_n",
        "exposed_mean",
        "comparator_mean",
        "mean_difference",
        "welch_t_statistic",
        "welch_p_value",
        "mann_whitney_p_value"
    }

    # Check expected output fields
    assert set(results.keys()) == expected_keys

    # Both groups must contain observations
    assert results["exposed_n"] > 0
    assert results["comparator_n"] > 0