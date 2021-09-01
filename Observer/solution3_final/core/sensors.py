import random
from core.observer_abc import Subject


class HumiditySensor(Subject):

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
        self.notify_all(humidity)


class TemperatureSensor(Subject):

    def __init__(self):
        super().__init__()
        self._temperature = 20

    def measure(self):
        change = random.randint(-1, 1)
        self.temperature = self._temperature + change

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        self._temperature = temperature
        self.notify_all(temperature)