import logging
import os
from datetime import datetime


log_file=f"(datetime.now().strftime('%Y-%m-%d-%H-%M-%S')).log"
log_path=os.path.join(os.getcwd(),"logs",log_file)
os.makedirs(log_path,exist_ok=True)

log_file_path=os.path.join(log_path,log_file)   

logging.basicConfig(filename=log_file_path,level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')


logger=logging.getLogger('fine_tuned_logger')

if __name__=='__main__':
    logging.info('This is a test log message')
    



