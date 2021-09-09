1. Copy + Pase this below `TemperatureSensor` in sensors.py

```python
class HumiditySensor:

    def __init__(self):
        self._humidity = 40
        self._charts: List[Chart] = []

    def add_chart(self, chart: Chart):
        self._charts.append(chart)

    def remove_chart(self, chart: Chart):
        self._charts.remove(chart)

    def measure(self):
        change = random.randint(-2, 2)
        self.humidity = self._humidity + change

        for chart in self._charts:
            chart.draw(self.temperature)

    @property
    def humidity(self):
        return self._humidity

    @humidity.setter
    def humidity(self, humidity):
        self._humidity = humidity

    @property
    def physical_quantity(self) -> str:
        return "Humidity"
```