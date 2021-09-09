from abc import ABC, abstractmethod
from enum import Enum, auto


class ChartColor(Enum):
    RED = auto()
    BLUE = auto()
    CYAN = auto()
    GREEN = auto()
    YELLOW = auto()
    WHITE = auto()


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


class ChartFactory(ABC):

    @abstractmethod
    def create_table_chart(self) -> Chart:
        pass

    @abstractmethod
    def create_bar_chart(self) -> Chart:
        pass
