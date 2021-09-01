from abc import ABC, abstractmethod
from core.sensors import TemperatureSensor

class Chart(ABC):

    @abstractmethod
    def update(self, sensor: TemperatureSensor):
        pass