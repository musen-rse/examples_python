class Circle():
    def draw(self):
        print("Drawing Circle")


class Rectangle():
    def draw(self):
        print("Drawing Rectangle")


class Triangle():
    def draw(self):
        print("Drawing Triangle")


class ShapeFactory():
    def create_circle(self):
        return Circle()

    def create_rectangle(self):
        return Rectangle()

    def create_triangle(self):
        return Triangle()
