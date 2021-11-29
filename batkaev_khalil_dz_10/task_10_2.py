from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, size, name=None):
        self.__size = size
        self.name = name
        self.__reserved_fabric = 0

    def __str__(self):
        return str(round(self.__reserved_fabric, 4))

    def __add__(self, other):
        if not self.__reserved_fabric:
            self.__reserved_fabric = self.fabric_calculation + other.fabric_calculation
        else:
            self.__reserved_fabric += other.fabric_calculation
        return self

    @abstractmethod
    def fabric_calculation(self):
        pass

    @property
    def get_size(self):
        return self.__size


class Coat(Clothes):
    __calculation_args = [6.5, 0.5]

    @property
    def fabric_calculation(self):
        self.__result = round(self.get_size / self.__calculation_args[0] + self.__calculation_args[1], 4)
        return self.__result


class Costume(Clothes):
    __calculation_args = [2, 0.3]

    @property
    def fabric_calculation(self):
        self.__result = round(self.get_size * self.__calculation_args[0] + self.__calculation_args[1], 4)
        return self.__result


coat_1, coat_2, coat_3 = Coat(48), Coat(56, 'Элегант'), Coat(62)
costume_1, costume_2, costume_3 = Costume(188, 'Мажор'), Costume(176), Costume(180)

print(coat_1.fabric_calculation, coat_2.fabric_calculation, coat_3.fabric_calculation, sep='\n')
print()
print(costume_1.fabric_calculation, costume_2.fabric_calculation, costume_3.fabric_calculation, sep='\n')
print()
total_fabric_for_coats = coat_1 + coat_2 + coat_3
total_fabric_for_costumes = costume_1 + costume_2 + costume_3
print(total_fabric_for_coats, total_fabric_for_costumes, sep='\n')
print()
print(coat_2.name, costume_1.name, sep='\n')
