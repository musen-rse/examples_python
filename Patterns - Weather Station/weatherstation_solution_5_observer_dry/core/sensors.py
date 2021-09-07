import random
from abc import ABC, abstractmethod
from typing import List

from core.charts_abc import Chart


class Sensor(ABC):
    def __init__(self) -> None:
        self.charts: List[Chart] = []

    def add_chart(self, chart: Chart) -> None:
        self.charts.append(chart)

    def remove_chart(self, chart: Chart) -> None:
        self.charts.remove(chart)

    def draw_all(self, value: float) -> None:
        for chart in self.charts:
            chart.draw(value)

    @abstractmethod
    def measure(self) -> float:
        pass

    @property
    @abstractmethod
    def physical_quantity(self) -> str:
        pass


class TemperatureSensor(Sensor):

    def __init__(self):
        super().__init__()
        self._temperature = 20

    def measure(self):
        change = random.randint(-5, 5)
        self.temperature = self._temperature + change

        self.draw_all(self.temperature)

    @property
    def physical_quantity(self) -> str:
        return "Temperature"

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        self._temperature = temperature


class HumiditySensor(Sensor):

    def __init__(self):
        super().__init__()
        self._humidity = 40

    def measure(self):
        change = random.randint(-2, 2)
        self.humidity = self._humidity + change

        self.draw_all(self.humidity)

    @property
    def physical_quantity(self) -> str:
        return "Humidity"

    @property
    def humidity(self):
        return self._humidity

    @humidity.setter
    def humidity(self, humidity):
        self._humidity = humidity
