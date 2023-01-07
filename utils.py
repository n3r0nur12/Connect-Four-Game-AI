class Helper:
    @staticmethod
    def initialize_table():
        n = 7
        m = 8
        table = [[" "] * m for i in range(n)]
        return table

    @staticmethod
    def print_table(table):
        for i in range(8):
            print("-"+str(i+1),end="")
        print("-")

        for i in range(7):
            for j in range(8):
                print("|" + table[i][j],end="")
            print("|")
        
        for i in range(8):
            print("-"+str(i+1),end="")
        print("-")
    
    @staticmethod
    def valid_column_number(table,col):
        col = str(col)
        if col.isnumeric()==False:
            return False

        col = int(col)
        if col <= 0 or col>8:
            return False
        
        if table[0][col-1]!=" ":
            return False
        
        return True

    @staticmethod
    def perform_move(table,col,isRed):
        col = col - 1
        for i in (6,5,4,3,2,1,0):
            if table[i][col]==" ":
                table[i][col] = "R" if (isRed) else "B"
                break

    @staticmethod
    def is_winner(table,isRed):
        check = "R" if isRed else "B"
        for i in range(7):
            count = 0
            for j in range(8):
                if table[i][j]==check:
                    count = count+1
                    if count==4:
                        return True
                else:
                    count = 0
        
        for j in range(8):
            count = 0
            for i in range(7):
                if table[i][j]==check:
                    count = count+1
                    if count==4:
                        return True
                else:
                    count = 0
        
        return False

