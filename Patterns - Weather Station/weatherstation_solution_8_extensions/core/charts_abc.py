from abc import ABC, abstractmethod
from enum import Enum
from core.observer_abc import Observer
from typing import List
import random


class ChartColor(str, Enum):
    RED = "red"
    BLUE = "blue"
    CYAN = "cyan"
    GREEN = "green"
    YELLOW = "yellow"
    WHITE = "white"

    @staticmethod
    def random_color() -> 'ChartColor':
        list_of_colors = list(ChartColor)
        random_index_without_white = random.randint(0, len(list_of_colors) - 2)
        return list_of_colors[random_index_without_white]

class Chart(Observer):

    def __init__(self) -> None:
        self._color = ChartColor.GREEN

    def set_color(self, value: ChartColor) -> None:
        self._color = value


class ChartFactory(ABC):

    @abstractmethod
    def create_chart(self, chart_type: str, title: str) -> Chart:
        pass

    @abstractmethod
    def get_chart_types(self) -> List[str]:
        pass
