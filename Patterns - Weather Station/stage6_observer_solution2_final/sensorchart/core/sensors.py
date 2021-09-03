import random

from sensorchart.core.observer_abc import Subject


class TemperatureSensor(Subject[float]):

    def __init__(self):
        super().__init__()
        self._temperature = 20

    def measure(self):
        change = random.randint(-5, 5)
        self.temperature = self._temperature + change

        self.notify_all(self.temperature)

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        self._temperature = temperature


class HumiditySensor(Subject[float]):

    def __init__(self):
        super().__init__()
        self._humidity = 40

    def measure(self):
        change = random.randint(-2, 2)
        self.humidity = self._humidity + change

        self.notify_all(self.humidity)

    @property
    def humidity(self):
        return self._humidity

    @humidity.setter
    def humidity(self, humidity):
        self._humidity = humidity
