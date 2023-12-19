import tkinter as tk
from tkinter import messagebox

def reset_game():
    global current_player
    current_player = 'X'
    for button_row in buttons:
        for button in button_row:
            button.config(text="")

def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != '':
            return buttons[i][0]['text']
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != '':
            return buttons[0][i]['text']
    
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        return buttons[0][0]['text']
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        return buttons[0][2]['text']
    
    return None

def place_symbol(row, column):
    global current_player
    if buttons[row][column]['text'] == "":
        buttons[row][column].config(text=current_player)
        winner = check_winner()
        if winner:
            messagebox.showinfo("Résultat", f"Le joueur {winner} a gagné !")
            reset_game()
        else:
            current_player = 'O' if current_player == 'X' else 'X'

root = tk.Tk()
root.title("TicTacToe")

buttons = []
current_player = 'X'

for i in range(3):
    button_row = []
    for j in range(3):
        button = tk.Button(root, font=("Arial", 50), width=5, height=3, command=lambda row=i, col=j: place_symbol(row, col))
        button.grid(row=i, column=j)
        button_row.append(button)
    buttons.append(button_row)

reset_button = tk.Button(root, text="Recommencer la partie", font=("Arial", 12), command=reset_game)
reset_button.grid(row=3, columnspan=3)

root.mainloop()

        

    
