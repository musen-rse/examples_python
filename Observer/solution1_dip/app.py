import threading

from matplotlib import pyplot as plt

from charts import BarChart, LineChart
from core.sensors import TemperatureSensor


class Application:
    def __init__(self) -> None:
        plt.ion()
        self.event = threading.Event()
        self.figure, (self.line_ax, self.bar_ax) = plt.subplots(ncols=2)
        self.figure.canvas.mpl_connect(
            "close_event", lambda _: self.event.set())

        self.temperature_sensor = TemperatureSensor()

        self.line_chart = LineChart(self.line_ax, self.temperature_sensor)
        self.bar_chart = BarChart(self.bar_ax, self.temperature_sensor)

    def run(self) -> None:
        while not self.event.wait(1):
            self.temperature_sensor.measure()

            self.figure.canvas.draw()
            self.figure.canvas.flush_events()

            plt.pause(0.1)
