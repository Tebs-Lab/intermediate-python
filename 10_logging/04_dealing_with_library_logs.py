# Many 3rd party libraries also have logging code.
# This can be very useful, but can also be very noisy.
# But you can control the logging configuration of these libraries!
import logging
import requests

# If I just set the global log level to debug, suddenly I'll see logs from 
# all the libraries that use logging. 
logging.basicConfig(level=logging.DEBUG)
requests.get("https://www.google.com")

# Suppose you want to control the logging of a specific library.
# You can use the "getLogger" function. Notice that the logs came from "urllib3"
# We've turned the level down to INFO so we don't get the debug messages.
logger = logging.getLogger("urllib3")
logger.setLevel(logging.INFO)
requests.get("https://www.google.com")

# Of course we could do anything we wanted with the logger, like set a custom
# handler or formatter, etc. 