from datetime import datetime

from matplotlib.axes import Axes

from core.sensors import TemperatureSensor


class LineChart:

    def __init__(self, axes: Axes, sensor: TemperatureSensor) -> None:
        sensor.set_chart(self)

        self.axes = axes
        self.temperature_line = self.initial_plot(sensor.temperature)
        self.configure_axes()

    def update(self, temperature: int) -> None:
        self.update_line(self.temperature_line, temperature)
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

        self.axes.set_ylim(min_temperature, max_temperature)

    def configure_axes(self):
        self.axes.legend(["Temperature"])
        self.axes.set_xlabel("Time")
        self.axes.set_ylabel("Temperature")
