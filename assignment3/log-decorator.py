import logging
from functools import wraps

logger = logging.getLogger(__name__+"_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__

        pos_params = list(args) if args else "none"

        kw_params = kwargs if kwargs else "none"

        result = func(*args, **kwargs)

        logger.log(logging.INFO, f"function: {func_name}")
        logger.log(logging.INFO, f"positional parameters: {pos_params}")
        logger.log(logging.INFO, f"keyword parameters: {kw_params}")
        logger.log(logging.INFO, f"return: {result}")
        logger.log(logging.INFO, "---------------------")

        return result

    return wrapper

@logger_decorator
def say_whatsUp():
    print("What's up?")

@logger_decorator
def take_args(*args):
    return True

@logger_decorator
def take_kwargs(**kwargs):
    return logger_decorator 

    
if __name__ == "__main__":
    say_whatsUp()
    take_args(1, 2, 3)
    take_kwargs(a=1, b=2)
