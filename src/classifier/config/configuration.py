from classifier.constants import *
import os;
from classifier.utils.common_functions import *
from classifier.entity.config_entity  import (DataIngestionConfig,PrepareBaseModelConfig, PrepareCallbacksConfig)


class ConfigurationManager:
    def __init__(
            self,
            config_filepath= CONFIG_FILE_PATH,
            parameters_filepath= PARAMETERS_FILE_PATH):
         
            self.config=read_yaml(config_filepath)
            self.parameters=read_yaml(parameters_filepath)

            create_dirctories([self.config.artifacts_roots])
         
            

    def get_data_ingestion_config(self) -> DataIngestionConfig:
          config=self.config.data_ingestion
          create_dirctories([config.root_dir])

          data_ingestion_config=DataIngestionConfig(
                root_dir=config.root_dir,
                source_url=config.source_url,
                local_datafiles=config.local_datafiles,
                unzip_dir= config.unzip_dir
                )

          return data_ingestion_config
    

    def get_prepare_base_model_config(self)-> PrepareBaseModelConfig:
          config=self.config.prepare_base_model

          create_dirctories([config.root_dir])

          prepare_base_model_config=PrepareBaseModelConfig(
                root_dir=Path(config.root_dir),
                base_model_path= Path(config.base_model_path),
                updated_base_model_path=Path(config.updated_base_model_path),
                parameter_image_size=self.parameters.IMAGE_SIZE,
                parameter_learning_rate=self.parameters.LEARNING_RATE,
                parameter_include_top=self.parameters.INCLUDE_TOP,
                parameter_weights=self.parameters.WEIGHTS,
                parameter_classes=self.parameters.CLASSES
          )

          return prepare_base_model_config
    def get_prepare_callbacks_config(self)-> PrepareCallbacksConfig:
        config=self.config.prepare_callbacks
        model_ckpt_dir= os.path.dirname(config.checkpoint_model_filepath)

        create_dirctories([
            Path(model_ckpt_dir),
            Path(config.tensorboard_root_log_dir)
        ])

        prepare_callbacks_config= PrepareCallbacksConfig(
            root_dir= Path(config.root_dir),
            tensorboard_root_log_dir=Path(config.tensorboard_root_log_dir),
            checkpoint_model_filepath=Path(config.checkpoint_model_filepath)
        )
        return prepare_callbacks_config
    

    