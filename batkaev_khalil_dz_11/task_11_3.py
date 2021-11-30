class IsNumberError(Exception):

    def __init__(self, elem):
        self._elem = elem

    def __str__(self):
        return f'Вы ввели не число, а: {self._elem}. Если хотите остановиться, то введите "stop"'


numbers = []

while True:
    elem = input('Введите число: ')
    try:
        if elem[0] in '-' and elem[1:].isdigit() or elem.isdigit():
            numbers.append(int(elem))
        elif elem == 'stop':
            break
        else:
            raise IsNumberError(elem)
    except IsNumberError as e:
        print(e)
    except IndexError:
        print('Вы ничего не ввели. Если хотите остановиться, то введите "stop"')

print(numbers)
