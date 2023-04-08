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

