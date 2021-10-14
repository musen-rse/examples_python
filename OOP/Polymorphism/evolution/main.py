from ants_impl import WorkerAnt, SoldierAnt, NurseAnt, SkyDiverAnt
from core.ant_queen import AntQueen


if __name__ == '__main__':
    ants = [WorkerAnt(), SoldierAnt(), NurseAnt(), SkyDiverAnt()]
    ant_queen = AntQueen(ants)
    ant_queen.do_morning_routine()