class Worker():

    def __init__(self, wage, bonus):
        self.__name = 'Khalil'
        self.__surname = 'Batkaev'
        self.__position = 'Developer'
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


work_october = Position(50000, 30000)
work_november = Position(50000, 40000)
print(work_october._Worker__position)
print(work_november._income)
print(work_october.get_full_name())
print(work_october.get_total_income())
print(work_november.get_total_income())
