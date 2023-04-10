# # from exception import CustomError
# # from logger import logging


# # try:
# #     print(2+"sys")

# # except Exception as e:
# #     logging.info(f"An {e} error is Occured")
# #     raise CustomError(e)

# # print("All are running well")

# # from datetime import datetime

# # print(datetime.now().strftime(format="%H_%M_%S_%d_%m_%y"))

# from sklearn.metrics import r2_score


# def model_evaluate(x_train,y_train,x_test,y_test,models):
#     records={}
#     for i in range(len(list(models))):
#         model=list(models.values())[i]
#         model.fit(x_train,y_train)

#         y_pred_train=model.predict(x_train)
#         y_pred_test=model.predict(x_test)

#         test_r2_score=r2_score(y_test,y_pred=y_pred_test)
#         records[model]=test_r2_score


#         return records

# import os
# import dill

# def save_objects(file_path,object):
#     file_path_name=os.path.join(file_path)

#     os.makedirs(os.path.dirname(file_path_name),exist_ok=True)

#     with open(file_path_name, 'wb') as file:
#         dill.dump(object, file)




