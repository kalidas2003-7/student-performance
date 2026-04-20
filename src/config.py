from dataclasses import dataclass
import os

@dataclass
class DataConfig:
    dataset_name: str = "spscientist/students-performance-in-exams"
    download_dir: str = "data"
    file_name: str = "students-performance-in-exams.zip"


@dataclass
class DataPreprocessingConfig:
    # Input data
    raw_data_path: str = os.path.join("data", "StudentsPerformance.csv")

    # Output paths
    processed_data_dir: str = "artifacts"
    X_processed_path: str = os.path.join(processed_data_dir, "X_processed.csv")
    y_path: str = os.path.join(processed_data_dir, "y.csv")

    # Saved objects
    preprocessor_path: str = os.path.join(processed_data_dir, "preprocessor.pkl")

    # Target column
    target_column: str = "average_score"

    # Score columns (to create target)
    score_columns: tuple = ("math score", "reading score", "writing score")