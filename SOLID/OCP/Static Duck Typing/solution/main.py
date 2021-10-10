from typing import List
from core.shape import Shape
from shapes_impl import Circle, Square, Rectangle
from core.app import Application


def main() -> None:
    Application([Circle(1.0), Square(2.0), Rectangle(2.0, 3.0)]).run()


if __name__ == "__main__":
    main()
