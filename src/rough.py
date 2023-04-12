# import logger
# import sys


# def add(a,b):
#     return a+b


# res=add(3,5)
# logger.logging.info(f"Number are added and sum is {res}")

# class AgeError(Exception):
#     "Raise when Person age is Less than 18"

# try:
#     age=int(input("Enter the age: "))
#     if age<18:
#         raise AgeError
# except:
#     print("An error is Occured")



# def error_details(error):
#     _, _, exc_traceback = sys.exc_info()
#     line_no=exc_traceback.tb_lineno
#     error_name=error
#     error_file=exc_traceback.tb_frame.f_code.co_filename
#     # print(line_no)
#     # print(error_name)
#     # print(error_file)
#     error_m=f"This is error: <{error_name}> and Line no is <{line_no}> and file name is <{error_file}>"
#     return error_m

# def trying():
#     try:
#         a=3
#         b="Name"
#         print(a+b)

#     except Exception as e:
#             return e
# e=trying()
# print(e)

# error_details(e,sys)

# try:
#     # print(int("k"))
#     print(a+29)
# except Exception as e:
#     raise CustomError(e)
    # a=e
    # print("This is error:",e)
    # exc_type, exc_value, exc_tb = sys.exc_info()
    # print("Type:", exc_type)
    # print("Value:", exc_value)
    # print("Traceback:", exc_tb)
    # another_option=sys.exc_info()[2]
    # _,_,exc_tb=sys.exc_info()
    # print(f"This is error: {a} and Line no is {exc_tb.tb_lineno} and file name is {exc_tb.tb_frame.f_code.co_filename}")
    # error_message= f"This is error: {a} and Line no is {another_option.tb_lineno} and file name is {another_option.tb_frame.f_code.co_filename}"
    # print(error_message)
#     print(type(a))
#     myerror_detail=error_details(a)
# print(myerror_detail)


# class CustomError(Exception):
#     "Here is class for the Raise the Custom Expection" 

#     def __init__(self,error_message):  #giving an argument as error message

#         super().__init__(self,error_message)   #need to call the Exception class using super().__init__() for using the functionality methods of Exception class
#         #also give an argument to super constracter which we give in our constractor..
#         self.error_message=error_details(error_message)    ##creating variable using self as creates in class and call the function to fetch the value
    
#     def __str__(self):
#         return self.error_message
    


# try:
#     print(2+"raj")

# except Exception as e:
#     raise CustomError(e)

# print("All lines are running")

##data Ingestion##
# import os
# from dataclasses import dataclass
# import pandas as pd
# from sklearn.model_selection import train_test_split

# @dataclass
# class DataingestionConfig:
#     data_path=os.path.join("Artifacts","data.csv")  #creating the path of the file where file/data will be store later
#     train_data_path=os.path.join("Artifacts","train.csv")  #creating the train path 
#     test_data_path=os.path.join("Artifacts","test.csv")   #creating the test path as well

# class DataIngestion:

#     def __init__(self):
#         self.path_details=DataingestionConfig()  #storing all the paths in a varibale due to which we can later call them directly by using that
#         print(self.path_details.data_path)
#         print(self.path_details.train_data_path)
#         print(self.path_details.test_data_path)

#     def initiate_data_ingestion(self):
#         data=pd.read_csv("data/StudentsPerformance.csv")
#         artifacts_path=os.path.join(os.getcwd(),"test")
#         # os.makedirs(artifacts_path,exist_ok=True)
#         # os.makedirs(os.path.dirname(self.path_details.data_path))
#         train_set,test_set=train_test_split(data,test_size=0.2,random_state=42)
#         train_set.to_csv(self.path_details.train_data_path)
#         test_set.to_csv(self.path_details.test_data_path)
#         data.to_csv(self.path_details.data_path)


# obj=DataIngestion()
# obj.initiate_data_ingestion()

# from logger import logging
# from exception import CustomError
# from dataclasses import dataclass
# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.compose import ColumnTransformer
# from sklearn.pipeline import Pipeline
# from sklearn.impute import SimpleImputer
# from sklearn.preprocessing import OneHotEncoder,StandardScaler
# import os
# from utils import save_obj

# @dataclass
# class DataTransformationConfig:
#     preprocessor_obj_path=os.path.join("Artifacts","rough.pkl")

# class DataTransformation:

#     def __init__(self):
#         self.preprocessor_obj_path=DataTransformationConfig()

#     def Get_Preprocessor(self):
#         try:
#             data=pd.read_csv(r"C:\Users\asdf\Documents\D.S\CICD\CICD-Test\data\insurance.csv")
#             logging.info("Data has been read ")
#             Target_feature="charges"
#             x=data.drop(Target_feature,axis=1)
#             num_features=x.select_dtypes([float,int]).columns
#             cat_features=x.select_dtypes(object).columns
#             logging.info("Numeric and Categorical features are diffirenciate successfully")
#             #create the num and cat pipline

#             num_pipe=Pipeline(steps=[
#                 ("imputer",SimpleImputer(strategy="median")),
#                 ("Scaler",StandardScaler())
#             ])           
#             cat_pipe=Pipeline(steps=[
#                 ("imputer",SimpleImputer(strategy="most_frequent")),
#                 ("Encoder",OneHotEncoder())
#             ])

#             logging.info("Both the Pipline has been created successfully")

#             Preprocessor=ColumnTransformer([
#                 ("numeric",num_pipe,num_features),
#                 ("categorical",cat_pipe,cat_features)
#             ])
#             logging.info("Processor has been Created Successfully..")

#             return Preprocessor

#         except Exception as e:
#             raise CustomError(e)
        
#     def initiate_data_transform(self,train_data_path,test_data_path):
#         try:
#             train_data=pd.read_csv(train_data_path)
#             test_data=pd.read_csv(test_data_path)
#             Target_feature="charges"
#             y_train=train_data[Target_feature]
#             x_train=train_data.drop(Target_feature,axis=1)
#             y_test=test_data[Target_feature]
#             x_test=test_data.drop(Target_feature,axis=1)
#             preprocessor_obj=self.Get_Preprocessor()

#             x_train_x=preprocessor_obj.fit_transform(x_train)
#             x_test_x=preprocessor_obj.fit_transform(x_test)

#             x_train_array=np.c_[x_train_x,np.array(y_train)]
#             x_test_array=np.c_[x_test_x,np.array(y_test)]

#             save_obj(self.preprocessor_obj_path.preprocessor_obj_path,preprocessor_obj)

#             return (x_train_array,
#                     x_test_array,
#                     preprocessor_obj)
            
#         except Exception as e:
#             raise CustomError(e)

##model Training##

# import os
# from exception import CustomError
# # from logger import logging
# from dataclasses import dataclass
# # from catboost import CatBoostRegressor
# from xgboost import XGBRegressor

# from sklearn.ensemble import (AdaBoostRegressor,
#                               RandomForestRegressor,
#                               GradientBoostingRegressor)

# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error
# from sklearn.neighbors import KNeighborsRegressor
# from sklearn.tree import DecisionTreeRegressor
# from utils import evaluate_models,save_obj
# from check import model_evaluate, save_objects

# @dataclass
# class RoughModelTrainerConfig:
#     model_saving_path=os.path.join("Artifacts","rough_model.pkl")

# class RoughModelTrainer:
#     try:

#         def __init__(self):
#             self.model_trainer_config=RoughModelTrainerConfig()

#         def initiate_rough_model_trainer(self,train_array,test_array):

#             x_train,y_train,x_test,y_test=(train_array[:,:-1],train_array[:,-1],
#                                         test_array[:,:-1],test_array[:,-1]
#             )

#             models={
#                 "Linerregression":LinearRegression(),
#                 "Xgboost":XGBRegressor(),
#                 "Kneighbour": KNeighborsRegressor(),
#                 "Decision Tree Regressor":DecisionTreeRegressor(),
#                 "Random Forest Regressor":RandomForestRegressor(),
#                 "Ada grad Regressor":AdaBoostRegressor(),
#                 "Gradiant Regressor":GradientBoostingRegressor()
#             }

#             records=model_evaluate(x_train,y_train,x_test,y_test,models)
#             best_score=max(list(records.values()))
#             # best_model=list(records.keys())[list(records.values).index(best_score)]
#             best_model=list(records.keys())[list(records.values()).index(best_score)]

#             save_objects(self.model_trainer_config.model_saving_path,best_model)

#             return print("This is rough model best accuracy:",best_score)
#     except Exception as e:
#         raise CustomError(e)



from flask import Flask,render_template,request
import pandas as pd
import pickle

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict",methods=["GET","POST"])
def predict():
            if request.method=="POST":
                   
                age=request.form["age"]
                sex=request.form.get("sex")
                bmi=request.form.get("bmi")
                children=request.form.get("children")
                smoker=request.form.get("smoker")
                region=request.form.get("region")
                d={"age":int(age),"sex":sex,"children":int(children),"smoker":smoker,"region":region,"bmi":int(bmi)}

                data={
                "age":[age],
                "sex":[sex],
                "bmi":[bmi],
                "children":[children],
                "smoker":[smoker],
                "region":[region]
                }
                df=pd.DataFrame(data)
                # print(df)
                preprocessor_path=r"C:\Users\asdf\Documents\D.S\CICD\CICD-Test\Artifacts\preprocessor.pkl"
                with open(preprocessor_path,"rb") as f:
                      preprocessor=pickle.load(f)
                scaled_data=preprocessor.transform(df)
                # print(scaled_data)
                model_path=r"C:\Users\asdf\Documents\D.S\CICD\CICD-Test\Artifacts\Model.pkl"
                with open(model_path,"rb") as f:
                      model=pickle.load(f)
                
                # print(model)
                pred=model.predict(scaled_data)
                print(pred)

                return render_template("rough_html.html",pred=pred[0])


if __name__=="__main__":
    app.run(debug=True)

