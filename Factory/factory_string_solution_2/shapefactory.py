from abc import ABC, abstractmethod
from typing import List
from common.shapes import Circle, Rectangle, Shape, Triangle


class ShapeFactory(ABC):
    @abstractmethod
    def create_shape(self, shape: str) -> Shape:
        pass

    @abstractmethod
    def get_shape_choices(self) -> List[str]:
        pass


class ShapeFactoryImpl(ShapeFactory):
    def __init__(self):
        self.shape_choices = ['circle', 'rectangle', 'triangle']

    def create_shape(self, shape: str) -> Shape:
        if shape == 'circle':
            return Circle()
        elif shape == 'rectangle':
            return Rectangle()
        elif shape == 'triangle':
            return Triangle()
        else:
            raise ValueError('Invalid shape')

    def get_shape_choices(self) -> List[str]:
        return self.shape_choices