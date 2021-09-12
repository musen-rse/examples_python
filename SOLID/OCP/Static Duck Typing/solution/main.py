from core.app import Application
from shapes import Circle, Square, Rectangle


def main() -> None:
    Application([Circle(1.0), Square(2.0), Rectangle(2.0, 3.0)]).run()


if __name__ == "__main__":
    main()
