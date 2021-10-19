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


if __name__ == "__main__":
    c = Circle(10.)
    c.translate(10., 10.)
    c.draw()