from core.abstractions import Shape


class Circle(Shape):
    def draw(self):
        print("Drawing Circle")


class Rectangle(Shape):
    def draw(self):
        print("Drawing Rectangle")
