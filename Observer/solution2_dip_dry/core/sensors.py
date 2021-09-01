import random

from core.sensors_abc import Sensor


class TemperatureSensor(Sensor):

    def __init__(self):
        super().__init__()
        self._temperature = 20

    @property
    def temperature(self) -> int:
        return self._temperature

    @temperature.setter
    def temperature(self, value: int):
        self._temperature = value
        self.update_charts()

    def measure(self):
        change = random.randint(-1, 1)
        self.temperature = self._temperature + change


class HumiditySensor(Sensor):

    def __init__(self):
        super().__init__()
        self._humidity = 20

    def measure(self):
        change = random.randint(-5, 5)
        self.humidity = self._humidity + change

    @property
    def humidity(self):
        return self._humidity

    @humidity.setter
    def humidity(self, humidity):
        self._humidity = humidity
        self.update_charts()
