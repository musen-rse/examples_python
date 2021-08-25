from datetime import datetime

from typing import Any

from matplotlib.axes import Axes
from observer_chart_solution.observer import Observer
from observer_chart_solution.sensors import HumiditySensor, TemperatureSensor


class LineChart(Observer):
    def __init__(
        self,
        axes: Axes,
        temperature_sensor: TemperatureSensor,
        humidity_sensor: HumiditySensor,
    ) -> None:

        self.axes = axes
        self.temperature_line = self.initial_plot(temperature_sensor.temperature)
        self.humidity_line = self.initial_plot(humidity_sensor.humidity)
        self.configure_axes()

        self.temperature_sensor = temperature_sensor
        self.humidity_sensor = humidity_sensor

        self.temperature_sensor.register(self)
        self.humidity_sensor.register(self)

    def update(self, sender: Any, *args, **kwargs) -> None:
        if sender is self.temperature_sensor:
            self.update_line(self.temperature_line, self.temperature_sensor.temperature)

        if sender is self.humidity_sensor:
            self.update_line(self.humidity_line, self.humidity_sensor.humidity)

        self.set_axes_limits()

    def initial_plot(self, yvalue):
        (line,) = self.axes.plot([datetime.now().strftime("%X")], [yvalue])
        return line

    def update_line(self, line, new_yvalue):
        new_xdata = [*line.get_xdata()[-4:], datetime.now().strftime("%X")]
        new_ydata = [*line.get_ydata()[-4:], new_yvalue]

        line.set_xdata(new_xdata)
        line.set_ydata(new_ydata)

    def set_axes_limits(self):
        min_time = self.temperature_line.get_xdata()[0]
        max_time = self.temperature_line.get_xdata()[-1]
        self.axes.set_xlim(min_time, max_time)

        min_temperature = min(self.temperature_line.get_ydata())
        max_temperature = max(self.temperature_line.get_ydata())
        min_humidity = min(self.humidity_line.get_ydata())
        max_humidity = max(self.humidity_line.get_ydata())
        self.axes.set_ylim(
            min(min_temperature, min_humidity), max(max_temperature, max_humidity)
        )

    def configure_axes(self):
        self.axes.legend(["Temperature", "Humidity"])
        self.axes.set_xlabel("Time")
        self.axes.set_ylabel("Temperature | Humidity")


class BarChart(Observer):
    def __init__(
        self,
        axes: Axes,
        temperature_sensor: TemperatureSensor,
        humidity_sensor: HumiditySensor,
    ) -> None:

        self.axes = axes
        self.temperature_bar = self.axes.bar(0, 0)
        self.humidity_bar = self.axes.bar(1, 0)

        self.temperature_sensor = temperature_sensor
        self.humidity_sensor = humidity_sensor
        self.temperature_sensor.register(self)
        self.humidity_sensor.register(self)

    def update(self, sender: Any, *args, **kwargs) -> None:
        if sender is self.temperature_sensor:
            self.temperature_bar[0].set_height(self.temperature_sensor.temperature)

        if sender is self.humidity_sensor:
            self.humidity_bar[0].set_height(self.humidity_sensor.humidity)

        self.set_axes_limits()

    def set_axes_limits(self):
        max_temperature = self.temperature_bar[0].get_height()
        max_humidity = self.humidity_bar[0].get_height()
        self.axes.set_ylim(0, max(max_temperature, max_humidity))
