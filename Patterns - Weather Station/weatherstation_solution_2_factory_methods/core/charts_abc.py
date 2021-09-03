from abc import ABC, abstractmethod

class Chart(ABC):

    @abstractmethod
    def draw(self, value: float) -> None:
        pass


class ChartFactory(ABC):

    @abstractmethod
    def create_table_chart(self) -> Chart:
        pass

    @abstractmethod
    def create_bar_chart(self) -> Chart:
        pass