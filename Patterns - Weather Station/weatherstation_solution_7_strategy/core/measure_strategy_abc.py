from abc import ABC, abstractmethod
from typing import List

from core.sensors import Sensor


class MeasureStrategy(ABC):

    def __init__(self):
        self._sensors: List[Sensor] = []

    def add_sensor(self, sensor: Sensor):
        self._sensors.append(sensor)

    @abstractmethod
    def measure(self):
        pass
