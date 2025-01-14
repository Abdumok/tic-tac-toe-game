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

