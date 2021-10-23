from datetime import datetime
from typing import Any, List, Optional, Union
from core.charts_abc import Chart, ChartColor, ChartFactory
from PySide6 import QtWidgets, QtCore, QtGui, QtCharts
from typing import Callable
import sys


class InvokeMethod(QtCore.QObject):
    # https://stackoverflow.com/questions/68137719/easy-way-to-call-a-function-on-the-main-thread-in-qt-pyside2

    def __init__(self, method: Callable, parent: Optional[QtCore.QObject] = None):
        """
        Invokes a method on the main thread. Taking care of garbage collection "bugs".
        """
        super().__init__()

        main_thread = QtGui.QGuiApplication.instance().thread()
        self.moveToThread(main_thread)
        application: QtGui.QGuiApplication = QtGui.QGuiApplication.instance()
        self.setParent(application)
        self.method = method
        self.called.connect(self.execute)  # type: ignore
        self.called.emit()  # type: ignore

    called = QtCore.Signal()

    @QtCore.Slot()  # type: ignore
    def execute(self) -> None:
        self.method()
        # trigger garbage collector
        self.setParent(None)  # type: ignore


class WorkerThread(QtCore.QThread):

    def __init__(self, run_loop: Callable) -> None:
        super().__init__()
        self._run_loop = run_loop

    def run(self) -> None:
        self._run_loop()


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, title: str) -> None:
        super(TableModel, self).__init__()

        self._data = [("-", "-")]
        self._headers = ["Time recorded", title]

    def data(self, index: Union[QtCore.QModelIndex, QtCore.QPersistentModelIndex], role: int = None) -> Any:
        if role == QtCore.Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, parent: Union[QtCore.QModelIndex, QtCore.QPersistentModelIndex] = None) -> int:
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, parent: Union[QtCore.QModelIndex, QtCore.QPersistentModelIndex] = None) -> int:
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int = None) -> Optional[str]:
        if orientation != QtCore.Qt.Horizontal:
            return None

        if role != QtCore.Qt.DisplayRole:
            return None

        return self._headers[section]

    def append(self, time: str, value: float) -> None:
        self._data = [*self._data[-4:], (time, str(value))]
        self.dataChanged.emit(self.index(0, 0), self.index(self.rowCount(), self.columnCount()))
        self.layoutChanged.emit()


class QtTableChartWindow(QtWidgets.QMainWindow):
    def __init__(self, title: str) -> None:
        super().__init__()
        self.setGeometry(100, 100, 400, 500)
        self._table = QtWidgets.QTableView()
        self._table.horizontalHeader().setVisible(True)
        self._table.horizontalHeader().setStretchLastSection(True)
        self._model = TableModel(title)
        self._table.setModel(self.model)
        self.setCentralWidget(self._table)

    @property
    def model(self) -> TableModel:
        return self._model


class QtTableChart(Chart):

    def __init__(self, title: str) -> None:
        super().__init__()
        InvokeMethod(lambda: self._create_window(title))

    updated = QtCore.Signal(str, float)

    def _create_window(self, title: str) -> None:
        self.window = QtTableChartWindow(title)
        self.window.setWindowTitle(title)
        self.window.show()

    def update(self, sender: Any, value: float) -> None:
        InvokeMethod(lambda: self.window.model.append(datetime.now().strftime("%H:%M:%S"), value))

    @property
    def color(self) -> ChartColor:
        return self._color

    @color.setter
    def color(self, value: ChartColor) -> None:
        self._color = value
        # bgrd_colors = {
        #     ChartColor.RED: "background-color:red;",
        #     ChartColor.GREEN: "background-color:green;",
        #     ChartColor.BLUE: "background-color:blue;",
        #     ChartColor.WHITE: "background-color:white;",
        #     ChartColor.YELLOW: "background-color:yellow;",
        #     ChartColor.CYAN: "background-color:cyan;"
        # }

        bgrd_colors = {
            ChartColor.RED: "QTableView { color:red };",
            ChartColor.GREEN: "QTableView { color: green }",
            ChartColor.BLUE: "QTableView { color: blue }",
            ChartColor.WHITE: "QTableView { color: white }",
            ChartColor.YELLOW: "QTableView { color: yellow }",
            ChartColor.CYAN: "QTableView { color: cyan }"
        }

        InvokeMethod(lambda: self.window.setStyleSheet(bgrd_colors[value]))


class QtBarChartWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setGeometry(100, 100, 680, 500)
        self.show()
        self.create_default_bars()
        self._max_value = 0

    def create_default_bars(self) -> None:
        # The QBarSet class represents a set of bars in the bar chart.
        # It groups several bars into a bar set

        set0 = QtCharts.QBarSet("--")

        set0 << 0 << 0 << 0 << 0 << 20

        series = QtCharts.QBarSeries()
        series.append(set0)

        series.barSets()[0].setLabel("--")
        self._chart = QtCharts.QChart()
        self._chart.addSeries(series)
        self._chart.setTitle("")
        self._chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        categories = ["00:00:01", "00:00:02", "00:00:03", "00:00:04", "00:00:05"]
        axis = QtCharts.QBarCategoryAxis()
        axis.append(categories)
        self._chart.createDefaultAxes()
        self._chart.setAxisX(axis, series)

        self._chart.legend().setVisible(False)
        self._chart.legend().setAlignment(QtGui.Qt.AlignBottom)

        chartView = QtCharts.QChartView(self._chart)
        chartView.setRenderHint(QtGui.QPainter.Antialiasing)

        self.setCentralWidget(chartView)

    def append_data(self, time: str, value: float) -> None:
        set0: QtCharts.QBarSet = self._chart.series()[0].barSets()[0]
        set0.remove(0)
        set0.append(value)

        # self._chart.axisX().categories()[0].pop(0)
        axis = self._chart.axisX()
        axis.remove(axis.at(0))
        axis.append([time])

        if value > self._max_value:
            self._chart.axisY().setMax(value + 10)
            self._max_value = int(value)

    def set_bar_color(self, color: QtCore.Qt.GlobalColor) -> None:
        set0: QtCharts.QBarSet = self._chart.series()[0].barSets()[0]
        set0.setColor(QtGui.QColor(color))


class QtBarChart(Chart):
    def __init__(self, title: str) -> None:
        super().__init__()
        InvokeMethod(lambda: self._create_window(title))

    def _create_window(self, title: str) -> None:
        self.window = QtBarChartWindow()
        self.window.setWindowTitle(title)
        self.window.show()

    def update(self, sender: Any, value: float) -> None:
        InvokeMethod(lambda: self.window.append_data(datetime.now().strftime("%H:%M:%S"), value))

    @property
    def color(self) -> ChartColor:
        return self._color

    @color.setter
    def color(self, value: ChartColor) -> None:
        self._color = value
        bgrd_colors = {
            ChartColor.RED: QtCore.Qt.red,
            ChartColor.GREEN: QtCore.Qt.green,
            ChartColor.BLUE: QtCore.Qt.blue,
            ChartColor.WHITE: QtCore.Qt.white,
            ChartColor.YELLOW: QtCore.Qt.yellow,
            ChartColor.CYAN: QtCore.Qt.cyan
        }
        InvokeMethod(lambda: self.window.set_bar_color(bgrd_colors[value]))


class QtChartFactory(ChartFactory):

    def __init__(self) -> None:
        super().__init__()
        self._chart_choices = {
            "table": QtTableChart,
            "bar": QtBarChart,
        }
        self._app = QtWidgets.QApplication(sys.argv)

    def create_run_loop(self, run_loop: Callable) -> None:
        self._gui_thread = WorkerThread(run_loop)
        self._gui_thread.start()
        sys.exit(self._app.exec())

    def create_chart(self, chart_type: str, title: str) -> Chart:
        chart_class = self._chart_choices[chart_type]
        return chart_class(title)

    def get_chart_types(self) -> List[str]:
        return sorted(self._chart_choices.keys())
