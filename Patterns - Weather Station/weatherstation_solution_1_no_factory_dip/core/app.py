import threading

from typing import List
from charts import ConsoleTableChart, ConsoleBarChart
from core.charts_abc import Chart, ChartColor
from core.sensors import TemperatureSensor


class Application:
    def __init__(self) -> None:
        self.sensor = TemperatureSensor()

        table_chart = ConsoleTableChart(self.sensor.name)
        table_chart.color = ChartColor.RED
        self.sensor.add_chart(table_chart)
        
        bar_chart = ConsoleBarChart(self.sensor.name)
        bar_chart.color = ChartColor.BLUE
        self.sensor.add_chart(bar_chart)

    def run(self) -> None:
        stop_event = threading.Event()
        while not stop_event.wait(1):
            self._clear_console()
            self.sensor.measure()

    def _clear_console(self):
        print("\033[2J", flush=True)
