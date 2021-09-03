import random
from typing import List

from sensorchart.charts import Chart


class TemperatureSensor:

    def __init__(self):
        super().__init__()
        self._temperature = 20
        self._charts: List[Chart] = []

    def add_chart(self, chart: Chart):
        self._charts.append(chart)

    def remove_chart(self, chart: Chart):
        self._charts.remove(chart)

    def measure(self):
        change = random.randint(-5, 5)
        self.temperature = self._temperature + change
        
        for chart in self._charts:
            chart.draw(self.temperature)

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        self._temperature = temperature
