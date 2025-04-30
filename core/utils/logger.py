# core/utils/logger.py
import logging
import sys

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_LEVEL = logging.DEBUG

def setup_logger():
    """Configures the root logger."""
    logging.basicConfig(level=LOG_LEVEL,
                        format=LOG_FORMAT,
                        handlers=[logging.StreamHandler(sys.stdout)]) # Log to console

def get_logger(name):
    """Gets a logger instance with the specified name."""
    return logging.getLogger(name)