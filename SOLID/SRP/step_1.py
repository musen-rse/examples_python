class Color:

    WHITE   = '\033[37m'
    BLUE    = '\033[94m'
    CYAN    = '\033[96m'
    GREEN   = '\033[92m'
    YELLOW  = '\033[93m'
    RED     = '\033[91m'
    DEFAULT = '\033[0m'


class Rectangle:

    def __init__(self, width: int, height: int, color: str):
        self._width = width
        self._height = height
        self._color = color

    def area(self) -> int:
        return self._width * self._height

    def perimeter(self) -> int:
        return 2 * (self._width + self._height)

    def __str__(self) -> str:
        return f"Rectangle({self._width}, {self._height})"

    def draw(self) -> None:
        for i in range(self._height):
            print(self._color + "*" * self._width + Color.DEFAULT)


###############################################################################
# Geometry App                                                                #
###############################################################################
class GeometryApp:
    
    def run(self) -> None:
        print("Console App")
        rectangle = Rectangle(2, 5, Color.RED)
        print(f"{rectangle} with area:{rectangle.area()} and perimeter:{rectangle.perimeter()}")


###############################################################################
# GUI App                                                                     #
###############################################################################
class GuiApp:

    def run(self) -> None:
        print("GUI app")
        rectangle = Rectangle(10, 5, Color.BLUE)
        rectangle.draw()


###############################################################################
# main.py                                                                     #
###############################################################################

if __name__ == '__main__':
    console_app = GeometryApp()
    console_app.run()

    print("---------------------")

    gui_app = GuiApp()
    gui_app.run()
    