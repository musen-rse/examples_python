import random

from core.sensors_abc import Sensor


class TemperatureSensor(Sensor):

    def __init__(self):
        super().__init__()
        self._temperature = 20

    def measure(self):
        change = random.randint(-5, 5)
        self.temperature = self._temperature + change

        self.draw_all(self.temperature)

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        self._temperature = temperature

    @property
    def physical_quantity(self) -> str:
        return "Temperature"


class HumiditySensor(Sensor):

    def __init__(self):
        super().__init__()
        self._humidity = 40

    def measure(self):
        change = random.randint(-2, 2)
        self.humidity = self._humidity + change

        self.draw_all(self.humidity)

    @property
    def humidity(self):
        return self._humidity

    @humidity.setter
    def humidity(self, humidity):
        self._humidity = humidity

    @property
    def physical_quantity(self) -> str:
        return "Humidity"
