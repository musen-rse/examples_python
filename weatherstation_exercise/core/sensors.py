import random

from charts import ConsoleTableChart


class TemperatureSensor:

    def __init__(self):
        super().__init__()
        self._temperature = 20
        self._chart: ConsoleTableChart = None

    def set_chart(self, chart: ConsoleTableChart) -> None:
        self._chart = chart

    def measure(self) -> None:
        change = random.randint(-5, 5)
        self.temperature = self._temperature + change

        self._chart.draw(self.temperature)

    @property
    def name(self) -> str:
        return "Temperature"
