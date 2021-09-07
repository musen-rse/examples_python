from charts import ConsoleChartFactory
from core.app import Application
from core.sensors import HumiditySensor, TemperatureSensor
from measure_strategy import ContinuousMeasureStrategy, OneTimeMeasureStrategy, ManualMeasureStrategy

if __name__ == "__main__":
    app = Application(sensors=[TemperatureSensor(), HumiditySensor()],
                      chart_factory=ConsoleChartFactory(),
                      measure_strategy=ContinuousMeasureStrategy())
    app.run()
