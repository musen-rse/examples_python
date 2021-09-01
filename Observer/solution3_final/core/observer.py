from abc import abstractmethod
from typing import Any


class Observer:
    @abstractmethod
    def update(self, sender: Any, *args, **kwargs):
        pass
