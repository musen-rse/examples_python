import threading

from core.charts_abc import ChartFactory, ChartColor
from core.sensors import TemperatureSensor


class Application:
    def __init__(self, chart_factory: ChartFactory) -> None:
        self.sensor = TemperatureSensor()
        self.chart_factory = chart_factory

    def run(self) -> None:
        choice = self._ask_chart_choice(self.chart_factory)
        chart = self.chart_factory.create_chart(choice, self.sensor.name)
        chart.color = ChartColor.RED
        self.sensor.add_chart(chart)

        stop_event = threading.Event()
        while not stop_event.wait(1):
            self._clear_console()
            self.sensor.measure()

    def _ask_chart_choice(self, chart_factory: ChartFactory) -> str:
        print("Choose a chart type:")
        for index, choice in enumerate(chart_factory.get_chart_choices()):
            print(f"{index + 1}. {choice}")

        input_choice = input("Input the chart number: ")
        choice_index = int(input_choice) - 1
        return chart_factory.get_chart_choices()[choice_index]

    def _clear_console(self):
        print("\033[2J", flush=True)
