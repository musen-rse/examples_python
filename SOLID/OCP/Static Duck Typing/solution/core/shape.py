from typing import Protocol
from abc import abstractmethod


class Shape(Protocol):
    def draw(self) -> None:
        raise NotImplementedError
