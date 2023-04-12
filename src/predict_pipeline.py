from logger import logging
from exception import CustomError
import pandas as pd
import numpy as np
from utils import load_object


class PredictPipeline:

    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=r"C:\Users\asdf\Documents\D.S\CICD\CICD-Test\Artifacts\Model.pkl"
            preprocessor_path=r"C:\Users\asdf\Documents\D.S\CICD\CICD-Test\Artifacts\preprocessor.pkl"

            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)

            scaled_data=preprocessor.transform(features)
            preds=model.predict(scaled_data)
            return preds
        except Exception as e:
            raise CustomError(e)
        
#we create this class only for the conver the datapoints into the dataFrame row and columns
class CustomData:

    def __init__(self,age:int,sex:str,bmi:float,children:int,smoker:str,region:str):
        self.age=age
        self.sex=sex
        self.bmi=bmi
        self.children=children
        self.smoker=smoker
        self.region=region

    #we create this 
    def get_values_as_dataframe(self):
        try:
            custom_data_inputs={
                "age":[self.age],
                "sex":[self.sex],
                "bmi":[self.bmi],
                "children":[self.children],
                "smoker":[self.smoker],
                "region":[self.region]
            }

            return pd.DataFrame(custom_data_inputs)

        except Exception as e:
            raise CustomError(e)

        