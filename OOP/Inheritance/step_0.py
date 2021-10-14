class Circle:

    def __init__(self, radius:float):
        self._radius = radius
        self._center_x = 0.
        self._center_y = 0.

    def translate(self, delta_x: float, delta_y: float) -> None:
        self._center_x += delta_x
        self._center_y -= delta_y

    def __str__(self) -> str:
        return f"Circle(center_x={self._center_x}, center_y={self._center_y}, radius={self._radius})"

    def draw(self) -> None:
        print(self)


class Rectangle:

    def __init__(self, width:float, height:float):
        self._width = width
        self._height = height
        self._center_x = 0.
        self._center_y = 0.

    def translate(self, delta_x: float, delta_y: float) -> None:
        self._center_x += delta_x
        self._center_y -= delta_y

    def __str__(self) -> str:
        return f"Rectangle(center_x={self._center_x}, center_y={self._center_y}, width={self._width}, height={self._height})"

    def draw(self) -> None:
        print(self)


class Triangle:

    def __init__(self, length:float):
        self._length = length
        self._center_x = 0.
        self._center_y = 0.

    def translate(self, delta_x: float, delta_y: float) -> None:
        self._center_x += delta_x
        self._center_y -= delta_y

    def __str__(self) -> str:
        return f"Triangle(center_x={self._center_x}, center_y={self._center_y}, length={self._length})"

    def draw(self) -> None:
        print(self)

    
class Hexagon:

    def __init__(self, length:float):
        self._length = length
        self._center_x = 0.
        self._center_y = 0.

    def translate(self, delta_x: float, delta_y: float) -> None:
        self._center_x += delta_x
        self._center_y -= delta_y

    def __str__(self) -> str:
        return f"Hexagon(center_x={self._center_x}, center_y={self._center_y}, length={self._length})"

    def draw(self) -> None:
        print(self)


class Square:
    
    def __init__(self, length:float):
        self._length = length
        self._center_x = 0.
        self._center_y = 0.

    def translate(self, delta_x: float, delta_y: float) -> None:
        self._center_x += delta_x
        self._center_y -= delta_y

    def __str__(self) -> str:
        return f"Square(center_x={self._center_x}, center_y={self._center_y}, length={self._length})"

    def draw(self) -> None:
        print(self)


if __name__ == "__main__":
    c = Circle(10.)
    c.translate(10., 10.)
    c.draw()

    r = Rectangle(10., 10.)
    r.translate(10., 10.)
    r.draw()

    t = Triangle(10.)
    t.translate(10., 10.)
    t.draw()

    h = Hexagon(10.)
    h.translate(10., 10.)
    h.draw()

    s = Square(10.)
    s.translate(10., 10.)
    s.draw()
