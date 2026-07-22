import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))
def logger_decorator(func):
    def wr(*args, **kwargs):
        function_name = (func.__name__)
        positional_parameters = list(args) if args else 'none'
        keyword_parameters = dict(kwargs) if kwargs else 'none'
        result = func(*args, **kwargs)
        log_message = (
            f'function: {function_name}\n'
            f'positional parameters: {positional_parameters}\n'
            f'keyword parameters: {keyword_parameters}\n'
            f"return: {result}\n"
            "-----------------------------"
        )
        logger.log(logging.INFO, log_message)
        return result
    return wr
@logger_decorator
def func_hello():
    print("Hello, World!")
@logger_decorator
def func_args_true(*args):
    return True
@logger_decorator
def func_kwargs_dec(**kwargs):
    return logger_decorator
if __name__ == "__main__":
    func_hello()
    func_args_true(1, 2, 3, 'test', True)
    func_kwargs_dec(a=1, b=2, user='Bob')
    print("test is done, check ./decorator.log")