class Circle:
    def __init__(self, radius: float = 1.0):
        self._radius: float = radius

    @property
    def radius(self) -> float:
        return self._radius


class Square:
    def __init__(self, length: float = 1.0):
        self._length: float = length

    @property
    def length(self) -> float:
        return self._length
