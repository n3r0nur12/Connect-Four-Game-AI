from utils import Helper
import time
import random


def get_AI_move(table,isRed):
    while True:
        ch = random.randint(1,8)
        if Helper.valid_column_number(table,ch):
            Helper.perform_move(table,ch,isRed)
            break


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
    
    print("\n\n\n\n\n\n")
    Helper.print_table(table)
    print("DRAW!!!",end="")
    ch = input(" Enter anything to start a new game.\n")
        


def human_ai():
    print("\n\n\n\n\n\n")
    color = 0
    while color == 0:
        print("1. Red")
        print("2. Black")
        ch = input("Enter index of your color.\n")
        match ch:
            case "1":
                color = 1
            case "2":
                color = 2
            case _:
                print("\n\n\n\n\n\n")
                "Invalid input. Please try again."
                continue
    
    table = Helper.initialize_table()
    for turn in range(56):
        print("\n\n\n\n\n\n")
        if turn%2==0:
            if color==1:
                get_human_move(table,True)
            else:
                get_AI_move(table,True)

            if Helper.is_winner(table,True):
                print("\n\n\n\n\n\n")
                Helper.print_table(table)
                print("RED WINS!!!",end="")
                ch = input(" Enter anything to start a new game.\n")
                return
        else:
            if color==2:
                get_human_move(table,False)
            else:
                get_AI_move(table,False)

            if Helper.is_winner(table,False):
                print("\n\n\n\n\n\n")
                Helper.print_table(table)
                print("BLACK WINS!!!",end="")
                ch = input(" Enter anything to start a new game.\n")
                return
    
    print("\n\n\n\n\n\n")
    Helper.print_table(table)
    print("DRAW!!!",end="")
    ch = input(" Enter anything to start a new game.\n")


def ai_ai():
    table = Helper.initialize_table()
    for turn in range(56):
        print("\n\n\n\n\n\n")
        if turn%2==0:
            get_AI_move(table,True)
            if Helper.is_winner(table,True):
                print("\n\n\n\n\n\n")
                Helper.print_table(table)
                print("RED WINS!!!",end="")
                ch = input(" Enter anything to start a new game.\n")
                return
            print("Red AI is played.")
        else:
            get_AI_move(table,False)
            if Helper.is_winner(table,False):
                print("\n\n\n\n\n\n")
                Helper.print_table(table)
                print("BLACK WINS!!!",end="")
                ch = input(" Enter anything to start a new game.\n")
                return
            print("Black AI is played.")
        Helper.print_table(table)
        time.sleep(1)
    
    print("\n\n\n\n\n\n")
    Helper.print_table(table)
    print("DRAW!!!",end="")
    ch = input(" Enter anything to start a new game.\n")



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
                print("\n\n\n\n\n\n")
                print("Invalid input. Please only enter the index of the game.")


start()
    

