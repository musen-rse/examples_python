1. Create a file called logger.py in `core` and paste in the following code

```python
class Logger:
    
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file: TextIO = None

    def __enter__(self) -> 'Logger':
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
```