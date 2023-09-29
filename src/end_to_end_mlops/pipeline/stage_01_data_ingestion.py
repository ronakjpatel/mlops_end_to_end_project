from end_to_end_mlops.config.configuration import ConfigurationManager
from end_to_end_mlops.components.data_ingestion import DataIngestion
from end_to_end_mlops import logger

STAGE_NAME = "DATA INGESTION STAGE"

class DataIngestionPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self)->None:
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
  
  
if __name__ == '__main__':
    
    try:
        logger.info(f"********** Stage {STAGE_NAME} has been started **********")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f"********** Stage {STAGE_NAME} has been finished \n\n **********")
    except Exception as e:
        logger.exception(e)
        raise e
    
    
    