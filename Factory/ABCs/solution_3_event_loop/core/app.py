from typing import List
from core.shape_abc import Shape, ShapeFactory


class Application:
    def __init__(self, shape_factory: ShapeFactory):
        self.shape_factory = shape_factory
        self.shapes: List[Shape] = []

    def run(self):
        while True:
            self.draw_menu()
            shape_type = input("Enter a shape type or type 'quit' to end: ")
            if shape_type == "quit":
                break

            try:
                shape = self.shape_factory.create_shape(shape_type)
            except Exception as e:
                print(e)

            self.shapes.append(shape)
            self.draw_shapes()

    def draw_menu(self):
        print("Choose from the following shapes:")
        for choice in self.shape_factory.get_shape_choices():
            print(choice)

    def draw_shapes(self):
        print("----------------")
        print("Draw all shapes:")
        for shape in self.shapes:
            shape.draw()
        print("----------------")
