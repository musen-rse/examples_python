from charts import ConsoleChartFactory
from core.app import Application
from measure_strategy import ContinuousMeasureStrategy, OneTimeMeasureStrategy, ManualMeasureStrategy
from sensors import HumiditySensor, TemperatureSensor

if __name__ == "__main__":
    sensors = [TemperatureSensor(), HumiditySensor()]
    app = Application(sensors=sensors,
                      chart_factory=ConsoleChartFactory(),
                      measure_strategy=ContinuousMeasureStrategy(sensors))

    app.run()
