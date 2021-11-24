class Worker():

    def __init__(self, name, surname, position, wage, bonus):
        self.__name = name
        self.__surname = surname
        self.__position = position
        self._income = dict()
        self._income['wage'] = wage
        self._income['bonus'] = bonus

    def getter_full_name(self):
        return f'{self.__name} {self.__surname}'


class Position(Worker):

    def get_full_name(self):
        return self.getter_full_name()

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


worker_khb = Position('Khalil', 'Batkaev', 'Developer', 50000, 40000)
worker_rm = Position('Roman', 'Kosov', 'Manager', 30000, 20000)
print(worker_khb._Worker__position)
print(worker_rm._income)
print(worker_khb.get_full_name())
print(worker_khb.get_total_income())
print(worker_rm.get_full_name())
print(worker_rm.get_total_income())
