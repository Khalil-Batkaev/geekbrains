from functools import wraps


def val_checker(validate_func):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if validate_func(*args):
                result = func(*args)
                print(f'Call for: {func.__name__}')
                print(*[f'{x}: {type(x)}' for x in args], sep=', ')
                if kwargs:
                    print(*[f"'{key}' = {val}: {type(val)}" for key, val in kwargs.items()], sep=', ')
                print(f'Result: {result}, type: {type(result)}')
                return result
            else:
                msg = f'wrong val {args[0]}'
                raise ValueError(msg)
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(2))
