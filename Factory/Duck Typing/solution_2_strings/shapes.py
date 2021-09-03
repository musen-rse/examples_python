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
    def __init__(self):
        self.shape_choices = ['circle', 'rectangle', 'triangle']

    def create_shape(self, shape_type):
        if shape_type == 'circle':
            return Circle()
        elif shape_type == 'rectangle':
            return Rectangle()
        elif shape_type == 'triangle':
            return Triangle()
        else:
            raise ValueError('Invalid shape')

    def get_shape_choices(self):
        return self.shape_choices
