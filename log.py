import logging
from constants import (
                        DEFAULT_LOG_LEVEL,
                        DEFAULT_LOG_FILE_PATH,
                        DEFAULT_LOG_FORMAT
                        )

def setup_logger(
                path_to_logfile=DEFAULT_LOG_FILE_PATH,
                level=DEFAULT_LOG_LEVEL,
                format=DEFAULT_LOG_FORMAT
                ):
    '''
    This function is used to setup basic configurations for the logger.
    
    Parameters
    ----------
    filename - The path the log file.
    level - Log level
    format - Logging format
    '''
    logging.basicConfig(
                        level=level,
                        filename=path_to_logfile,
                        filemode='w',
                        format=format
                        )
