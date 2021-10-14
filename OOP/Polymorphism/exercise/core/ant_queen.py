from typing import List
from core.ant import Ant


class AntQueen:

    def __init__(self, ants: List[Ant]) -> None:
        self._ants = ants

    def do_morning_routine(self) -> None:
      for ant in self._ants:
        ant.do_your_job()