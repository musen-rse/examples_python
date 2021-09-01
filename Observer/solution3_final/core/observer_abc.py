from abc import ABC, abstractmethod
from typing import Any, List


class Observer(ABC):
    @abstractmethod
    def update(self, sender: Any, *args, **kwargs):
        pass


class Subject(ABC):
    def __init__(self) -> None:
        self.observers: List[Observer] = []

    def register(self, observer: Observer) -> None:
        self.observers.append(observer)

    def unregister(self, observer: Observer) -> None:
        self.observers.remove(observer)

    def notify_all(self, *args, **kwargs) -> None:
        for observer in self.observers:
            observer.update(self, *args, **kwargs)