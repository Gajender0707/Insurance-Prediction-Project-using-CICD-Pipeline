from logger import logging
from exception import CustomError
from dataclasses import dataclass
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
import os
from utils import save_obj

@dataclass
class DataTransformationConfig:
    preprocessor_obj_path=os.path.join("Artifacts","preprocessor.pkl")  #path for the save the object in the pickle format...

class DataTransformation:
    
    def __init__(self):
        self.data_transformtion_config=DataTransformationConfig()

    def get_data_transformation_object(self):
        """
                Main aim of this function is to get the 
                        tranformer object by using and giving data to 
                                object we find out the transformed data        """
        try:
            data=pd.read_csv(r"C:\Users\asdf\Documents\D.S\CICD\CICD-Test\Artifacts\data.csv")
            data=data.drop(data.iloc[:,0:1],axis=1)
            x=data.drop("charges",axis=1)
            categorical_features=x.select_dtypes(object).columns
            numeric_features=x.select_dtypes([float,int]).columns

            num_pipline=Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())
            ])

            cat_pipeline=Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("Encoder",OneHotEncoder()),

                ]
            )
            logging.info("Pipeline has been created..")
            logging.info("numeric and categorical has been created..")

            logging.info(f"our Categorical Features are {categorical_features} ")
            logging.info(f"our Numeric Features are: {numeric_features}")

            preprocessor=ColumnTransformer(
            [
                ("Num_pipline",num_pipline,numeric_features),
                ("cat_pipline",cat_pipeline,categorical_features)
            ]
            )

            return preprocessor
        



        except Exception as e:
            raise CustomError(e)
    
    def initiate_data_transformation(self,train_path,test_path):
        """
        In this function we will write  the code for transform the data using the upper function object
        """
        try:
            train_df=pd.read_csv(train_path) #reading the training data
            test_df=pd.read_csv(test_path)   #reading the testing data

            logging.info("Read the Train and Test data")
            logging.info("Obtained the Preprocessor")

            preprocessing_obj=self.get_data_transformation_object()

            target_column="charges"
            #getting the x_train and y_train columns
            train_df_y=train_df[target_column]
            train_df_x=train_df.drop(target_column,axis=1)

            ##getting the x_Test and y_test columns in pandas data frame
            test_df_y=test_df[target_column]
            test_df_x=test_df.drop(target_column,axis=1)

            logging.info("x_train, y_train and x_test,y_test getted successfully")

            train_arr_x=preprocessing_obj.fit_transform(train_df_x)
            test_arr_x=preprocessing_obj.fit_transform(test_df_x)

            logging.info("fit and transform the data using preprocessing object using pipelina and columntransformer")

            train_arr=np.c_[train_arr_x,np.array(train_df_y)]
            test_arr=np.c_[test_arr_x,np.array(test_df_y)]
            logging.info("train array and test array are created after the fit and transform")

            save_obj(
                file_path=self.data_transformtion_config.preprocessor_obj_path,
                object=preprocessing_obj
            )
            
            return (
                train_arr,
                test_arr,
                self.data_transformtion_config.preprocessor_obj_path
            )
   
        except Exception as e:
            raise CustomError(e)