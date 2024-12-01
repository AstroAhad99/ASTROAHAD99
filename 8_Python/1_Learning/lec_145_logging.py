"""
Loggers are very important feature of the python to debug the
and print some information.

Levels of loggers
DEBUG (This does not show up by default and you have to enable it)
INFO (This show not show up by default and you have to enable it)
WARNING (This show up by default)
ERROR (This show up by default)
CRITICAL (This show up by default)

"""

import logging
logging.basicConfig(format='%(asctime)s ---> %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', 
                    datefmt = '%d-%m-%Y %H:%M:%S',
                    level = logging.DEBUG,
                    filename = 'C:\\Users\\Qanare\\Documents\\ASTROAHAD99\\8_Python\\1_Learning\\Logs_lec145.txt',)

logger = logging.getLogger("My_Logger")
logger2 = logging.getLogger("My_Logger.Internal")


logger.debug('This is debug level logger')
logger.info('This is info level logger')
logger.warning('This is warning level logger')
logger.critical('This is critical level logger')
logger.error('This is error level logger')


logger2.debug('This is debug level logger')
logger2.info('This is info level logger')
logger2.warning('This is warning level logger')
logger2.critical('This is critical level logger')
logger2.error('This is error level logger')