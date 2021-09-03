from abc import ABC, abstractmethod
from typing import List


class Chart(ABC):

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
