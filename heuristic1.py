from utils import Helper
INF = 1000000000
MININF = -1000000000
"""
The whole philosophy of Heuristic1:
Act when you are about to win or lose.
Otherwise, play any way you want.

So, we check if this move is win or lose.
That way red go for win, black go for reds lose.
"""
class Heuristic1:
    @staticmethod
    def evaluate(table):
        if Helper.is_winner(table,True):
            return INF
        if Helper.is_winner(table,False):
            return MININF
        return 0
