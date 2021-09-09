from typing import List

from core.charts_abc import Chart, ChartColor, ChartFactory
from core.logger import ObservingLogger
from core.measure_strategy_abc import MeasureStrategy
from core.sensors_abc import Sensor


class Application:
    def __init__(self, sensors: List[Sensor], chart_factory: ChartFactory, measure_strategy: MeasureStrategy) -> None:
        self.sensors = sensors
        self.chart_factory = chart_factory
        self.measure_strategy = measure_strategy

    def run(self) -> None:
        with ObservingLogger("output.txt") as logger:
            self._register_logger_on_sensors(logger)
            self._choose_charts_for_all_sensors()

            self.measure_strategy.measure()

    def _register_logger_on_sensors(self, logger):
        for sensor in self.sensors:
            sensor.register(logger)

    def _choose_charts_for_all_sensors(self) -> None:
        for index, sensor in enumerate(self.sensors):
            self._choose_chart_for_sensor(index, sensor)

    def _choose_chart_for_sensor(self, index: int, sensor: Sensor) -> None:
        choice = self._ask_chart_choice(self.chart_factory,
                                        sensor.physical_quantity)

        chart = self._create_chart_with_color(choice, index, sensor)
        sensor.register(chart)

    def _create_chart_with_color(self, chart_choice: str, index: int, sensor: Sensor) -> Chart:
        color = list(ChartColor)[index]
        chart = self.chart_factory.create_chart(chart_choice,
                                                sensor.physical_quantity)

        chart.color = color
        return chart

    def _ask_chart_choice(self, chart_factory: ChartFactory, sensor_name: str) -> str:
        print(f"Choose a chart type for {sensor_name}:")
        for index, choice in enumerate(chart_factory.get_chart_choices()):
            print(f"{index + 1}. {choice}")

        input_choice = input("Input the chart number: ")
        choice_index = int(input_choice) - 1
        return chart_factory.get_chart_choices()[choice_index]
