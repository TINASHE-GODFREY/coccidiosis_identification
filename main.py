from classifier import logger
from classifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline


# douing data ingestion from main 
STAGE_NAME = "Data Ingestion Stage"

try:
        logger.info(f">>>>stage {STAGE_NAME}  started<<<<")
        data_ingestion=DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<< \n\n x======x ")

except Exception as e:
        logger.exception(e)
        raise e