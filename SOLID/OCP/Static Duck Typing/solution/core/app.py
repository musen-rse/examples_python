from typing import List
from core.shape import Shape


class Application:
    def __init__(self, shapes: List[Shape]) -> None:
        self._shapes: List[Shape] = shapes

    def run(self) -> None:
        for shape in self._shapes:
            shape.draw()
