## setup.py##

# from setuptools import setup,find_packages


# def requirements_func():
#     with open("requirements.txt","r") as f:
#         req=f.readlines()
#         req=[i.replace("\n","") for i in req ]
#         if "-e ." in req:
#             req.remove("-e .")
#         return req

# setup(
#     name="Gajender",
#     author="Gajender",
#     description="this is revion file",
#     author_email="check@gmail.com",
#     packages=find_packages(),
#     install_requires=requirements_func()

# )


##Now Logger.py ##

# import logging
# from datetime import datetime
# import os

# main_folder=os.path.join(os.getcwd(),"Logs_test")
# sub_folder_name=datetime.now().strftime(format="%H_%M_%S_%d_%m_%y")
# sub_folders_path=os.path.join(main_folder,sub_folder_name)
# print(sub_folders_path)
# # file_name=f"{sub_folders_path}.log"
# os.makedirs(sub_folders_path,exist_ok=True)
# # print(file_name)
# # file_path=os.path.join(main_folder,sub_folders_path,file_name)
# file_path=os.path.join(sub_folders_path,"19_3_2_2_2_9.log")
# file_path=os.path.join(sub_folders_path,f"{datetime.now().strftime(format='%H_%M_%S')}.log")
# print(file_path)

# logging.basicConfig(
#     filename=file_path,
#     filemode="w",
#     level=logging.INFO,
#     format="%(asctime)s-%(level)s-%(lineno)s-%(message)s"
# )

##Exception##
# import sys
# def error_details(error):
#     exc_tb=sys.exc_info()[2]
#     error_name=error
#     lineno=exc_tb.tb_lineno
#     file_name=exc_tb.tb_frame.f_code.co_filename
    
#     error_message=f"An python scrip error ocured  error is {error_name} and line no {lineno} and file name {file_name}"
#     return error_message


# class CustomException(Exception):
#     "Creating Custom Exception"

#     def __init__(self,error):
#         super().__init__(self,error)
#         self.error=error_details(error)

#     def __str__(self):
#         return self.error
    

# try:
#     print(3+"b")
# except Exception as e:
#     raise CustomException(e)


##data ingestion##

# import os
# from sklearn.model_selection import train_test_split
# from dataclasses import dataclass
# import pandas as pd

# @dataclass
# class DataIngestionConfig:
#     data_path=os.path.join("Datasets","data.csv")
#     train_data_path=os.path.join("Datasets","train.csv")
#     test_data_path=os.path.join("Datasets","test.csv")

# class initiate_data_ingestion:
#     def __init__(self):
#         self.paths_detail=DataIngestionConfig()

#     def data_ingestion(self):
#         print(self.paths_detail.data_path)
#         print(self.paths_detail.train_data_path)
#         print(self.paths_detail.test_data_path)
#         os.makedirs(os.path.dirname(self.paths_detail.data_path),exist_ok=True)

#         data=pd.read_csv("data\StudentsPerformance.csv")

#         train_set,test_set=train_test_split(data,test_size=0.2,random_state=42)
#         train_set.to_csv(self.paths_detail.train_data_path)
#         test_set.to_csv(self.paths_detail.test_data_path)
#         data.to_csv(self.paths_detail.data_path)

# obj=DataIngestionConfig()
# obj1=initiate_data_ingestion()
# obj1.data_ingestion()
