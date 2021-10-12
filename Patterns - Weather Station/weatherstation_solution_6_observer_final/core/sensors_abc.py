from abc import abstractmethod

from core.observer_abc import Subject


class Sensor(Subject[float]):

    @abstractmethod
    def measure(self) -> float:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass
