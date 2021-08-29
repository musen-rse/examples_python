from factory_method_solution.shapefactory import ShapeFactory


class Application:
    def __init__(self, shape_factory: ShapeFactory):
        self.shape_factory = shape_factory

    def run(self):
        shapes = [
            self.shape_factory.create_circle(),
            self.shape_factory.create_rectangle(),
            self.shape_factory.create_triangle(),
        ]

        for shape in shapes:
            shape.draw()
