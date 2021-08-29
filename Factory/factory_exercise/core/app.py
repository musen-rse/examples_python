from shapes import Circle, Rectangle
from core.abstractions import Shape


class Application:
    def run(self):
        shapes: List[Shape] = []

        shapes.append(Circle())
        shapes.append(Rectangle())

        for shape in shapes:
            shape.draw()
