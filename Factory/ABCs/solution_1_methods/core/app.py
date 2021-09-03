from typing import List
from core.shape_abc import Shape, ShapeFactory


class Application:
    def __init__(self, shape_factory: ShapeFactory):
        self.shape_factory = shape_factory

    def run(self):
        shapes: List[Shape] = [
            self.shape_factory.create_circle(),
            self.shape_factory.create_rectangle(),
            self.shape_factory.create_triangle(),
        ]

        for shape in shapes:
            shape.draw()
