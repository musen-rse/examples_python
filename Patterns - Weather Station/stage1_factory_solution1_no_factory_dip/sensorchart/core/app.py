import threading

from typing import List
from sensorchart.charts import ConsoleTableChart, ConsoleBarChart
from sensorchart.core.charts_abc import Chart
from sensorchart.core.sensors import TemperatureSensor


class Application:
    def __init__(self) -> None:
        self.sensor = TemperatureSensor()

        self.sensor.add_chart(ConsoleTableChart())
        self.sensor.add_chart(ConsoleBarChart())

    def run(self) -> None:
        stop_event = threading.Event()
        while not stop_event.wait(1):
            self._clear_console()
            self.sensor.measure()

    def _clear_console(self):
        print("\033[2J", flush=True)
