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
