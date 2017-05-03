class Celsius:

    ABSOLUTE_ZERO = -273

    def __init__(self, value=0):
        self._temperature = value

    def to_fahrenheit(self):
        return self.temperature * 1.8 + 32

    def set_temperature(self, value):
        if value < self.ABSOLUTE_ZERO:
            raise ValueError('Temperature below ', self.ABSOLUTE_ZERO, 'is not possible.')
        print("setting value")
        self._temperature = value

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    temperature = property(get_temperature, set_temperature)


c1 = Celsius(-100)
print(c1.get_temperature(), '=>', c1.to_fahrenheit())
c1.set_temperature(100)
print(c1.get_temperature(), '=>', c1.to_fahrenheit())
c1.temperature = 50
print(c1.get_temperature(), '=>', c1.to_fahrenheit())

