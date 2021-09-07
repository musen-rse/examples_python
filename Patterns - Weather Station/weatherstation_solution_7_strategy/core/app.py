import threading
from typing import List

from core.charts_abc import ChartFactory
from core.logger import ObservingLogger
from core.measure_strategy_abc import MeasureStrategy
from core.sensors_abc import Sensor


class Application:
    def __init__(self, sensors: List[Sensor], chart_factory: ChartFactory, measure_strategy: MeasureStrategy) -> None:
        self.sensors = sensors
        self.chart_factory = chart_factory
        self.measure_strategy = measure_strategy

        for sensor in sensors:
            self.measure_strategy.add_sensor(sensor)

    def run(self) -> None:
        with ObservingLogger("output.txt") as logger:
            for sensor in self.sensors:
                sensor.register(logger)
                self._choose_chart_for_sensor(sensor)

            self.measure_strategy.measure()

    def _choose_chart_for_sensor(self, sensor: Sensor) -> None:
        sensor_name = sensor.physical_quantity
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
