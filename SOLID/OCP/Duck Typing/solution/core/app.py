class Application:
    def __init__(self, shapes) -> None:
        self._shapes = shapes

    def run(self) -> None:
        for shape in self._shapes:
            shape.draw()
