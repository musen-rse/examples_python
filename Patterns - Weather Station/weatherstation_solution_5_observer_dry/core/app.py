import threading
from typing import List

from core.charts_abc import ChartFactory
from core.sensors_abc import Sensor


class Application:

    def __init__(self, sensors: List[Sensor], chart_factory: ChartFactory) -> None:
        self.chart_factory = chart_factory
        self.sensors = sensors

    def run(self) -> None:
        self._choose_charts_for_all_sensors()
        stop_event = threading.Event()
        while not stop_event.wait(1):
            self._clear_console()
            self._measure_all_sensors()

    def _measure_all_sensors(self):
        for sensor in self.sensors:
            sensor.measure()

    def _choose_charts_for_all_sensors(self) -> None:
        for sensor in self.sensors:
            self._choose_chart_for_sensor(sensor)

    def _choose_chart_for_sensor(self, sensor: Sensor) -> None:
        choice = self._ask_chart_choice(self.chart_factory,
                                        sensor.physical_quantity)

        chart = self.chart_factory.create_chart(choice,
                                                sensor.physical_quantity)
        sensor.add_chart(chart)

    def _ask_chart_choice(self, chart_factory: ChartFactory, sensor_name: str) -> str:
        print(f"Choose a chart type for {sensor_name}:")
        for index, choice in enumerate(chart_factory.get_chart_choices()):
            print(f"{index + 1}. {choice}")

        input_choice = input("Input the chart number: ")
        choice_index = int(input_choice) - 1
        return chart_factory.get_chart_choices()[choice_index]

    def _clear_console(self):
        print("\033[2J", flush=True)
