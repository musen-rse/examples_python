from core.app import Application, Rectangle

def main() -> None:
    Application([Rectangle(2.0, 3.0), Rectangle(4.0, 2.1)]).run()


if __name__ == "__main__":
    main()
