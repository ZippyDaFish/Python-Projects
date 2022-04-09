from tkinter import *
from functools import partial

root = Tk()
root.title("TicTacToe - Andrew Riker")
root.resizable(width=False,height=False)

xTurn = True
buttons = []

def disp_winner(winner):
    for i in buttons:
        i.config(state='disabled')
    win = Toplevel(root)
    win.title("Victory!")
    win.grab_set()
    win.resizable(width=False,height=False)
    x = root.winfo_x()
    y = root.winfo_y()
    win.geometry("+%d+%d" %(x+200,y+200))
    victory_label = Label(win, text=winner + " Wins!")
    victory_label.config(font=("Arial", 30), padx=40, pady=30, borderwidth=7, relief="solid")
    victory_label.pack()
    replay_button = Button(win, text="Play Again", command=partial(reset_board, win))
    replay_button.pack()

def display_board():
    for i in range(0,3):
        for j in range(0,3):
            button = Button(root, font=20, width=10,height=5,bg='white')
            button.config(command=partial(on_click,button))
            button.grid(row=i,column=j,padx=5,pady=5)
            buttons.append(button)

def reset_board(win):
    global buttons
    global xTurn
    for button in buttons:
        button.config(text="", state='normal',bg='white')
    xTurn = True
    win.destroy()

def on_click(button):
    global xTurn
    if xTurn == True:
        button.config(text="X", state='disabled',bg='light gray')
        xTurn = False
    elif xTurn == False:
        button.config(text="O", state='disabled',bg='light gray')
        xTurn = True
    check_board()

def check_board():
    x1 = 0
    o1 = 0
    # check for win in rows
    for i in range(0,9):
        if i == 3 or i == 6:
            x1 = 0
            o1 = 0
        if buttons[i]['text'] == "":
            x1 = 0
            o1 = 0
        elif buttons[i]['text'] == 'X':
            x1 += 1
            o1 = 0
        elif buttons[i]['text'] == 'O':
            o1 += 1
            x1 = 0
        if x1 >= 3: disp_winner('X')
        elif o1 >= 3: disp_winner('O')
    # check for win in columns
    for n in range(0,3):
        x2 = 0
        o2 = 0
        for j in range(0,9,3):
            if buttons[j + n]['text'] == 'X':
                x2 += 1
                o2 = 0
            elif buttons[j + n]['text'] == 'O':
                o2 += 1
                x2 = 0
            if x2 >= 3: disp_winner('X')
            elif o2 >= 3: disp_winner('O')
    # check for win in diagonals
    if buttons[0]['text'] == 'X' and buttons[4]['text'] == 'X' and buttons[8]['text'] == 'X': disp_winner('X')
    elif buttons[0]['text'] == 'O' and buttons[4]['text'] == 'O' and buttons[8]['text'] == 'O': disp_winner('O')
    if buttons[2]['text'] == 'X' and buttons[4]['text'] == 'X' and buttons[6]['text'] == 'X': disp_winner('X')
    elif buttons[2]['text'] == 'O' and buttons[4]['text'] == 'O' and buttons[6]['text'] == 'O': disp_winner('O')        

display_board()
root.mainloop()
