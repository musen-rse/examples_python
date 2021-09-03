import math
from core.app import Application
from shapes import Circle, Square


def main() -> None:
    Application([Circle(1.0), Square(2.0)]).run()


if __name__ == "__main__":
    main()
