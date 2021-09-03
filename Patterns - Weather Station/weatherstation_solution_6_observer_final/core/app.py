import threading

from core.charts_abc import ChartFactory
from core.logger import ObservingLogger
from core.sensors import HumiditySensor, TemperatureSensor, Sensor


class Application:
    def __init__(self, chart_factory: ChartFactory) -> None:
        self.temperature_sensor = TemperatureSensor()
        self.humidity_sensor = HumiditySensor()
        self.chart_factory = chart_factory

    def run(self) -> None:
        self._choose_chart_for_sensor(self.temperature_sensor, "Temperature")
        self._choose_chart_for_sensor(self.humidity_sensor, "Humidity")

        with ObservingLogger("output.txt") as logger:
            self.temperature_sensor.register(logger)
            self.humidity_sensor.register(logger)

            stop_event = threading.Event()
            while not stop_event.wait(1):
                self._clear_console()
                self.temperature_sensor.measure()
                self.humidity_sensor.measure()

    def _choose_chart_for_sensor(self, sensor: Sensor, sensor_name: str) -> None:
        choice = self._ask_chart_choice(self.chart_factory, sensor_name)
        chart = self.chart_factory.create_chart(choice, sensor_name)
        sensor.register(chart)

    def _ask_chart_choice(self, chart_factory: ChartFactory, sensor_name: str) -> str:
        print(f"Choose a chart type for {sensor_name}:")
        for index, choice in enumerate(chart_factory.get_chart_choices()):
            print(f"{index + 1}. {choice}")

        input_choice = input("Input the chart number: ")
        choice_index = int(input_choice) - 1
        return chart_factory.get_chart_choices()[choice_index]

    def _clear_console(self):
        print("\033[2J", flush=True)
