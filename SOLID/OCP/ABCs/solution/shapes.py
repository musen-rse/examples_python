from core.shape_abc import Shape


class Circle(Shape):
    def __init__(self, radius=1.0):
        self._radius: float = radius

    @property
    def radius(self) -> float:
        return self._radius

    def draw(self):
        print(f"Draw circle with radius: {self.radius}.")


class Square(Shape):
    def __init__(self, length=1.0):
        self._length: float = length

    @property
    def length(self) -> float:
        return self._length

    def draw(self):
        print(f"Draw square with side length: {self.length}.")


class Rectangle(Shape):
    def __init__(self, side_a=1.0, side_b=1.0):
        self._side_a: float = side_a
        self._side_b: float = side_b

    def draw(self):
        print(f"Draw recangle with side length a:{self._side_a} \
            and side length b:{self._side_b}.")
