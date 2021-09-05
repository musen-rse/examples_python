from shapes import Circle, Square


def _draw_circle(radius):
    print(f"Draw circle with radius: {radius}.")


def _draw_square(length):
    print(f"Draw square with side length: {length}.")


class Application:
    def __init__(self, shapes) -> None:
        self._shapes = shapes

    def run(self) -> None:
        for shape in self._shapes:
            if type(shape) is Circle:
                _draw_circle(shape.radius)
            if type(shape) is Square:
                _draw_square(shape.length)
