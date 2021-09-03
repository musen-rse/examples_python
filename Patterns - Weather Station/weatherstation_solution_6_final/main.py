from sensorchart.charts import ConsoleChartFactory
from sensorchart.core.app import Application

if __name__ == "__main__":
    app = Application(ConsoleChartFactory())
    app.run()