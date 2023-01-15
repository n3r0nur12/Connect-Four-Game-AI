class Heuristic3:
    @staticmethod
    def evaluate(table):
        balance = 0
        for col in range(8):
            if table[0][col]!=" ":
                continue

            row = 0
            while row+1<7 and table[row+1][col]==" ":
                row = row + 1
            #print("R:"+str(Heuristic3.getmax_profit(table,row,col,"R")))
            balance = balance + Heuristic3.getmax_profit(table,row,col,"R")
            #print("B:"+str(-1 * Heuristic3.getmax_profit(table,row,col,"B")))
            balance = balance - Heuristic3.getmax_profit(table,row,col,"B")
        return balance
    

    @staticmethod
    def getmax_profit(table,i,j,color):
        return 10**(max(
            min(4,Heuristic3.count_right_increasing_diagonal(table,i,j,color)+Heuristic3.count_left_increasing_diagonal(table,i,j,color)),
            min(4,Heuristic3.count_right_decreasing_diagonal(table,i,j,color)+Heuristic3.count_left_decreasing_diagonal(table,i,j,color)),
            min(4,Heuristic3.count_below(table,i,j,color)),
            min(4,Heuristic3.cout_right_horizontal(table,i,j,color)+Heuristic3.count_left_horizontal(table,i,j,color))
        )+1)


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
