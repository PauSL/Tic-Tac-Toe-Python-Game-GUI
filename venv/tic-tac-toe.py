import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")

current_player = "X"
buttons = []

for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(root, text=" ", font='Arial 20', width=5, height=2)
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)

board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def check_win():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == "X":
            messagebox.showinfo("Game Over", "Player X wins!")
            return True
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == "O":
            messagebox.showinfo("Game Over", "Player O wins!")
            return True
    return False

def check_tie():
    if all([spot in ["X", "O"] for spot in board]):
        messagebox.showinfo("Game Over", "It's a tie!")
        return True
    return False

def button_click(x, y):
    global current_player
    if buttons[x][y]['text'] == " ":
        buttons[x][y]['text'] = current_player
        board[x * 3 + y] = current_player

        if check_win():
            reset_game()
        elif check_tie():
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

def reset_game():
    global current_player
    for i in range(3):
        for j in range(3):
            buttons[i][j]['text'] = " "
    current_player = "X"

for i in range(3):
    for j in range(3):
        buttons[i][j]['command'] = lambda x=i, y=j: button_click(x, y)

root.mainloop()
