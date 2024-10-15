from classifier.constants import *
from classifier.utils.common_functions import *
from classifier.entity.config_entity  import DataIngestionConfig


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