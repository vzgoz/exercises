class Road:

    def __init__(self, width, length):
        self._width = width
        self._length = length
        self.weight = 50
        self.height = 20


    def mass(self):
        mass = self._length * self._width * self.weight * self.height / 1000
        print(f'Масса асфальта: {mass}')


result = Road (1000,30)
result.mass()


