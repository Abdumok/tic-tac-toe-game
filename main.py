import os
import time

# Create function to clear the screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def welcome():
    print("Welcome to tic toc game:")
    input("Press enter to start the game...")

