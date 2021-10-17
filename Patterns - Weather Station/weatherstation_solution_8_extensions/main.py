from typing import List
from console_charts import ConsoleChartFactory
from qt_charts import QtChartFactory
from core.app import Application
from core.sensors_abc import Sensor
from logger import Logger
from measure_strategy import ContinuousMeasureStrategy, OneTimeMeasureStrategy, ManualMeasureStrategy
from sensors import HumiditySensor, TemperatureSensor, BarometerSensor


def register_loggers_on_sensors(sensors: Sensor) -> List[Logger]:
        return [register_logger_on_sensor(sensor) 
                for sensor in sensors]


def register_logger_on_sensor(sensor: Sensor) -> Logger:
    logger = Logger(f"{sensor.name}.txt")
    sensor.register(logger)

    return logger


def open_loggers(loggers: List[Logger]) -> None:
    for logger in loggers:
        logger.open()


def close_loggers(loggers: List[Logger]) -> None:
    for logger in loggers:
        logger.close()


if __name__ == "__main__":
    sensors = [TemperatureSensor(), HumiditySensor(), BarometerSensor()]
    loggers = register_loggers_on_sensors(sensors)

    open_loggers(loggers)

    chart_factory = QtChartFactory()
    app = Application(sensors=sensors,
                    #   chart_factory=ConsoleChartFactory(),
                      chart_factory=chart_factory,
                      measure_strategy=ContinuousMeasureStrategy(sensors))

    chart_factory.create_run_loop(app.run)

    close_loggers(loggers)
