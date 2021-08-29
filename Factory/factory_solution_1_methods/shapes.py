from core.abstractions import Shape, ShapeFactory


class Circle(Shape):
    def draw(self):
        print("Drawing Circle")


class Rectangle(Shape):
    def draw(self):
        print("Drawing Rectangle")


class Triangle(Shape):
    def draw(self):
        print("Drawing Triangle")


class ShapeFactoryImpl(ShapeFactory):
    def create_circle(self):
        return Circle()

    def create_rectangle(self):
        return Rectangle()

    def create_triangle(self):
        return Triangle()
