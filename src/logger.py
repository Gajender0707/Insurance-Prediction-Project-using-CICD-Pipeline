import logging
import os
from datetime import datetime

# print(os.getcwd())
folder_name=datetime.strftime(datetime.now(),"%H_%M_%S_%d_%m_%y")
# print(folder_name)
file_name=f"{folder_name}.log"
# print(file_name)

foler=os.path.join(os.getcwd(),"LOGS")

log_folder=os.path.join(foler,folder_name)
os.makedirs(log_folder,exist_ok=True)
# print(log_folder)
log_file_name=os.path.join(log_folder,file_name)
# print(log_file_name)

logging.basicConfig(
    filename=log_file_name,
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s-%(name)s=%(levelname)s-%(lineno)s-%(message)s",
)

# logging.info("This is logged")
# logging.info("Here log is logged")
# logging.info("This is for checking that happening simultanously")

