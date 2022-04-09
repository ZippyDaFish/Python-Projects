from tkinter import *
from tkinter import ttk
from functools import partial
import random
from random import sample
import copy
tk = Tk()
tk.title("Sudoku - Andrew Riker")
tk.resizable(width=False,height=False)

# pattern for a baseline valid solution
def pattern(r,c,base,side): return (base*(r%base)+r//base+c)%side
# randomize rows, columns and numbers (of valid base pattern)
def shuffle(s): return sample(s,len(s)) 

# produce board using randomized baseline pattern
def generate_complete_board():
    # set params
    base = 3
    side = base*base
    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))
    # generate board
    board = [ [nums[pattern(r,c,base,side)] for c in cols] for r in rows ]
    return board
    
def gen_incomplete_board(b):
    e_board = copy.deepcopy(b)
    for line in e_board:
        for i in range(0,6):
            j = random.randint(0,8)
            line[j] = ""
    return e_board
    
def display_board(b):
    n = 0
    for line in b:
        # adding horizontal separators
        if n == 3:
            ttk.Separator(tk, orient=HORIZONTAL).grid(column=0, row=n, columnspan=12, sticky='nswe', pady=10)
            n += 1
        if n == 7:
            ttk.Separator(tk, orient=HORIZONTAL).grid(column=0, row=n, columnspan=12, sticky='nswe', pady=10)
            n += 1
        # looping through each line
        for i in range(0,9):
            if i <= 2:
                button = Button(tk, text=line[i], width=5,height=3, state="disabled")
                if line[i] == "":
                    button.config(state=NORMAL, bg='white')
                    button.config(command=partial(digit_window,button))
                button.grid(column=i,row=n, padx=5,pady=5)
                continue
            # adding first vertical separator
            if i == 3:
                ttk.Separator(tk, orient=VERTICAL).grid(column=i, row=0, rowspan=12, sticky='nswe', padx=10)
            if i >= 3 and i <= 5:
                button = Button(tk, text=line[i], width=5,height=3, state="disabled")
                if line[i] == "":
                    button.config(state=NORMAL, bg='white')
                    button.config(command=partial(digit_window,button))
                button.grid(column=i+1,row=n, padx=5,pady=5)
                continue
            # adding second vertical separator
            if i == 6:
                ttk.Separator(tk, orient=VERTICAL).grid(column=i+1, row=0, rowspan=12, sticky='nswe', padx=10)
            if i >= 6:
                button = Button(tk, text=line[i], width=5,height=3, state="disabled")
                if line[i] == "":
                    button.config(state=NORMAL, bg='white')
                    button.config(command=partial(digit_window,button))
                button.grid(column=i+2,row=n, padx=5,pady=5)
        n += 1

def digit_window(button_clicked):
    button_clicked.config(bg='light green')
    digit_win = Toplevel(tk)
    digit_win.title("Digit Selection")
    digit_win.grab_set()
    digit_win.resizable(width=False,height=False)
    x = tk.winfo_x()
    y = tk.winfo_y()
    digit_win.geometry("+%d+%d" %(x+200,y+200))
    b_digit = Button(digit_win,text="None",width=4,height=3, command=partial(edit_button,"",button_clicked,digit_win))
    b_digit.grid(column=0,row=0,padx=2,pady=2)
    for i in range(1,10):
        b_digit = Button(digit_win,text=i,width=3,height=3, command=partial(edit_button,i,button_clicked,digit_win))
        b_digit.grid(column=i,row=0,padx=2,pady=2)
    digit_win.protocol("WM_DELETE_WINDOW", partial(digit_win_closed, button_clicked, digit_win))
def digit_win_closed(b,win):
    b.config(bg='white')
    win.destroy()
def edit_button(num,b,win):
    b.config(text=num, bg='white')
    b_index = str(b).split('n')
    n = 1
    for line in incomp_board:
        for i in range(0,9):
            if b_index[1] != "":
                if n == int(b_index[1]):
                    line[i] = num
                    win.destroy()
                    compare_boards()
                    return
            else:
                line[0] = num
                win.destroy()
                compare_boards()
                return
            n += 1
    win.destroy()
    
def compare_boards():
    if incomp_board == default_board:
        # display victory window
        win_win = Toplevel(tk)
        win_win.title("Victory!")
        win_win.resizable(width=False,height=False)
        victory_label = Label(win_win, text="You Win!")
        victory_label.config(font=("Arial", 30), padx=40, pady=30, borderwidth=7, relief="solid")
        victory_label.pack()

default_board = []
default_board = generate_complete_board()
incomp_board = gen_incomplete_board(default_board)
display_board(incomp_board)

for line in default_board: print(line)

tk.mainloop()
