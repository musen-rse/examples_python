from typing import List
from core.rectangle import Rectangle
from square import Square


class Application:
    def __init__(self, rectangles) -> None:
        self._rectangles: List[Rectangle] = rectangles

    def run(self) -> None:
        for rect in self._rectangles:
            self._set_size(rect, 3.0, 4.0)

    def _set_size(self, rect: Rectangle, width: float, height: float):
        rect.set_width(width)
        rect.set_height(height)
        #print(f"Type of rect {type(rect)}")
        if isinstance(rect, Square):
            print("Class is Square")
            if rect.area() != height * height:
                print("Area of rect is wrong! 2")
                return
        else:
            if rect.area() != width * height:
                print("Area of rect is wrong!")
                return
        print(f"The area of the rectangle is:{rect.area()}.")