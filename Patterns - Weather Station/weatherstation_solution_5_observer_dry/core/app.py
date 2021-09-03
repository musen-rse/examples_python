import threading

from sensorchart.core.charts_abc import ChartFactory
from sensorchart.core.sensors import HumiditySensor, TemperatureSensor


class Application:
    def __init__(self, chart_factory: ChartFactory) -> None:
        self.temperature_sensor = TemperatureSensor()
        self.humidity_sensor = HumiditySensor()

        for choice in chart_factory.get_chart_choices():
            temperature_chart = chart_factory.create_chart(choice, "Temperature")
            self.temperature_sensor.add_chart(temperature_chart)
            
            humidity_chart = chart_factory.create_chart(choice, "Humidity")
            self.humidity_sensor.add_chart(humidity_chart)

    def run(self) -> None:
        stop_event = threading.Event()
        while not stop_event.wait(1):
            self._clear_console()
            self.temperature_sensor.measure()
            self.humidity_sensor.measure()

    def _clear_console(self):
        print("\033[2J", flush=True)
