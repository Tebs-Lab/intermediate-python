import logging
import logging.config # for weird historical reasons you have to explicitly import this submodule.
from log_config import LOGGING_CONFIG
logging.config.dictConfig(LOGGING_CONFIG)

import module

# Using getLogger will now return the logging configuration from the log_config.py file
# associated with whatever __name__ is (__main__ in this case).
logger = logging.getLogger(__name__)

logger.info("main.py is being run")
module.do_something()

# Mini-exercise: Run this code and try to explain where in the configuration file
# each log message is configured, why it has it's particular format, and why it is logged
# to a particular location. Then, explain why the log message in module that says 
# "module.py is being imported" is not actually logged anywhere.