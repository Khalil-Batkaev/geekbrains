class ComplexNumber:

    def __init__(self, real_part, imaginary_part):
        self.__real_part = real_part
        self.__imaginary_part = imaginary_part

    def __str__(self):
        return f'{self.__real_part}{self.__imaginary_part:+d}j'

    def __add__(self, other):
        self._new_real_part = self.__real_part + other.__real_part
        self._new_imaginary_part = self.__imaginary_part + other.__imaginary_part
        return ComplexNumber(self._new_real_part, self._new_imaginary_part)

    def __sub__(self, other):
        self._new_real_part = self.__real_part - other.__real_part
        self._new_imaginary_part = self.__imaginary_part - other.__imaginary_part
        return ComplexNumber(self._new_real_part, self._new_imaginary_part)

    def __mul__(self, other):
        self._new_real_part = self.__real_part * other.__real_part - self.__imaginary_part * other.__imaginary_part
        self._new_imaginary_part = self.__real_part * other.__imaginary_part + self.__imaginary_part * other.__real_part
        return ComplexNumber(self._new_real_part, self._new_imaginary_part)


complex_1 = ComplexNumber(7, 1)
complex_2 = ComplexNumber(3, -5)
complex_3 = ComplexNumber(-9, 4)
print(complex_1, complex_2, complex_3, sep='\n')
print()
complex_4 = complex_1 + complex_2
complex_5 = complex_2 - complex_3
complex_6 = complex_1 * complex_3
print(complex_4, complex_5, complex_6, sep='\n')
