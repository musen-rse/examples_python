from core.app import Application
from shapes import ShapeFactoryImpl


def main() -> None:
    Application(ShapeFactoryImpl()).run()


if __name__ == "__main__":
    main()
