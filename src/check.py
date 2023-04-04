from exception import CustomError
from logger import logging


try:
    print(2+"sys")

except Exception as e:
    logging.info(f"An {e} error is Occured")
    raise CustomError(e)

print("All are running well")