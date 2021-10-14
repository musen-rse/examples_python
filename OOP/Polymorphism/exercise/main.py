from ants_impl import WorkerAnt, SoldierAnt, NurseAnt
from core.ant_queen import AntQueen

if __name__ == '__main__':
    ants = [WorkerAnt(), SoldierAnt(), NurseAnt()]
    ant_queen = AntQueen(ants)
    ant_queen.do_morning_routine()