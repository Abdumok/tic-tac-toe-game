import os
import time

p = [" "] * 9

# Create function to clear the screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")


def welcome():
    print("Welcome to tic toc game:")
    input("Press enter to start the game...")


# Create function to display board status
def display_board(game_board):
    
    board = print(f"""
|----------|---------|----------|
|          |         |          |
|    {p[6]}     |    {p[7]}    |    {p[8]}     |
|          |         |          |
|----------|---------|----------|
|          |         |          |
|    {p[3]}     |    {p[4]}    |    {p[5]}     |
|          |         |          |
|----------|---------|----------|
|          |         |          |
|    {p[0]}     |    {p[1]}    |    {p[2]}     |
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
        elif player2 == "X":
            player1 = player_choice
            player2 = "O"
            break
        else:
            print("Invalid input, Please choose X or O")
    return player1, player2


def position_of_play(positions, player_symbol, player_name):
    while True:
        choice = int(input(f"{player_name} chosse a number 1 - 9: "))
        if 0 < choice < 10 and positions[choice-1] == " ":
            positions[choice-1] = player_symbol
            break
        elif positions[choice-1] != " ":
            print("this position is already taken, Try again")
        elif 0 > choice > 10:
            print("Invalid input, Enter number between 1 - 9")

player1_name =  input("Player1, Enter a name: ")
player2_name =  input("Player2, Enter a name: ")

player = player_symbol() 
player_info= {"player1" : {"name" : player1_name, "symbol" : player[0]},
          "player2" : {"name" : player2_name, "symbol" : player[1]}
          }


    

while True:
    clear()
    display_board(p)
    position_of_play(p, player_info["player1"]["symbol"], player_info["player1"]["name"])
    clear()
    display_board(p)
    position_of_play(p, player_info["player2"]["symbol"], player_info["player2"]["name"])
   
    
    
