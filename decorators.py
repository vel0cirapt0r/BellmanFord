import time
import logging
from functools import wraps

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Decorator for measuring the time
def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"Execution time for {func.__name__}: {end_time - start_time:.6f} seconds")
        return result

    return wrapper


# Decorator for handling errors
def handle_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {str(e)}")
            return None

    return wrapper
