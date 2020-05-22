import logging
from functools import wraps
from timeit import default_timer

logging.basicConfig(
    format="%(asctime)s [%(levelname)s][TIMER]: %(message)s",
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.DEBUG
)

_logger = logging.getLogger(__name__)


def file_handler(filename):
    return logging.FileHandler(f"{filename}.log")


def timer(save=False, precision=3):
    """ Timer Decorator with Logging """
    def decorator(function):
        @wraps(function)
        def inner(*args, **kwargs):
            start = default_timer()
            value = function(*args, **kwargs)
            end = default_timer()
            if save:
                _logger.addHandler(file_handler(function.__name__))
                _logger.debug(f"[{function.__name__}] {round(end-start, precision)}s")
            else:
                _logger.debug(f"[{function.__name__}] {round(end - start, precision)}s")
            return value
        return inner
    return decorator

