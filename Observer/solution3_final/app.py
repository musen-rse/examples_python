import threading

from matplotlib import pyplot as plt

from core.sensors import HumiditySensor, TemperatureSensor
from charts import BarChart, LineChart


class Application:
    def __init__(self) -> None:
        plt.ion()
        self.event = threading.Event()
        self.figure, (self.line_ax, self.bar_ax) = plt.subplots(ncols=2)
        self.figure.canvas.mpl_connect("close_event", lambda _: self.event.set())

        self.temperature_sensor = TemperatureSensor()
        self.humdity_sensor = HumiditySensor()
        self.line_chart: LineChart = LineChart(
            self.line_ax, self.temperature_sensor, self.humdity_sensor
        )

        self.bar_chart: BarChart = BarChart(
            self.bar_ax, self.temperature_sensor, self.humdity_sensor
        )

    def run(self) -> None:
        while not self.event.wait(1):
            self.humdity_sensor.measure()
            self.temperature_sensor.measure()

            self.figure.canvas.draw()
            self.figure.canvas.flush_events()

            plt.pause(0.1)
