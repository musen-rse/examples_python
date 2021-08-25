from common.shapes import Circle, Rectangle, Triangle


class Application:
    def run(self):
        shapes = []

        shapes.append(Circle())
        shapes.append(Rectangle())
        shapes.append(Triangle())

        for shape in shapes:
            shape.draw()
