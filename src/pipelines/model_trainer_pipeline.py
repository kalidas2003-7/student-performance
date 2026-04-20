from src.components.model_trainer import ModelTrainer
from src.config import DataPreprocessingConfig


def run_model_training():
    config = DataPreprocessingConfig()
    trainer = ModelTrainer(config)

    model = trainer.train()

    return model


if __name__ == "__main__":
    run_model_training()