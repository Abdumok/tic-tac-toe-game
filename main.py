import os
import random
import ascii


# Create function to clear the screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")


def welcome():
    print(ascii.logo)
    print("Welcome to tic toc game:")
    input("Press enter to start...\n")


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
def players_symbol():
    while True:
        player_choice = input("Plyer1 choose a your symbol: (X or O) ").upper()
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


def position_of_play(board, player_symbol, player_name):
    while True:
        choice = input(f"{player_name} choose a number 1 - 9: ")
        if choice.isdigit():
            choice_int= int(choice)
            if 0 < choice_int < 10 and board[choice_int-1] == "-":
                board[choice_int-1] = player_symbol
                break
            elif board[choice_int-1] != "-":
                print("this position is already taken, Try again")
            elif 0 > choice_int > 10:
                print("Invalid input, Enter number between 1 - 9")
        else:
            print("That is not a number please enter number between (1 - 9)")


# Create function to determine game result
def game_over(board, player):
    if ((board[0] == board[1] == board[2] == player["symbol"]) or
        (board[3] == board[4] == board[5] == player["symbol"]) or
        (board[6] == board[7] == board[8] == player["symbol"]) or
        (board[0] == board[3] == board[6] == player["symbol"]) or
        (board[1] == board[4] == board[7] == player["symbol"]) or
        (board[2] == board[5] == board[8] == player["symbol"]) or
        (board[0] == board[4] == board[8] == player["symbol"]) or
        (board[2] == board[4] == board[6] == player["symbol"])):
        
        clear()
        display_board(board)
        
        print(f"\n{"-" * (len(player["name"])+5)}")
        print(f"{player["name"]} Wins")
        print(f"{"-" * (len(player["name"])+5)}\n")
        return True
        
    elif not "-" in board:
        clear()
        display_board(board)
        print("it's a draw")
        return True

        
def game_start():
    
    welcome()    
    
    game_board = ["-"] * 9
    player1_name =  input("Player1: Enter a name: ")
    player2_name =  input("Player2: Enter a name: ")

    player_symbol= players_symbol() 

    player_info= {
                  "player1" : {"name": player1_name,
                             "symbol": player_symbol[0]},
                  
                  "player2" : {"name": player2_name,
                             "symbol": player_symbol[1]}
          }

    
    game_on = True
    
    random_num = random.randint(1,2)
    
    clear()
    print(f"{player_info[f"player{random_num}"]["name"]} start")
    input("Press enter to start the game when you are ready...")

    if random_num == 1:
        player1 = player_info["player1"]
        player2 = player_info["player2"]
    else:
        player1 = player_info["player2"]    
        player2 = player_info["player1"]
    
    while game_on:
        clear()
        display_board(game_board)
        position_of_play(game_board, player1["symbol"],player1["name"])
        if game_over(game_board, player1):
            game_on = False
            break
        else:
            pass
        
        clear()
        display_board(game_board)
        position_of_play(game_board, player2["symbol"], player2["name"])
        if game_over(game_board, player2):
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

    
    
