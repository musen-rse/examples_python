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