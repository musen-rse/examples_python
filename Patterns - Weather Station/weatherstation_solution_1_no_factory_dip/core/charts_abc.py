from abc import ABC, abstractmethod
from enum import Enum, auto


class ChartColor(Enum):
    WHITE = auto()
    BLUE = auto()
    CYAN = auto()
    GREEN = auto()
    YELLOW = auto()
    RED = auto()


class Chart(ABC):

    def __init__(self) -> None:
        self._color = ChartColor.WHITE

    @abstractmethod
    def draw(self, value: float) -> None:
        pass

    @property
    def color(self) -> ChartColor:
        return self._color

    @color.setter
    def color(self, value: ChartColor) -> None:
        self._color = value
