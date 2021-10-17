import random

from core.sensors_abc import Sensor


class TemperatureSensor(Sensor):

    def __init__(self) -> None:
        super().__init__()
        self._temperature = 20

    def measure(self) -> None:
        change = random.randint(-5, 5)
        self.temperature = self._temperature + change

        self.notify_all(self.temperature)

    @property
    def temperature(self) -> int:
        return self._temperature

    @temperature.setter
    def temperature(self, temperature: int) -> None:
        self._temperature = temperature

    @property
    def name(self) -> str:
        return "Temperature"


class HumiditySensor(Sensor):

    def __init__(self) -> None:
        super().__init__()
        self._humidity = 40

    def measure(self) -> None:
        change = random.randint(-2, 2)
        self.humidity = self._humidity + change

        self.notify_all(self.humidity)

    @property
    def humidity(self) -> int:
        return self._humidity

    @humidity.setter
    def humidity(self, humidity: int) -> None:
        self._humidity = humidity

    @property
    def name(self) -> str:
        return "Humidity"


class BarometerSensor(Sensor):

    def __init__(self) -> None:
        super().__init__()
        self._pressure = 1013 # hPa, https://en.wikipedia.org/wiki/Atmospheric_pressure

    def measure(self) -> None:
        change = random.randint(-20, 20)
        self.pressure = self._pressure + change

        self.notify_all(self.pressure)

    @property
    def pressure(self) -> int:
        return self._pressure

    @pressure.setter
    def pressure(self, pressure: int) -> None:
        self._pressure = pressure

    @property
    def name(self) -> str:
        return "Atmospheric pressure"
