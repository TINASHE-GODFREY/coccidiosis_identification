import os
import sys
import logging 

#logging_str="[%(asctime)s:%(levelname)%:%(module)s:%(message)s]"

#creating a directory named logs
log_dir="logs"
log_filepath= os.path.join(log_dir,"running logs")
os.makedirs(log_dir, exist_ok=True)


#initialising the log
logging.basicConfig(

    level=logging.INFO,
     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
    
)

logger = logging.getLogger(__name__)

# Log a message
logger.info("welcome tinashe")