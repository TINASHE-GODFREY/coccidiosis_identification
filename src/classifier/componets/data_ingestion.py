# updating the componets when getting the pictures
import os 
import urllib.request as request
import zipfile
from classifier import logger
from  classifier.utils.common_functions import get_size
from classifier.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config= config 



# method to download the zip file
    def download_file(self):
        if not os.path.exists(self.config.local_datafiles):
            filename, headers =request.urlretrieve(url=self.config.source_url, filename=self.config.local_datafiles)
            logger.info(f"{filename} download!! with the following info {headers}")

        else:
            logger.info(f"file already exits of size {get_size(Path(self.config.local_datafiles))}")

    #method to unzip the  zip file 
    def extract_zip_files(self):
        """ zip_file_path: str
        Extract the zip file into  the data directory
        function returns None
        """
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_datafiles, "r") as zip_ref:
            zip_ref.extractall(unzip_path)
