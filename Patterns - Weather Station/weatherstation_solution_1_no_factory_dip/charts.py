from datetime import datetime
from typing import List, Tuple

from sensorchart.core.charts_abc import Chart


class ConsoleTableChart(Chart):

    def __init__(self):
        self.values: List[Tuple[datetime, float]] = []
        self._column_headers = ["Time recorded", "Value"]

    def draw(self, value: float) -> None:
        self._print_headers()
        self._collect_values(value)
        for date, value in reversed(self.values):
            datestr = self._format_date(date, value)
            print(datestr, value, sep="\t")

    def _print_headers(self):
        print("=========== TABLE CHART ===========")
        print(*self._column_headers, sep="\t")

    def _collect_values(self, value):
        self.values = self.values[-4:]
        self.values.append((datetime.now(), value))

    def _format_date(self, date: datetime, value: float) -> str:
        first_column_width = len(self._column_headers[0])
        return date.strftime("%H:%M:%S").ljust(first_column_width - len(str(value)))


class ConsoleBarChart(Chart):
    def __init__(self):
        self.bar_heights: List[float] = []

    def draw(self, value: float) -> None:
        self._print_header()
        self._collect_values(value)

        print(self._create_chart_string(value))

    def _create_chart_string(self, value: float) -> str:
        chart = ""
        max_bar = max([*self.bar_heights, 0])
        min_bar = min([*self.bar_heights, 0]) - 1

        for current_height in range(max_bar, min_bar, -1):
            for bar_height in self.bar_heights:
                chart += self.get_bar_string(bar_height, current_height)
                
            chart += "\n"

        chart += self._create_value_line(value) 
        return chart

    def _create_value_line(self, value: float) -> str:
        num_bars = len(self.bar_heights)
        spaces = " " * (num_bars - 1)
        return spaces + str(value)

    def _collect_values(self, value: float) -> None:
        bar_height = int(value / 3)
        self.bar_heights.append(bar_height)
        self.bar_heights = self.bar_heights[-40:]

    def _print_header(self) -> None:
        print("=========== BAR CHART ===========")

    def get_bar_string(self, bar: float, height: float) -> str:
        if height == 0:
            return "-"

        if height > 0 and bar >= height:
            return "*"

        if height < 0 and bar <= height:
            return "*"
        
        return " "