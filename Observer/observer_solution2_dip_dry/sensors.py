import random

from abc import ABC
from typing import List


class Sensor(ABC):

    def __init__(self) -> None:
        self._charts: List['Chart'] = []

    def attach_chart(self, view: 'Chart') -> None:
        self._charts.append(view)

    def update_charts(self) -> None:
        for chart in self._charts:
            chart.update(self)


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
