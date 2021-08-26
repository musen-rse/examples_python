import random


class TemperatureSensor:

    def __init__(self) -> None:
        self._temperature = 20
        self._chart: 'LineChart' = None

    def set_chart(self, chart: 'LineChart') -> None:
        self._chart = chart

    def measure(self):
        change = random.randint(-1, 1)
        self.temperature = self._temperature + change

    @property
    def temperature(self) -> int:
        return self._temperature

    @temperature.setter
    def temperature(self, value: int) -> None:
        self._temperature = value
        self._chart.update(self._temperature)
