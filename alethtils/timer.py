"""
# Simple timing decorator utility with logging capabilities
"""


import logging
from functools import wraps
from timeit import default_timer


# logging set-up
logging.basicConfig(
    format="%(asctime)s [%(levelname)s][TIMER]: %(message)s",
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.DEBUG
)

_logger = logging.getLogger(__name__)


def timer(iterations=1, precision=3, save=False, verbose=False):
    """ Timer Decorator with Logging
    save: adds the log to the function's log file
    iterations: re-runs the timer and averages the results
    precision: number of decimal places for the time
    verbose: add all times recorded (via iteration) to the log file
    """
    if iterations < 1 or not isinstance(iterations, int):
        raise AttributeError
    if precision < 1 or not isinstance(precision, int):
        raise AttributeError

    def decorator(function):
        @wraps(function)
        def inner(*args, **kwargs):
            # The tester
            results = []
            for i in range(iterations):
                start = default_timer()
                value = function(*args, **kwargs)
                end = default_timer()
                results.append((value, end-start))
            time = round(sum(run[1] for run in results)/iterations, precision)

            # The logger
            if save:
                _logger.addHandler(logging.FileHandler(f"{function.__name__}.log"))
                _logger.debug(f"[{function.__name__}] {time}s")
                if verbose:
                    times = [round(run[1], precision) for run in results]
                    _logger.debug(f"[{function.__name__}] FULL TIMES: {times}")
            else:
                _logger.debug(f"[{function.__name__}] {time}s")

            return value
        return inner
    return decorator
