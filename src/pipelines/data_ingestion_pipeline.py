from src.components.data_ingestion import DataIngestion

ingestion = DataIngestion()
ingestion.download_data()
ingestion.extract_data()