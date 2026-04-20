from kaggle.api.kaggle_api_extended import KaggleApi
import os
import zipfile

from src.config import DataConfig
from src.utils.common import create_directory


class DataIngestion:
    def __init__(self):
        self.config = DataConfig()

    def download_data(self):
        create_directory(self.config.download_dir)

        api = KaggleApi()
        api.authenticate()

        api.dataset_download_files(
            self.config.dataset_name,
            path=self.config.download_dir,
            unzip=False
        )

    def extract_data(self):
        zip_path = os.path.join(
            self.config.download_dir,
            self.config.file_name
        )

        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(self.config.download_dir)