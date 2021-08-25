from abc import ABC, abstractmethod
from common.shapes import Shape, Circle, Rectangle, Triangle


class ShapeFactory(ABC):
    @abstractmethod
    def create_circle(self):
        pass

    @abstractmethod
    def create_rectangle(self):
        pass

    @abstractmethod
    def create_triangle(self):
        pass


class ShapeFactoryImpl(ShapeFactory):
    def create_circle(self):
        return Circle()

    def create_rectangle(self):
        return Rectangle()

    def create_triangle(self):
        return Triangle()
