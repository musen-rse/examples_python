from typing import List, Protocol


###############################################################################
# non volatile core of our application                                        #
###############################################################################


class Ant(Protocol):

    def do_your_job(self) -> None:
        raise NotImplementedError


class AntQueen:

    def __init__(self, ants: List[Ant]) -> None:
        self._ants = ants

    def do_morning_routine(self) -> None:
      for ant in self._ants:
        ant.do_your_job()


###############################################################################
# volatile part of our application                                            #
###############################################################################


class WorkerAnt(Ant):
  
      def do_your_job(self) -> None:
          print("Worker ant is building the ant hill.")


class SoldierAnt(Ant):
  
      def do_your_job(self) -> None:
          print("Soldier ant is protecting the ant tribe.")


class NurseAnt(Ant):
  
      def do_your_job(self) -> None:
          print("Nurse ant is feeding the baby ants.")


class SkyDiverAnt(Ant):
  
      def do_your_job(self) -> None:
          print("Sky diver ant is diving in the sky.")


if __name__ == '__main__':
    ants = [WorkerAnt(), SoldierAnt(), NurseAnt(), SkyDiverAnt()]
    ant_queen = AntQueen(ants)
    ant_queen.do_morning_routine()