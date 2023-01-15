class Heuristic2:
    @staticmethod
    def evaluate(table):
        redbest = 0
        blackbest = 0
        for row in range(7):
            for col in range(8):
                if table[row][col]=="R":
                    redbest = max(redbest,Heuristic2.getmax_profit(table,row,col,"R"))
                elif table[row][col]=="B":
                    blackbest = max(blackbest,Heuristic2.getmax_profit(table,row,col,"B"))
        return redbest-blackbest
    

    @staticmethod
    def getmax_profit(table,i,j,color):
        return max(
            min(4,Heuristic2.count_right_increasing_diagonal(table,i,j,color)+Heuristic2.count_left_increasing_diagonal(table,i,j,color)),
            min(4,Heuristic2.count_right_decreasing_diagonal(table,i,j,color)+Heuristic2.count_left_decreasing_diagonal(table,i,j,color)),
            min(4,Heuristic2.count_below(table,i,j,color)),
            min(4,Heuristic2.cout_right_horizontal(table,i,j,color)+Heuristic2.count_left_horizontal(table,i,j,color))
        )


    """
       *
      *
     *
    o
    """
    @staticmethod
    def count_right_increasing_diagonal(table,i,j,color):
        if i-1>=0 and j+1<8 and table[i-1][j+1]==color:
            if i-2>=0 and j+2<8 and table[i-2][j+2]==color:
                if i-3>=0 and j+3<8 and table[i-3][j+3]==color:
                    return 3
                else:
                    return 2
            else:
                return 1
        else:
            return 0


    """
    o
     *
      *
       *
    """
    @staticmethod
    def count_right_decreasing_diagonal(table,i,j,color):
        if i+1<7 and j+1<8 and table[i+1][j+1]==color:
            if i+2<7 and j+2<8 and table[i+2][j+2]==color:
                if i+3<7 and j+3<8 and table[i+3][j+3]==color:
                    return 3
                else:
                    return 2
            else:
                return 1
        else:
            return 0
    
    
    """
       o
      *
     *
    *
    """
    @staticmethod
    def count_left_increasing_diagonal(table,i,j,color):
        if i+1<7 and j-1>=0 and table[i+1][j-1]==color:
            if i+2<7 and j-2>=0 and table[i+2][j-2]==color:
                if i+3<7 and j-3>=0 and table[i+3][j-3]==color:
                    return 3
                else:
                    return 2
            else:
                return 1
        else:
            return 0
    

    """
    *
     *
      *
       o
    """
    @staticmethod
    def count_left_decreasing_diagonal(table,i,j,color):
        if i-1>=0 and j-1>=0 and table[i-1][j-1]==color:
            if i-2>=0 and j-2>=0 and table[i-2][j-2]==color:
                if i-3>=0 and j-3>=0 and table[i-3][j-3]==color:
                    return 3
                else:
                    return 2
            else:
                return 1
        else:
            return 0


    @staticmethod
    def cout_right_horizontal(table,i,j,color):
        if j+1<8 and table[i][j+1]==color:
            if j+2<8 and table[i][j+2]==color:
                if j+3<8 and table[i][j+3]==color:
                    return 3
                else:
                    return 2
            else:
                return 1
        else:
            return 0
    

    @staticmethod
    def count_left_horizontal(table,i,j,color):
        if j-1>=0 and table[i][j-1]==color:
            if j-2>=0 and table[i][j-2]==color:
                if j-3>=0 and table[i][j-3]==color:
                    return 3
                else:
                    return 2
            else:
                return 1
        else:
            return 0
    

    @staticmethod
    def count_below(table,i,j,color):
        if i+1<7 and table[i+1][j]==color:
            if i+2<7 and table[i+2][j]==color:
                if i+3<7 and table[i+3][j]==color:
                    return 3
                else:
                    return 2
            else:
                return 1
        else:
            return 0