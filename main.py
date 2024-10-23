from classifier import logger
from classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline



#calling stage 1 pipeline
# data ingestion
STAGE_NAME = "Data Ingestion Stage"

try:
        logger.info(f">>>>stage {STAGE_NAME}  started<<<<")
        data_ingestion=DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<< \n\n x======x ")

except Exception as e:
        logger.exception(e)
        raise e


#calling stage 2 pipeline
#prepare base model
if __name__== "__main__":
    try:
        logger.info(f">>>>stage {STAGE_NAME}  started<<<<")
        prepare_base_model=PrepareBaseModelTrainingPipeline()
        prepare_base_model.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<< \n\n x======x ")

    except Exception as e:
        logger.exception(e)
        raise e