import random
from typing import List


class TemperatureSensor:

    def __init__(self):
        self._temperature = 20
        self._charts: List['Chart'] = []

    @property
    def temperature(self) -> int:
        return self._temperature

    @temperature.setter
    def temperature(self, value: int):
        self._temperature = value
        for chart in self._charts:
            chart.update(self)

    def attach_chart(self, view: 'Chart') -> None:
        self._charts.append(view)

    def measure(self):
        change = random.randint(-1, 1)
        self.temperature = self._temperature + change
