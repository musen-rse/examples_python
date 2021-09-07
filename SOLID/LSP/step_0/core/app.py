from typing import List

class Rectangle:
    def __init__(self, height=1.0, width=1.0):
        self._height: float = height
        self._width: float = width

    def set_height(self, height: float):
        self._height = height
    
    def set_width(self, width: float):
        self._width = width

    def area(self) -> float:
        return self._height * self._width


class Application:
    def __init__(self, rectangles) -> None:
        self._rectangles: List[Rectangle] = rectangles

    def run(self) -> None:
        for rect in self._rectangles:
            self._set_size(rect, 3.0, 4.0)

    def _set_size(self, rect: Rectangle, width: float, height: float):
        rect.set_width(width)
        rect.set_height(height)
        if rect.area() != width * height:
            print("Area of rect is wrong!")
            return
        print(f"The area of the rectangle is:{rect.area()}.")