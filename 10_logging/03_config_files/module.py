import logging

# Using getLogger will now return the logging configuration from the log_config.py file
# associated with whatever __name__ is (module in this case).
logger = logging.getLogger(__name__)
logger.info("module.py is being imported")

def do_something():
    logger.error("This is an error message from the module")
