import logging
import os

class Logger:
    def __init__(self):
        path = f'{os.getcwd()}/log'
        isExist = os.path.exists(path)
        if not isExist:
            os.makedirs(path)

        logging.basicConfig(filename=f"{path}/file.log",format='%(asctime)s %(levelname)s: %(message)s', encoding='utf-8', level=logging.DEBUG)
        
        # If loging to STD out is needed
        # logging.basicConfig(stream=sys.stdout,format='%(asctime)s\t%(levelname)s\t%(message)s', level=logging.DEBUG)

        logging.info("Logger initlized")

    def debug(self,string):
        logging.debug(string)

    def error(self,string):
        logging.error(string)

    def info(self,string):
        logging.info(string)

    def warning(self,string):
        logging.warning(string)

Log = Logger()