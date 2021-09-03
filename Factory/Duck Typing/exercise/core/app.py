from shapes import Circle, Rectangle


class Application:
    def run(self):
        shapes = []

        shapes.append(Circle())
        shapes.append(Rectangle())

        for shape in shapes:
            shape.draw()
