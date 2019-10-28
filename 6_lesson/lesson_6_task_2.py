class Road:
    width_road = 3

    def __init__(self, length, width, mass):
        self._length = length
        self._width = width
        self._mass = mass

    def mass_calculation(self):
        return self._length * self._width * self._mass * Road.width_road

road_1 = Road(200, 8, 20)
print(road_1.mass_calculation())