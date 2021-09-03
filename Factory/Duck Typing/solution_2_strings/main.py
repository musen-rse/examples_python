from core.app import Application
from shapes import ShapeFactory


def main() -> None:
    Application(ShapeFactory()).run()


if __name__ == "__main__":
    main()
