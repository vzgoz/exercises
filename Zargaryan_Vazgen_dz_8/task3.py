def type_logger(callback):
    def wrapper(*args):
        for arg in args:
            print(f'{callback.__name__}({arg}:{type(arg)})')

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


calc_cube(5, 'string')
