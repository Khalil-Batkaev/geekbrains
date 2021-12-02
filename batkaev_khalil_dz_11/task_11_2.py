class MyZeroDivisionError(Exception):

    def __init__(self, divisible, divisor):
        self._divisible = divisible
        self._divisor = divisor

    def __str__(self):
        return f'Невозможно разделить {self._divisible} на {self._divisor}!'


def division(divisible, divisor):
    if divisor:
        return divisible / divisor
    else:
        raise MyZeroDivisionError(divisible, divisor)


try:
    number_1 = division(5, 2)
    number_2 = division(0, -5)
    print(number_1, number_2, sep='\n')
    number_3 = division(5, 0)
except MyZeroDivisionError as e:
    print(e)
