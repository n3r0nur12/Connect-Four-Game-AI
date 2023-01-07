from utils import Helper


def get_AI_move():
    pass


def get_human_move(table,isRed):
    while True:
        Helper.print_table(table)
        if isRed:
            print("Red will play.")
        else:
            print("Black will play.")
        col = input("Enter the column number you want to place.\n")

        if Helper.valid_column_number(table,col)==False:
            print("\n\n\n\n\n\n")
            print("Invalid move! Please try again.")
            continue
        col = int(col)

        Helper.perform_move(table,col,isRed)
        return
            
        


def human_human():
    table = Helper.initialize_table()
    winner = 0
    for turn in range(56):
        print("\n\n\n\n\n\n")
        if turn%2==0:
            get_human_move(table,True)
            if Helper.is_winner(table,True):
                print("\n\n\n\n\n\n")
                Helper.print_table(table)
                print("RED WINS!!!",end="")
                ch = input(" Enter anything to start a new game.\n")
                return
        else:
            get_human_move(table,False)
            if Helper.is_winner(table,False):
                print("\n\n\n\n\n\n")
                Helper.print_table(table)
                print("BLACK WINS!!!",end="")
                ch = input(" Enter anything to start a new game.\n")
                return
        


def human_ai():
    pass


def ai_ai():
    pass


def start():
    print("\n\n\n\n\n\n")
    while True:
        print("**********************")
        print("*                    *")
        print("*    CONNECT FOUR    *")
        print("*                    *")
        print("**********************")
        print("1. Human vs Human")
        print("2. Human vs AI")
        print("3. AI vs AI")
        ch = input("Enter the index you want to play.\n")

        match ch:
            case "1":
                human_human()
                print("\n\n\n\n\n\n")
            case "2":
                human_ai()
                print("\n\n\n\n\n\n")
            case "3":
                ai_ai()
                print("\n\n\n\n\n\n")
            case _:
                print("Invalid input. Please only enter the index of the game.")


start()
    

