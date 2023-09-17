


#using logger defined in __init__ of the end_to_end_mlops 
from end_to_end_mlops import logger

from end_to_end_mlops.pipeline.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f"********** Stage {STAGE_NAME} has been started **********")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f"********** Stage {STAGE_NAME} has been finished \n\n **********")
except Exception as e:
    logger.exception(e)
    raise e
