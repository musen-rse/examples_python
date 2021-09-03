from abc import ABC, abstractmethod

class Chart(ABC):

    @abstractmethod
    def draw(self, value: float) -> None:
        pass