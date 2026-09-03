import sys
import os
import pandas as pd

# Allow Python to find analysis.py
sys.path.append(
    os.path.dirname(os.path.abspath(__file__))
)

from analysis import clean_data
from analysis import create_groups
from analysis import run_analysis


def run_pipeline(input_file, processed_file, results_file):

    print("Starting research pipeline...")

    # -----------------------------------------
    # 1. Load raw data
    # -----------------------------------------

    print("\n[1] Loading raw data...")

    df = pd.read_csv(input_file)

    print(f"Raw records: {len(df)}")

    # -----------------------------------------
    # 2. Clean data
    # -----------------------------------------

    print("\n[2] Cleaning data...")

    cleaned_df = clean_data(df)

    print(f"Records after cleaning: {len(cleaned_df)}")

    # -----------------------------------------
    # 3. Create exposure groups
    # -----------------------------------------

    print("\n[3] Creating study groups...")

    grouped_df = create_groups(cleaned_df)

    print(
        grouped_df["group"].value_counts()
    )

    # -----------------------------------------
    # 4. Run statistical analysis
    # -----------------------------------------

    print("\n[4] Running statistical analysis...")

    results = run_analysis(grouped_df)

    # -----------------------------------------
    # 5. Save processed data
    # -----------------------------------------

    print("\n[5] Saving processed data...")

    grouped_df.to_csv(
        processed_file,
        index=False
    )

    # -----------------------------------------
    # 6. Save results
    # -----------------------------------------

    print("\n[6] Saving analysis results...")

    results_df = pd.DataFrame([results])

    results_df.to_csv(
        results_file,
        index=False
    )

    # -----------------------------------------
    # 7. Display results
    # -----------------------------------------

    print("\n========== RESULTS ==========")

    for key, value in results.items():
        print(f"{key}: {value}")

    print("\nPipeline completed successfully!")


if __name__ == "__main__":

    run_pipeline(
        "data/raw/students.csv",
        "data/processed/processed_data.csv",
        "reports/results.csv"
    )