import logging
logging.basicConfig(level=logging.INFO, 
                    format="[{asctime}]{levelname}:{name}:{message}", 
                    style="{", 
                    datefmt="%Y-%m-%d %H:%M:%S"
)

import sys # Using this to manage output of stream handler
import pathlib # To specify the location of a log file.
import module

# It's common to use specific loggers per module. This allows you to
# easily track the location in the code of a particular log entry. 
# It also allows us to use different configuration settings for 
# different parts of the code.

# __name__ will contain the module hierarchy, or in this file it will be '__main__'
# but either way this helps us track where the log message is coming from.
logger = logging.getLogger(__name__)

# The "basicConfig" function is a "global" configuration for the 
# root logger. This is a good way to set up a default configuration
# but if you want to configure individual loggers you need to use 
# "formatters" and "handlers"

logger.info("Prior to setting specific formatter and handler")

# Lets make a logger for main, and add two handlers. One for the console
# and one for a file. 
logger = logging.getLogger(__name__)

# std error is the default, stdout is another option
console_handler = logging.StreamHandler(stream=sys.stderr)

# this will append to a file called "sample.log" in the current directory
file_handler = logging.FileHandler(pathlib.Path(__file__).parent / "sample.log", mode="a", encoding="utf-8")

logger.addHandler(console_handler)
logger.addHandler(file_handler)

# We can also add a custom formatter that overwrites the "basicConfig" format
# but we add them to the handlers, not the logger itself. In this example we 
# don't care much about the date in the console handler, but we do care about it
# for the file handler.
console_formatter = logging.Formatter(
    "{levelname} - {message}",
     style="{"
)
console_handler.setFormatter(console_formatter)

file_formatter = logging.Formatter(
    "[{asctime}]{levelname}:{name}:{message}", 
    style="{", 
    datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(file_formatter)

# NOTE! if you've already set a basicConfig then logging to a file handler 
# will ALSO log to the console. This is because the root logger is active and 
# log messages propagate up to the root logger. You can turn this off with:
logger.propagate = False

logger.error("This error message gets logged differently in the console vs the file it creates")

# Finally, notice that the log messages from the module are handled by their own logger
module.do_something()

# Micro-Exercise: Change the code in module.py such that it logs to the sample.log file
# and does not ever log to the console. 