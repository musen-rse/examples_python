from datetime import datetime
from typing import List, Tuple


class ConsoleTableChart:

    def __init__(self):
        self.values: List[Tuple[datetime, float]] = []
        self._column_headers = ["Time recorded", "Value"]

    def draw(self, value: float) -> None:
        self._print_headers()
        self._collect_values(value)
        self._print_values()

    def _print_values(self):
        for date, value in reversed(self.values):
            datestr = self._format_date(date, value)
            print(datestr, value, sep="\t")

    def _collect_values(self, value):
        self.values = self.values[-4:]
        self.values.append((datetime.now(), value))

    def _print_headers(self):
        print("=========== TABLE CHART ===========")
        print(*self._column_headers, sep="\t")

    def _format_date(self, date: datetime, value: float) -> str:
        first_column_width = len(self._column_headers[0])
        return date.strftime("%H:%M:%S").ljust(first_column_width - len(str(value)))
