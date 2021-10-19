class Color:

    WHITE   = '\033[37m'
    BLUE    = '\033[94m'
    CYAN    = '\033[96m'
    GREEN   = '\033[92m'
    YELLOW  = '\033[93m'
    RED     = '\033[91m'
    DEFAULT = '\033[0m'


###############################################################################
# rectangle.py                                                                #
###############################################################################

class Rectangle:

    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    def area(self) -> int:
        return self._width * self._height

    def perimeter(self) -> int:
        return 2 * (self._width + self._height)

    def __str__(self) -> str:
        return f"Rectangle({self._width}, {self._height})"
    
    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height


###############################################################################
# graphical_rectangle.py                                                      #
###############################################################################

class GraphicalRectangle:

    def __init__(self, rectangle: Rectangle, color: str):
        self._rectangle = rectangle
        self._color = color

    def draw(self) -> None:
        for i in range(self._rectangle.height):
            print(self._color + "*" * self._rectangle.width + Color.DEFAULT)



###############################################################################
# gui_app.py                                                                  #
###############################################################################
class GuiApp:

    def run(self) -> None:
        print("GUI app")
        rectangle = GraphicalRectangle(Rectangle(10, 5), Color.RED)
        rectangle.draw()


###############################################################################
# geometry_app.py                                                             #
###############################################################################
class GeometryApp:
    
    def run(self) -> None:
        print("Console App")
        rectangle = Rectangle(2, 5)
        print(f"{rectangle} with area:{rectangle.area()} and perimeter:{rectangle.perimeter()}")


###############################################################################
# main.py                                                                     #
###############################################################################

if __name__ == '__main__':
    console_app = GeometryApp()
    console_app.run()

    print("---------------------")

    gui_app = GuiApp()
    gui_app.run()
    