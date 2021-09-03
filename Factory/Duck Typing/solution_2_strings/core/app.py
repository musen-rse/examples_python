class Application:
    def __init__(self, shape_factory):
        self.shape_factory = shape_factory

    def run(self):
        shapes = [
            self.shape_factory.create_shape("circle"),
            self.shape_factory.create_shape("rectangle"),
            self.shape_factory.create_shape("triangle")
        ]

        for shape in shapes:
            shape.draw()
