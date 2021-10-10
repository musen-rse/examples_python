from core.shape import Shape


class Circle:
    def __init__(self, radius: float = 1.0) -> None:
        self._radius: float = radius

    @property
    def radius(self) -> float:
        return self._radius

    def draw(self) -> None:
        print(f"Draw circle with radius: {self.radius}.")


class Square:
    def __init__(self, length: float = 1.0) -> None:
        self._length: float = length

    @property
    def length(self) -> float:
        return self._length

    def draw(self) -> None:
        print(f"Draw square with side length: {self.length}.")


class Rectangle:
    def __init__(self, side_a: float = 1.0, side_b: float = 1.0):
        self._side_a: float = side_a
        self._side_b: float = side_b

    def draw(self) -> None:
        print(f"Draw recangle with side length a:{self._side_a} \
            and side length b:{self._side_b}.")
