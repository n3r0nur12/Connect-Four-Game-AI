from utils import Helper
INF = 1000000000
MININF = -1000000000

class Heuristic1:
    @staticmethod
    def evaluate(table):
        if Helper.is_winner(table,True):
            return INF
        if Helper.is_winner(table,False):
            return MININF
        return 0
