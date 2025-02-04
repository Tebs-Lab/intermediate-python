import logging

# Since this module is imported by main, __name__ will be a string
# reference to this module.
logger = logging.getLogger(__name__)
logger.info("module.py is being imported")

def do_something():
    logger.info("This is an info message from the module")
