'''
Constants required of the project
'''
from math import ceil
from logging import DEBUG

ASCII_MAP = "@%#*+=-:. "
ASCII_MAP_LEN = len(ASCII_MAP)
WIDTH = ceil(255/ASCII_MAP_LEN)

DEFAULT_IMAGE_PATH_PATH = "./test.png"
DEFAULT_HEIGHT_CORRECTION = 0.47
DEFAULT_SCALE = 0.5

# Constants required for logger
DEFAULT_LOG_FORMAT = format="%(name)s - %(levelname)s - %(message)s"
DEFAULT_LOG_LEVEL = DEBUG
DEFAULT_LOG_FILE = "/tmp/ascii.log"