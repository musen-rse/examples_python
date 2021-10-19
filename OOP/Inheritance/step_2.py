from abc import ABC


class Shape(ABC):

    def __init__(self) -> None:
        self._center_x = 0.
        self._center_y = 0.
    
    def translate(self, delta_x: float, delta_y: float) -> None:
        self._center_x += delta_x
        self._center_y += delta_y

    def draw(self) -> None:
        print(self)


class Circle(Shape):

    def __init__(self, radius:float):
        super().__init__()
        self._radius = radius
        
    def __str__(self) -> str:
        return f"Circle(center_x={self._center_x}, center_y={self._center_y}, radius={self._radius})"


class Rectangle(Shape):

    def __init__(self, width:float, height:float):
        super().__init__()
        self._width = width
        self._height = height

    def __str__(self) -> str:
        return f"Rectangle(center_x={self._center_x}, center_y={self._center_y}, width={self._width}, height={self._height})"


class Triangle(Shape):

    def __init__(self, length:float):
        super().__init__()
        self._length = length

    def __str__(self) -> str:
        return f"Triangle(center_x={self._center_x}, center_y={self._center_y}, length={self._length})"

    
class Hexagon(Shape):

    def __init__(self, length:float):
        super().__init__()
        self._length = length

    def __str__(self) -> str:
        return f"Hexagon(center_x={self._center_x}, center_y={self._center_y}, length={self._length})"


class Square(Shape):
    
    def __init__(self, length:float):
        super().__init__()
        self._length = length

    def __str__(self) -> str:
        return f"Square(center_x={self._center_x}, center_y={self._center_y}, length={self._length})"


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
