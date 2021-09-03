from abc import ABC, abstractmethod
from core.observer_abc import Observer
from typing import Any, List


class Chart(Observer[float], ABC):

    @abstractmethod
    def draw(self, value: float) -> None:
        pass



class ChartFactory(ABC):

    @abstractmethod
    def create_chart(self, chart_type: str, title: str) -> Chart:
        pass

    @abstractmethod
    def get_chart_choices(self) -> List[str]:
        pass
