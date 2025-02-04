import pathlib

LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'detailed': {
            'style': '{',
            'format': '{asctime} - {name} - {levelname} - {module} - {lineno} - {message}',
        },
        'simple': {
            'style': '{',
            'format': '{levelname} - {message}',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'level': 'DEBUG',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': str(pathlib.Path(__file__).parent / 'sample.log'),
            'formatter': 'detailed',
            'level': 'DEBUG',
            'mode': "w" # Note, this causes the log file to be written from scratch each time the program is run.
        },
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'functions': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}