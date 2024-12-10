from classifier import logger
from classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from classifier.pipeline.stage_03_training import ModelTrainingPipeline



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




STAGE_NAME= "Pepare base model "

try:
        logger.info(f">>>>stage {STAGE_NAME}  started<<<<")
        prepare_base_model=PrepareBaseModelTrainingPipeline()
        prepare_base_model.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<< \n\n x======x ")

except Exception as e:
        logger.exception(e)
        raise e





STAGE_NAME= "Training"

try:
        logger.info(f">>>>stage {STAGE_NAME}  started<<<<")
        model_trainer=ModelTrainingPipeline()
        model_trainer.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<< \n\n x======x ")

except Exception as e:
        logger.exception(e)
        raise e







if __name__== "__main__":
    try:
        logger.info(f">>>>stage {STAGE_NAME}  started<<<<")
        prepare_base_model=PrepareBaseModelTrainingPipeline()
        prepare_base_model.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<< \n\n x======x ")

    except Exception as e:
        logger.exception(e)
        raise e