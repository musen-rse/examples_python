from abc import ABC, abstractmethod
from core.sensors_abc import Sensor

class Chart(ABC):

    @abstractmethod
    def update(self, sensor: Sensor):
        pass