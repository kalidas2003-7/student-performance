import os
import pickle
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

from src.config import DataPreprocessingConfig


class ModelTrainer:
    def __init__(self, config: DataPreprocessingConfig):
        self.config = config

    def train(self):
        # 1. Load processed data
        X = pd.read_csv(self.config.X_processed_path)
        y = pd.read_csv(self.config.y_path).squeeze()

        # 2. Train-test split
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # 3. Initialize model
        model = RandomForestRegressor(n_estimators=100, random_state=42)

        # 4. Train
        model.fit(X_train, y_train)

        # 5. Evaluate
        y_pred = model.predict(X_test)

        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)

        print(f"R2 Score: {r2}")
        print(f"MAE: {mae}")

        # 6. Save model
        model_path = os.path.join(self.config.processed_data_dir, "model.pkl")

        with open(model_path, "wb") as f:
            pickle.dump(model, f)

        print(f"\nModel saved at: {model_path}")

        return model