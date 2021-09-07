from charts import ConsoleChartFactory
from core.app import Application
from measure_strategy import ContinuousMeasureStrategy, OneTimeMeasureStrategy, ManualMeasureStrategy
from sensors import HumiditySensor, TemperatureSensor

if __name__ == "__main__":
    app = Application(sensors=[TemperatureSensor(), HumiditySensor()],
                      chart_factory=ConsoleChartFactory(),
                      measure_strategy=ContinuousMeasureStrategy())

    app.run()
