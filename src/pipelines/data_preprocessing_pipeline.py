from src.components.data_preprocessing import DataPreprocessing
from src.config import DataPreprocessingConfig


def run_data_preprocessing():
    config = DataPreprocessingConfig()
    preprocessing = DataPreprocessing(config)

    X, y = preprocessing.preprocess()

    return X, y


if __name__ == "__main__":
    run_data_preprocessing()