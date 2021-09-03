import threading

from pynput.keyboard import Key, Listener

from core.measure_strategy_abc import MeasureStrategy


class OneTimeMeasureStrategy(MeasureStrategy):

    def measure(self):
        for sensor in self._sensors:
            sensor.measure()


class ContinuousMeasureStrategy(MeasureStrategy):

    def measure(self):
        stop_event = threading.Event()
        while not stop_event.wait(1):
            for sensor in self._sensors:
                sensor.measure()


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
            for sensor in self._sensors:
                sensor.measure()

        elif key.char == "q":
            self.listener.stop()
