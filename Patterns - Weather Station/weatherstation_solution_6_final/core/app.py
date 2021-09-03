import threading

from sensorchart.core.charts_abc import ChartFactory
from sensorchart.core.logger import ObservingLogger
from sensorchart.core.sensors import HumiditySensor, TemperatureSensor


class Application:
    def __init__(self, chart_factory: ChartFactory) -> None:
        self.temperature_sensor = TemperatureSensor()
        self.humidity_sensor = HumiditySensor()

        for choice in chart_factory.get_chart_choices():
            temperature_chart = chart_factory.create_chart(choice, "Temperature")
            self.temperature_sensor.register(temperature_chart)
            
            humidity_chart = chart_factory.create_chart(choice, "Humidity")
            self.humidity_sensor.register(humidity_chart)

    def run(self) -> None:
        with ObservingLogger("output.txt") as logger:
            self.temperature_sensor.register(logger)
            self.humidity_sensor.register(logger)
            
            stop_event = threading.Event()
            while not stop_event.wait(1):
                self._clear_console()
                self.temperature_sensor.measure()
                self.humidity_sensor.measure()

    def _clear_console(self):
        print("\033[2J", flush=True)
