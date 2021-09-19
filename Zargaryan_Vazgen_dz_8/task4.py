def val_checker(callback):
    def checker(function):
        def wrapper(*args):
            for arg in args:
                if callback(arg):
                    return function(arg)
                else:
                    raise ValueError ('Число отрицательное')

        return wrapper
    return checker

@val_checker (lambda x : x > 0)
def calc_cube(x):
    return x ** 3

a = calc_cube(5)
print(a)