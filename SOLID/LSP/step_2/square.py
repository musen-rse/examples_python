from core.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, width=1.0):
        self._height = width
        self._width = width

    def set_height(self, height: float):
        self._height = height
        self._width = height
    
    def set_width(self, width: float):
        self._width = width
        self._height = width
