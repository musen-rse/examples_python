import threading

from typing import List
from sensorchart.core.charts_abc import ChartFactory
from sensorchart.core.sensors import TemperatureSensor


class Application:
    def __init__(self, chart_factory: ChartFactory) -> None:
        self.sensor = TemperatureSensor()

        for choice in chart_factory.get_chart_choices():
            chart = chart_factory.create_chart(choice)
            self.sensor.add_chart(chart)

    def run(self) -> None:
        stop_event = threading.Event()
        while not stop_event.wait(1):
            self._clear_console()
            self.sensor.measure()

    def _clear_console(self):
        print("\033[2J", flush=True)
