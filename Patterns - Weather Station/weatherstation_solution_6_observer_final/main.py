from charts import ConsoleChartFactory
from core.app import Application
from core.sensors import HumiditySensor, TemperatureSensor

if __name__ == "__main__":
    app = Application(
        sensors=[TemperatureSensor(), HumiditySensor()],
        chart_factory=ConsoleChartFactory())
    
    app.run()
