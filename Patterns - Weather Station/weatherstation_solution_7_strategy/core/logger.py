from typing import Any, TextIO
from core.observer_abc import Observer


class ObservingLogger(Observer[float]):
    
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file: TextIO = None

    def __enter__(self) -> 'ObservingLogger':
        self.open()
        return self

    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        self.close()

    def open(self) -> None:
        self.file = open(self.filename, "w")

    def close(self) -> None:
        self.file.close()

    def log(self, message: str) -> None:
        self.file.write(message + "\n")

    def update(self, sender: Any, value: float) -> None:
        self.log(f"{type(sender).__name__}: {value:.2f}")