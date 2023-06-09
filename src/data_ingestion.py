# data ingestion

import pandas as pd
from sklearn.model_selection import train_test_split
import os
from dataclasses import dataclass
from logger import logging
from exception import CustomError
from data_transformation import DataTransformation,DataTransformationConfig
from model_trainer import ModelTrainerConfig,ModelTrainer


@dataclass
class DataIngestionConfig:
    data_path=os.path.join("Artifacts","data.csv")
    train_data_path=os.path.join("Artifacts","train.csv")
    test_data_path=os.path.join("Artifacts","test.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingstion has been started")
        try:
            data=pd.read_csv("data/insurance.csv")  #read the dataset
            logging.info("Data Read Successfully")    

            os.makedirs(os.path.dirname(self.ingestion_config.data_path),exist_ok=True)

            logging.info("Data split has been initiated")
            train_set,test_set=train_test_split(data,test_size=0.2,random_state=42)
            data.to_csv(self.ingestion_config.data_path)
            train_set.to_csv(self.ingestion_config.train_data_path)
            test_set.to_csv(self.ingestion_config.test_data_path)

            logging.info("Ingestion of Data has been succesfully ")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomError(e)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_array,test_array,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)

    model_trainer_obj=ModelTrainer()
    print(model_trainer_obj.initate_model_trainer(train_array=train_array,test_array=test_array))
