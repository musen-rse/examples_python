from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


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
