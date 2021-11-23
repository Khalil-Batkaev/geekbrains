from time import sleep
from itertools import cycle


class TrafficLight():
    __color = None

    def __init__(self, red_duration, yellow_duration, green_duration):
        self.colors = dict()
        self.colors['red'] = red_duration
        self.colors['yellow'] = yellow_duration
        self.colors['green'] = green_duration

    def state(self):
        print(self.__color)

    def running(self):
        colors = ['red', 'yellow', 'green', 'yellow']
        try:
            for color in cycle(colors):
                self.__color = color
                self.state()
                sleep(self.colors[color])
        except KeyboardInterrupt:
            print(f'Светофор выключен инспектором. Текущий цвет - {color}.')


traffic_light_1 = TrafficLight(7, 2, 10)
traffic_light_1.running()
