
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


# Global Variables
players = ['X', 'O']
character = 'X'
board = [[], [], []]


def button(frame):
    """Creates a button"""
    bttn = Button(frame, padx=1, width=3, text="", font=('arial', 40))
    return bttn


def change_character():
    """Changes the operand for the next player"""
    global character, players
    for char in players:
        if char != character:
            character = char
            break


def reset():
    """Resets the board"""
    global character, players
    for row in range(3):
        for column in range(3):
            board[row][column]["text"] = ""
            board[row][column]["state"] = NORMAL
    players = ["X", "O"]
    character = "0"


def game_status():
    """Checks for victory or draw"""
    for i in range(3):
        if (board[i][0]["text"] == board[i][1]["text"] == board[i][2]["text"] == character or
                board[0][i]["text"] == board[1][i]["text"] == board[2][i]["text"] == character):
            messagebox.showinfo("Congrats!", character + " has won")
            reset()
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] == character or
            board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] == character):
        messagebox.showinfo("Congrats!", character + " has won")
        reset()
    elif (board[0][0]["state"] == board[0][1]["state"] == board[0][2]["state"]
          == board[1][0]["state"] == board[1][1]["state"] == board[1][2]["state"]
          == board[2][0]["state"] == board[2][1]["state"] == board[2][2]["state"] == DISABLED):
        messagebox.showinfo("Draw", "Cats game")
        reset()


def click(row, column):
    """Action for when button is clicked"""
    board[row][column].config(text=character, state=DISABLED)
    game_status()
    change_character()


def game_board():
    """Sets up the buttons to make the board"""
    for rows in range(3):
        for columns in range(3):
            board[rows].append(button(window))
            board[rows][columns].config(
                command=lambda row=rows, col=columns: click(row, col))
            board[rows][columns].grid(row=rows, column=columns)


# Setting up the window
window = Tk()
window.title("Tic Tac Toe")
game_board()

# Run Tic Tac Toe Game
window.mainloop()
