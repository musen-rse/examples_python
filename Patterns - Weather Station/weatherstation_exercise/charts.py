from datetime import datetime
from enum import Enum, auto
from typing import List, Tuple


class ChartColor(Enum):
    RED = auto()
    BLUE = auto()
    CYAN = auto()
    GREEN = auto()
    YELLOW = auto()
    WHITE = auto()


_DEFAULT_COLOR = '\033[0m'
_CONSOLE_COLORS = {
    ChartColor.WHITE: '\033[37m',
    ChartColor.BLUE: '\033[94m',
    ChartColor.CYAN: '\033[96m',
    ChartColor.GREEN: '\033[92m',
    ChartColor.YELLOW: '\033[93m',
    ChartColor.RED: '\033[91m',
}


class ConsoleTableChart:

    def __init__(self):
        self.values: List[Tuple[datetime, float]] = []
        self._column_headers = ["Time recorded", "Value"]
        self._color: ChartColor = ChartColor.WHITE

    def draw(self, value: float) -> None:
        self._print_headers()
        self._collect_values(value)
        self._print_values()

    @property
    def color(self) -> int:
        return self._history_length

    @color.setter
    def color(self, value: ChartColor) -> None:
        self._color = value

    def _print_values(self):
        for date, value in reversed(self.values):
            datestr = self._format_date(date, value)
            console_color = _CONSOLE_COLORS[self._color]
            print(f"{console_color}{datestr}", value, _DEFAULT_COLOR, sep="\t")

    def _collect_values(self, value):
        self.values = self.values[-4:]
        self.values.append((datetime.now(), value))

    def _print_headers(self):
        print("=========== TABLE CHART ===========")
        print(*self._column_headers, sep="\t")

    def _format_date(self, date: datetime, value: float) -> str:
        first_column_width = len(self._column_headers[0])
        return date.strftime("%H:%M:%S").ljust(first_column_width - len(str(value)))
