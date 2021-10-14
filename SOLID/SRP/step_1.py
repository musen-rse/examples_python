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

    def draw(self) -> None:
        for i in range(self._height):
            print("*" * self._width)


###############################################################################
# gui_app.py                                                                  #
###############################################################################
class GuiApp:

    def run(self) -> None:
        print("GUI app")
        rectangle = Rectangle(10, 5)
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
    