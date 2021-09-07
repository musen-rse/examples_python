from core.rectangle import Rectangle
from square import Square
from core.app import Application

class Square(Rectangle):
    def __init__(self, width=1.0):
        self._height = width
        self._width = width

    def set_height(self, height: float):
        self._height = height
        self._width = height
    
    def set_width(self, width: float):
        self._width = width
        self._height = width


def main() -> None:
    Application([Rectangle(2.0, 3.0), Square(4.0)]).run()


if __name__ == "__main__":
    main()
