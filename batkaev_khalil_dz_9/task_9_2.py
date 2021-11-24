class Road():
    __asphalt_mass = 25
    __asphalt_thickness = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_asphalt_mass(self):
        result_asphalt_mass = round(self._length * self._width * self.__asphalt_mass / 1000 * self.__asphalt_thickness)
        return result_asphalt_mass


road_1 = Road(5000, 12)
road_2 = Road(20000, 6)
print(road_1.calc_asphalt_mass())
print(road_2.calc_asphalt_mass())
