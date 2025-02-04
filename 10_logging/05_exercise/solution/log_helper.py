import logging
import functools

def log(logger: logging.Logger, level: int):

    def decorator(input_function):
        functools.wraps(input_function)
        def wrapper(*args, **kwargs):
            logger.log(level=level, msg=f'{input_function} called with args: {args} and kwargs: {kwargs}')
            r = input_function(*args, **kwargs)
            logger.log(level=level, msg=f'{input_function} returned {r}')
            return r
        
        return wrapper

    return decorator