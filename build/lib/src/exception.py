## creating the Custom Exception

#step.1: Create a function for give the detail of that perticular error by taking that error using sys

import sys

def Error_details(error):
    exc_tb=sys.exc_info()[2]  #sys give all details automatic when come in under exception error
    error_name=error
    error_line=exc_tb.tb_lineno
    error_file_name=exc_tb.tb_frame.f_code.co_filename
    
    error_message=f"""An Error named: {error_name} has been occured in pythons script on 
    line No. {error_line} and  In the file {error_file_name}"""

    return error_message

##Now create the Custom Error class using pre-defined class Exception

class CustomError(Exception):  #inherit the pre-defined class Exception
    "Creating a Custom error"
    def __init__(self,error_message):   #create the constructor by give a argument name error_message
        super().__init__(self,error_message)   #create the Super Class : Exception Constructor by giving that same argument.
        self.error_message=Error_details(error_message)  #as Error message will come fro

    def __str__(self):  #Create function for the return the message
        return self.error_message
    
