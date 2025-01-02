import logging
import os

# Define the log file path
log_file_path = r'C:\Users\ahad9\Documents\ASTROAHAD99\8_Python\2_Challenge\milestone_proj4_V1\logs.txt'

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    level=logging.DEBUG,
    filename=log_file_path
)

logger = logging.getLogger('scraping')