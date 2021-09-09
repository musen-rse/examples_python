from abc import ABC, abstractmethod
from enum import Enum, auto
from core.observer_abc import Observer
from typing import Any, List


class ChartColor(Enum):
    RED = auto()
    BLUE = auto()
    CYAN = auto()
    GREEN = auto()
    YELLOW = auto()
    WHITE = auto()


class Chart(Observer[float], ABC):

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
    def create_chart(self, chart_type: str, title: str) -> Chart:
        pass

    @abstractmethod
    def get_chart_choices(self) -> List[str]:
        pass
