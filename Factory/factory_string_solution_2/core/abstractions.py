from abc import ABC, abstractmethod
from typing import List


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class ShapeFactory(ABC):
    @abstractmethod
    def create_shape(self, shape: str) -> Shape:
        pass

    @abstractmethod
    def get_shape_choices(self) -> List[str]:
        pass
