import threading
from typing import List

from core.charts_abc import Chart, ChartColor, ChartFactory
from core.sensors_abc import Sensor


class Application:

    def __init__(self, sensors: List[Sensor], chart_factory: ChartFactory) -> None:
        self.chart_factory = chart_factory
        self.sensors = sensors

    def run(self) -> None:
        self._choose_charts_for_all_sensors()
        self._run_measure_loop()

    def _run_measure_loop(self):
        stop_event = threading.Event()
        while not stop_event.wait(1):
            self._clear_console()
            self._measure_all_sensors()

    def _measure_all_sensors(self):
        for sensor in self.sensors:
            sensor.measure()

    def _choose_charts_for_all_sensors(self) -> None:
        for index, sensor in enumerate(self.sensors):
            self._choose_chart_for_sensor(index, sensor)

    def _choose_chart_for_sensor(self, index: int, sensor: Sensor) -> None:
        choice = self._ask_chart_choice(self.chart_factory,
                                        sensor.name)

        chart = self._create_chart_with_color(choice, index, sensor)
        sensor.register(chart)

    def _create_chart_with_color(self, chart_choice: str, index: int, sensor: Sensor) -> Chart:
        color = list(ChartColor)[index]
        chart = self.chart_factory.create_chart(chart_choice,
                                                sensor.name)

        chart.color = color
        return chart

    def _ask_chart_choice(self, chart_factory: ChartFactory, sensor_name: str) -> str:
        print(f"Choose a chart type for {sensor_name}:")
        for index, choice in enumerate(chart_factory.get_chart_choices()):
            print(f"{index + 1}. {choice}")

        input_choice = input("Input the chart number: ")
        choice_index = int(input_choice) - 1
        return chart_factory.get_chart_choices()[choice_index]

    def _clear_console(self):
        print("\033[2J", flush=True)
