from signLanguage.logger import logging
from signLanguage.exception import SignException
import sys
# logging.info("Starting the application...")

try:
    a = 7 / '9'
    
except Exception as e:
    logging.info("Exception occurred", exc_info=True)
    raise SignException(e, sys)


