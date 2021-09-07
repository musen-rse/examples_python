from abc import ABC, abstractmethod
from typing import List

from core.sensors_abc import Sensor


class MeasureStrategy(ABC):

    def __init__(self):
        self._sensors: List[Sensor] = []

    def add_sensor(self, sensor: Sensor):
        self._sensors.append(sensor)

    @abstractmethod
    def measure(self):
        pass

    def _measure_all_sensors(self):
        for sensor in self._sensors:
            sensor.measure()

    def _clear_console(self):
        print("\033[2J", flush=True)