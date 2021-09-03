from charts import ConsoleChartFactory
from core.app import Application
from measure_strategy import ContinuousMeasureStrategy, OneTimeMeasureStrategy, ManualMeasureStrategy

if __name__ == "__main__":
    app = Application(ConsoleChartFactory(), ManualMeasureStrategy())
    app.run()