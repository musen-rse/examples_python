import threading
from typing import List

from pynput.keyboard import Key, Listener

from core.sensors_abc import Sensor
from core.measure_strategy_abc import MeasureStrategy


def _clear_console():
    print("\033[2J", flush=True)


def _measure_all_sensors(sensors: List[Sensor]):
    _clear_console()
    for sensor in sensors:
        sensor.measure()


class OneTimeMeasureStrategy(MeasureStrategy):

    def measure(self):
        _measure_all_sensors(self._sensors)


class ContinuousMeasureStrategy(MeasureStrategy):

    def measure(self):
        stop_event = threading.Event()
        while not stop_event.wait(1):
            _measure_all_sensors(self._sensors)


class ManualMeasureStrategy(MeasureStrategy):

    def __init__(self):
        super().__init__()
        self.listener: Listener = None

    def measure(self):
        with Listener(on_press=self.on_press) as listener:
            self.listener = listener
            listener.join()

    def on_press(self, key: Key):
        if key.char == "m":
            _measure_all_sensors(self._sensors)

        elif key.char == "q":
            self.listener.stop()
