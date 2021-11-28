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
    def clear_reserved_fabric(self):
        self.__reserved_fabric.clear()

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


coat_1, coat_2, coat_3, coat_4 = Coat(48), Coat(56), Coat(62), Coat(70)
costume_1, costume_2, costume_3, costume_4 = Costume(188), Costume(176), Costume(180), Costume(168)

print(coat_1.fabric_calculation)
print(costume_2.fabric_calculation)
total_fabric_for_coats = coat_1 + coat_2 + coat_3 + coat_4
print(total_fabric_for_coats)
total_fabric_for_costumes = costume_1 + costume_2 + costume_3
print(total_fabric_for_costumes)
new_total_fabric_for_costumes = total_fabric_for_costumes + costume_4
print(new_total_fabric_for_costumes)

total_fabric_for_costumes.clear_reserved_fabric
total_fabric_for_costumes = costume_1 + costume_4
print(total_fabric_for_costumes)

'''
Можно так методы добавить в класс-родитель вместо перегрузки __str__ и __add__, но тогда вызов итоговой цифры идёт 
через экземпляр, а это мне не очень нравится...

    # @property
    # def add_to_reserve(self):
    #     self.__reserved_fabric.append(self.fabric_calculation)
    #
    # @property
    # def show_reserved_fabric(self):
    #     return sum(self.__reserved_fabric)
    
    coat_1.add_to_reserve
    coat_2.add_to_reserve
    coat_3.add_to_reserve
    coat_4.add_to_reserve
    coat_1.show_reserved_fabric    
'''