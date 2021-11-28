from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, size):
        self.__size = size
        self.__reserved_fabric = []

    def __str__(self):
        return str(sum(self.__reserved_fabric))

    def __add__(self, other):
        if len(self.__reserved_fabric):
            self.__reserved_fabric.append(other.fabric_calculation)
        else:
            self.__reserved_fabric.extend([self.fabric_calculation, other.fabric_calculation])
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


coat_1, coat_2, coat_3 = Coat(48), Coat(56), Coat(62)
costume_1, costume_2, costume_3 = Costume(188), Costume(176), Costume(180)

print(coat_1.fabric_calculation, coat_2.fabric_calculation, coat_3.fabric_calculation, sep='\n')
print()
print(costume_1.fabric_calculation, costume_2.fabric_calculation, costume_3.fabric_calculation, sep='\n')
print()
total_fabric_for_coats = coat_1 + coat_2 + coat_3
total_fabric_for_costumes = costume_1 + costume_2 + costume_3
print(total_fabric_for_coats, total_fabric_for_costumes, sep='\n')
