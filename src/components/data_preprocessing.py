import os
import pandas as pd
import pickle

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

from src.config import DataPreprocessingConfig


class DataPreprocessing:
    def __init__(self, config: DataPreprocessingConfig):
        self.config = config

    def preprocess(self):
        # 1. Load data
        df = pd.read_csv(self.config.raw_data_path)

        # 2. Create target
        df[self.config.target_column] = df[list(self.config.score_columns)].mean(axis=1)

        # 3. Split X and y
        X = df.drop(columns=list(self.config.score_columns) + [self.config.target_column])
        y = df[self.config.target_column]

        # 4. Ensure output directory exists
        os.makedirs(self.config.processed_data_dir, exist_ok=True)

        # 5. Define categorical columns
        categorical_cols = X.select_dtypes(include="object").columns.tolist()

        # 6. Preprocessor
        preprocessor = ColumnTransformer(
            transformers=[
                ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols)
            ],
            remainder="drop"
        )

        # 7. Fit + transform
        X_processed = preprocessor.fit_transform(X)

        # 8. Convert to dense if needed
        X_processed = X_processed.toarray() if hasattr(X_processed, "toarray") else X_processed

        # 9. Get feature names
        feature_names = preprocessor.get_feature_names_out()

        # 10. Convert to DataFrame
        X_processed_df = pd.DataFrame(X_processed, columns=feature_names)

        # 11. Save outputs
        X_processed_df.to_csv(self.config.X_processed_path, index=False)
        y.to_csv(self.config.y_path, index=False)

        with open(self.config.preprocessor_path, "wb") as f:
            pickle.dump(preprocessor, f)

        print("Preprocessing completed successfully.")

        return X_processed_df, y