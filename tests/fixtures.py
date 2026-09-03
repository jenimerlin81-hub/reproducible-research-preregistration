import pandas as pd


def create_synthetic_data():
    """
    Create fake data for testing the analysis pipeline.
    """

    data = {
        "student_id": [1, 2, 3, 4, 5, 6],
        "study_hours": [4, 2, 5, 1, 3, 2],
        "exam_score": [80, 60, 85, 55, 78, 62]
    }

    return pd.DataFrame(data)