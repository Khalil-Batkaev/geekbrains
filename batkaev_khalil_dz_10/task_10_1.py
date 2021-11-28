class Matrix:

    def __init__(self, matrix_list):
        is_valid = False
        if isinstance(matrix_list, list):
            el_quantity = len(matrix_list[0])
            for item in matrix_list:
                if isinstance(item, list) and len(item) == el_quantity:
                    is_valid = True
                else:
                    is_valid = False
                    break
        if is_valid:
            self.__matrix = matrix_list
            self.__rows = len(matrix_list)
            self.__cols = len(matrix_list[0])
        else:
            raise ValueError(matrix_list)

    def __str__(self):
        matrix_line = ''
        for i in range(self.__rows):
            for j in range(self.__cols):
                if j == 0:
                    matrix_line += f'|{str(self.__matrix[i][j]).rjust(5)}'
                elif j == self.__cols - 1:
                    matrix_line += f'{str(self.__matrix[i][j]).rjust(5)}  |\n'
                else:
                    matrix_line += str(self.__matrix[i][j]).rjust(5)
        return matrix_line

    def __add__(self, other):
        if self.__cols == other.__cols and self.__rows == other.__rows:
            new_matrix = []
            for i in range(self.__rows):
                tmp = []
                for j in range(self.__cols):
                    el = self.__matrix[i][j] + other.__matrix[i][j]
                    tmp.append(el)
                new_matrix.append(tmp)
            return Matrix(new_matrix)
        else:
            raise ValueError('Разная размерность матриц')


try:
    matrix_1 = Matrix([[10, 500, 3], [300, 2, 1], [25, 4, 700]])
    print(matrix_1)
    matrix_2 = Matrix([[150, 50, 20], [30, 12, 5], [5, 47, 60]])
    print(matrix_2)
    matrix_3 = matrix_1 + matrix_2
    print(matrix_3)
    # # Некорректные данные
    # matrix_wrong_1 = Matrix([[150, 50, 20], 30, 12, 5, [5, 47, 60]])
    # matrix_wrong_2 = Matrix([[150, 50, 20], [30, 12, 5, 10], [5, 47, 60]])
    # # Разная размерность матриц
    matrix_4 = Matrix([[150, 50], [30, 12], [5, 47]])
    matrix_6 = matrix_1 + matrix_4
    print(matrix_6)
    # matrix_5 = Matrix([[10, 5, 20], [30, 12, 5], [5, 47, 60], [1, 2, 3]])
    # matrix_7 = matrix_1 + matrix_5
    # print(matrix_7)
except ValueError as e:
    print('Введены неверные данные:', e)
