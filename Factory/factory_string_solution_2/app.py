from factory_string_solution.shapefactory import ShapeFactory


class Application:
    def __init__(self, shape_factory: ShapeFactory):
        self.shape_factory = shape_factory

    def run(self):
        while True:
            shape_type = input("Enter a shape type: ")
            if shape_type == "quit":
                break

            try:
                shape = self.shape_factory.create_shape(shape_type)
                shape.draw()
            except Exception as e:
                print(e)
