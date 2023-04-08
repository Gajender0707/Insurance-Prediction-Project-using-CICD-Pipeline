from logger import logging
from exception import CustomError
import pickle
import os
import dill



def save_obj(file_path,object):
        try:
              dir_path=os.path.dirname(file_path)
              os.makedirs(dir_path,exist_ok=True)

              with open(file_path,"wb") as file_obj:
                    dill.dump(object,file_obj)                
        except Exception as e:
            raise CustomError(e)