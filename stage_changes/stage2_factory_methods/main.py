from charts import ConsoleChartFactory
from core.app import Application

if __name__ == "__main__":
    app = Application(ConsoleChartFactory())
    app.run()