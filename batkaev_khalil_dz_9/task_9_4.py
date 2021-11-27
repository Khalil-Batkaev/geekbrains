class Car():

    def __init__(self, speed, color, name, is_police=False):
        self._speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police

    def go(self):
        print(f'Автомобиль {self._name} начал движение')

    def stop(self):
        print(f'Автомобиль {self._name} остановился')

    def turn(self, direction):
        print(f'Автомобиль {self._name} повернул на {direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self._name} - {self._speed}')


class TownCar(Car):
    __speed_limit = 60

    def show_speed(self):
        if self._speed <= self.__speed_limit:
            print(f'Текущая скорость автомобиля {self._name} - {self._speed}')
        else:
            print(f'Автомобиль {self._name} превысил допустимую скорость!')


class WorkCar(Car):
    __speed_limit = 40

    def show_speed(self):
        if self._speed <= self.__speed_limit:
            print(f'Текущая скорость автомобиля {self._name} - {self._speed}')
        else:
            print(f'Автомобиль {self._name} превысил допустимую скорость!')


class SportCar(Car):
    pass


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


auto_1 = Car(60, 'красный', 'Ceed')
auto_2 = PoliceCar(70, 'синий', 'Ford')
auto_3 = TownCar(50, 'жёлтый', 'Mazda')
auto_4 = WorkCar(60, 'черный', 'Lada', True)
auto_5 = SportCar(220, 'оранжевый', 'Ferrari')

auto_1.stop()
auto_2.turn('лево')
auto_3.go()
auto_4.show_speed()
auto_2.show_speed()
auto_5.show_speed()
print(auto_1._color)
print(auto_2._name)
print(auto_3._speed)
print(auto_5._name)
print(auto_3._is_police)
print(auto_4._is_police)
print(auto_2._is_police)
