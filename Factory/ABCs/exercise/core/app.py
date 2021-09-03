from shapes import Circle, Rectangle
from core.shape_abc import Shape
from typing import List


class Application:
    def run(self):
        shapes: List[Shape] = [Circle(), Rectangle()]

        for shape in shapes:
            shape.draw()
