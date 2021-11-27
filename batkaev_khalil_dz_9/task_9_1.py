from time import sleep
from itertools import cycle


class TrafficLight:
    __colors = ['red', 'yellow', 'green', 'yellow']

    def __init__(self, red_duration, yellow_duration, green_duration):
        self.__color = None
        self.colors_dur = dict()
        self.colors_dur['red'] = red_duration
        self.colors_dur['yellow'] = yellow_duration
        self.colors_dur['green'] = green_duration

    def state(self):
        print(self.__color)

    def running(self):
        try:
            for color in cycle(self.__colors):
                self.__color = color
                self.state()
                sleep(self.colors_dur[color])
        except KeyboardInterrupt:
            print(f'Светофор выключен инспектором. Текущий цвет - {color}.')


traffic_light_1 = TrafficLight(7, 2, 10)
traffic_light_1.running()
