from core.ant import Ant


class WorkerAnt(Ant):
  
      def do_your_job(self) -> None:
          print("Worker ant is building the ant hill.")


class SoldierAnt(Ant):
  
      def do_your_job(self) -> None:
          print("Soldier ant is protecting the ant tribe.")


class NurseAnt(Ant):
  
      def do_your_job(self) -> None:
          print("Nurse ant is feeding the baby ants.")

