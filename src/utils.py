from logger import logging
from exception import CustomError
import pickle
import os
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV


def save_obj(file_path,object):
        try:
              dir_path=os.path.dirname(file_path)
              os.makedirs(dir_path,exist_ok=True)

              with open(file_path,"wb") as file_obj:
                    dill.dump(object,file_obj)                
        except Exception as e:
            raise CustomError(e)
        

def evaluate_models(x_train,y_train,x_test,y_test,models,param):
      try:
            report={}
            for i in range(len(list(models))):
                  model=list(models.values())[i]
                  logging.info("Training the Models")
                  para=param[list(models.keys())[i]]
                  
                  gs=GridSearchCV(model,para,cv=3)
                  gs.fit(x_train,y_train)  #now fit with some parameters with different different models


                  model.set_params(**gs.best_params_)     #set the best parameters 

                  model.fit(x_train,y_train)
                  y_train_pred=model.predict(x_train)
                  y_test_pred=model.predict(x_test)

                  train_model_score=r2_score(y_train,y_pred=y_train_pred)
                  test_model_score=r2_score(y_test,y_pred=y_test_pred)

                  logging.info("Predict the train score and test score using the r2 score")



                  report[list(models.keys())[i]]=test_model_score

                  return report

      except Exception as e:
            raise CustomError(e)
      
def load_object(file_path):
     try:
      with open(file_path, "rb") as f:
            return dill.load(f)
             
     except Exception as e:
      raise CustomError(e)
