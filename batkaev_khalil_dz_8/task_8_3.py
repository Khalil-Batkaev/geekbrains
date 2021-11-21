def logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args)
        print(f'Call for: {func.__name__}')
        print(*[f'{x}: {type(x)}' for x in args], sep=', ')
        if kwargs:
            print(*[f"'{key}' = {val}: {type(val)}" for key, val in kwargs.items()], sep=', ')
        print(f'Result: {result}, type: {type(result)}')
        return result
    return wrapper


@logger
def render_input(*args):
   return 1


@logger
def calc_cube(x):
   return x ** 3


print(calc_cube(3))
print()
print(render_input(1, 10, z='test', y=True))
