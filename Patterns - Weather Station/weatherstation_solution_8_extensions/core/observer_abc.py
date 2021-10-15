from abc import ABC, abstractmethod
from typing import Any, Generic, List, TypeVar

T = TypeVar('T')

class Observer(ABC, Generic[T]):
    @abstractmethod
    def update(self, sender: Any, value: T) -> None:
        pass


class Subject(ABC, Generic[T]):
    def __init__(self) -> None:
        self.observers: List[Observer[T]] = []

    def register(self, observer: Observer[T]) -> None:
        self.observers.append(observer)

    def unregister(self, observer: Observer[T]) -> None:
        self.observers.remove(observer)

    def notify_all(self, value: T) -> None:
        for observer in self.observers:
            observer.update(self, value)