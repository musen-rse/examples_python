from abc import ABC, abstractmethod
from typing import List

from core.sensors_abc import Sensor


class MeasureStrategy(ABC):

    def __init__(self, sensors: List[Sensor]):
        self._sensors = sensors

    @abstractmethod
    def measure(self):
        pass
