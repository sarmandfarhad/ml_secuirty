import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message: str, error_detail: sys):
       
        self.error_message = error_message
        _, _,exc_tb = error_detail.exc_info()
        self.file_name = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        
    def __str__(self) -> str:
        return f"Error occurred in file: {self.file_name} at line: {self.file_name} with message:[ {self.error_message}]"
      
if __name__ == "__main__":
    try:
        logger.logging.info("This is a test log message.")
        a=1/0
        print('This will not be printed',a)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
      