class Cell:

    def __init__(self, quantity):
        self.__quantity = quantity

    def __str__(self):
        return str(self.__quantity)

    def __add__(self, other):
        result = self.__quantity + other.__quantity
        return Cell(result)

    def __sub__(self, other):
        if self.__quantity >= other.__quantity:
            result = self.__quantity - other.__quantity
        else:
            raise ValueError('Начальное количество клеток меньше вычитаемого')
        return Cell(result)

    def __mul__(self, other):
        result = self.__quantity * other.__quantity
        return Cell(result)

    def __floordiv__(self, other):
        result = self.__quantity // other.__quantity
        return Cell(result)

    def make_order(self, quantity):
        rows = self.__quantity // quantity
        remainder = self.__quantity % quantity
        if not remainder:
            line = ('*' * quantity + '\\n') * (rows - 1) + '*' * quantity
        else:
            line = ('*' * quantity + '\\n') * rows + '*' * remainder
        return line


cell_1 = Cell(5)
cell_2 = Cell(10)
cell_3 = cell_1 + cell_2
cell_4 = cell_2 - cell_1
cell_5 = cell_1 * cell_2
cell_6 = cell_2 // cell_1
print(cell_3, cell_3.make_order(5))
print(cell_4, cell_4.make_order(2))
print(cell_5, cell_5.make_order(15))
print(cell_6, cell_6.make_order(2))
try:
    cell_4 = cell_1 - cell_2
except ValueError as e:
    print(e)
