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
