import os
import time


# Create function to clear the screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")


def welcome():
    print("Welcome to tic toc game:")
    input("Press enter to start the game...")


# Create function to display board status
def display_board(board):
    
    print(f"""
|----------|---------|----------|
|          |         |          |
|    {board[6]}     |    {board[7]}    |    {board[8]}     |
|          |         |          |
|----------|---------|----------|
|          |         |          |
|    {board[3]}     |    {board[4]}    |    {board[5]}     |
|          |         |          |
|----------|---------|----------|
|          |         |          |
|    {board[0]}     |    {board[1]}    |    {board[2]}     |
|          |         |          |
|----------|---------|----------|
""")
    


# Create function to set player symbol:
def player_symbol():
    while True:
        player_choice = input("choose a your symbol: (X or O) ").upper()
        if player_choice == "O":
            player1 = player_choice
            player2 = "X"
            break
        elif player_choice == "X":
            player1 = player_choice
            player2 = "O"
            break
        else:
            print("Invalid input, Please choose X or O")
    return player1, player2


def position_of_play(positions, player_symbol, player_name):
    while True:
        choice = input(f"{player_name} choose a number 1 - 9: ")
        if choice.isdigit():
            choice_int= int(choice)
            if 0 < choice_int < 10 and positions[choice_int-1] == "-":
                positions[choice_int-1] = player_symbol
                break
            elif positions[choice_int-1] != "-":
                print("this position is already taken, Try again")
            elif 0 > choice_int > 10:
                print("Invalid input, Enter number between 1 - 9")
        else:
            print("That is not a number please enter number between (1 - 9)")



def game_over(p, player):
    if ((p[0] == p[1] == p[2] == player["symbol"]) or
        (p[3] == p[4] == p[5] == player["symbol"]) or
        (p[6] == p[7] == p[8] == player["symbol"]) or
        (p[0] == p[3] == p[6] == player["symbol"]) or
        (p[1] == p[4] == p[7] == player["symbol"]) or
        (p[2] == p[5] == p[8] == player["symbol"]) or
        (p[0] == p[4] == p[8] == player["symbol"]) or
        (p[2] == p[4] == p[6] == player["symbol"])):
        
        print(f"{player["name"]} is win")
        return True
        
    elif not "-" in p:
        print("it's a draw")
        return True

        
     
def game_start():
    
    empty_board = ["-"] * 9
    player1_name =  input("Player1, Enter a name: ")
    player2_name =  input("Player2, Enter a name: ")

    player= player_symbol() 

    player_info= {"player1" : {"name" : player1_name, "symbol" : player[0]},
          "player2" : {"name" : player2_name, "symbol" : player[1]}
          }


    game_on = True

    while game_on:
    
        clear()
        display_board(empty_board)
        position_of_play(empty_board, player_info["player1"]["symbol"], player_info["player1"]["name"])
        if game_over(empty_board, player_info["player1"]):
            game_on = False
            break
        else:
            pass
        
        clear()
        display_board(empty_board)
        position_of_play(empty_board, player_info["player2"]["symbol"], player_info["player2"]["name"])
        if game_over(empty_board, player_info["player1"]):
            game_on = False
            break
        else:
            pass
    

    play_again = input("Do you want to play again? (Y/N) ").lower()
    if play_again == "y":
        game_start()
    else:
        pass
    
game_start()

    
    
