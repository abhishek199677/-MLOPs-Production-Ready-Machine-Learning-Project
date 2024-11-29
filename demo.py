from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys 

logging.info("Welcome to logging")

try:
    a = 2 / 0
except Exception as e:
    raise USvisaException(e, sys)   #Ensure USvisaException accepts these arguments


    