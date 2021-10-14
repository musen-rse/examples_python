from typing import Protocol


class Shape(Protocol):
    def draw(self) -> None:
        raise NotImplementedError
