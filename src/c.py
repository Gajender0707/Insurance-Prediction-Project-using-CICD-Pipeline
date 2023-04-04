from logger import logging
from exception import CustomError
if __name__=="__main__":
    try:
        print(2+"custom")
    except Exception as e:
        print("error",e)
        logging.info(f"{e} error has been occured")
        raise CustomError(e)