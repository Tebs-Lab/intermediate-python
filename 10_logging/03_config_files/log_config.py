import pathlib

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'detailed': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s',
        },
        'simple': {
            'format': '%(levelname)s - %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'level': 'INFO',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': str(pathlib.Path(__file__).parent / 'sample.log'),
            'formatter': 'detailed',
            'level': 'INFO',
            'mode': "w" # Note, this causes the log file to be written from scratch each time the program is run.
        },
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['console'],
            'level': 'INFO',
        },
        '__main__': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'module': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}