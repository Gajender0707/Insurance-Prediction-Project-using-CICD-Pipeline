import os
import dill
from sklearn.preprocessing import StandardScaler
# def save_file(file_path,obj):
#     path=os.path.join("Artifacts","preprocessor.pkl")
#     print(path)
#     file_path=os.path.dirname(file_path)
#     print(file_path)

# save_file()

s=StandardScaler()
file_path=os.path.join("Artifacts","checker.pkl")
print(file_path)
folder_path=os.path.dirname(file_path)
print(file_path)
os.makedirs(folder_path,exist_ok=True)

with open(file_path, "wb") as dill_file:
    dill.dump(s, dill_file)