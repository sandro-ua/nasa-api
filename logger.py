import logging
import os


logger = logging.getLogger('nasa-api-logger')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
log_filename = "logs/output.log"
os.makedirs(os.path.dirname(log_filename), exist_ok=True)
fh = logging.FileHandler(log_filename, mode="a", encoding=None, delay=False)
fh.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add the handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)
