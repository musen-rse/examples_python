from core.abstractions import Shape, ShapeFactory
from typing import List


class Circle(Shape):
    def draw(self):
        print("Drawing Circle")


class Rectangle(Shape):
    def draw(self):
        print("Drawing Rectangle")


class Triangle(Shape):
    def draw(self):
        print("Drawing Triangle")


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
