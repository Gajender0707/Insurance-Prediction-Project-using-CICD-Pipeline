import os
from exception import CustomError
from logger import logging
from dataclasses import dataclass
# from catboost import CatBoostRegressor
from xgboost import XGBRegressor

from sklearn.ensemble import (AdaBoostRegressor,
                              RandomForestRegressor,
                              GradientBoostingRegressor)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from utils import evaluate_models,save_obj

@dataclass
class ModelTrainerConfig:
    model_trainer_path=os.path.join("Artifacts","Model.pkl")

class ModelTrainer:

    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Splitting Training and Test Data")
            x_train,y_train,x_test,y_test=(
                train_array[:,:-1],train_array[:,-1],
                test_array[:,:-1],test_array[:,-1]
            )

            
            models={
                "Liner Regression":LinearRegression(),
                "Xgboost Regressor":XGBRegressor(),
                # "catboost Regressor":CatBoostRegressor(),
                "KNeighbor Regressor":KNeighborsRegressor(),
                "Adaboost Regression":AdaBoostRegressor(),
                "DecisionTree Regressor":DecisionTreeRegressor(),
                "GradiantBoost Regressor":GradientBoostingRegressor(),
                "Random Forest Regressor":RandomForestRegressor()
            }
            logging.info("All the Models for the Training are defined")

            logging.info("Creating a Report using utils model evalute function by giving train and test data")


            models_report:dict=evaluate_models(x_train=x_train,y_train=y_train,x_test=x_test,y_test=y_test,models=models)

            best_score=max(list(models_report.values()))
            best_model_name=list(models_report.keys())[list(models_report.values()).index(best_score)]

            best_model=models[best_model_name]
            logging.info("Find the Best Model With the higest Accuracy")

            if best_score<0.6:
                raise CustomError("No Best Model Found")
            

            save_obj(self.model_trainer_config.model_trainer_path,object=best_model)
            logging.info("Model has been saved Successfully")

            prediction=best_model.predict(x_test)
            r2_accuracy=r2_score(y_test,y_pred=prediction)

            return r2_accuracy



        except Exception as e:
            raise CustomError(e)