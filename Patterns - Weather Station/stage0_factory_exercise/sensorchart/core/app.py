import threading

from sensorchart.charts import ConsoleTableChart
from sensorchart.core.sensors import TemperatureSensor


class Application:
    def __init__(self) -> None:
        self.sensor = TemperatureSensor()

        chart = ConsoleTableChart()
        self.sensor.set_chart(chart)

    def run(self) -> None:
        stop_event = threading.Event()
        while not stop_event.wait(1):
            self._clear_console()
            self.sensor.measure()

    def _clear_console(self):
        print("\033[2J", flush=True)
