from tkinter import *
from tkinter import messagebox
from datetime import date

save_data = []
# defining functions for saving
def read_file():
    with open('save_data.txt') as file:
        for line in file:
            temp = line.rstrip('\n')
            save_data.append(temp)
        file.close()

def save_to_file():
    with open('save_data.txt', 'w') as file:
        save_data = lb.get(0,END)
        for i in save_data:
            file.write(i + '\n')
        file.close()

def new_task():
    task = my_entry.get()
    temp = task.replace("$","")
    try:
        float(temp)
    except:
        messagebox.showwarning("Error", "Please enter an expense.")
        return
    temp = round(float(temp), 2)
    lb.insert(0, "$" + str(temp) + " || " + str(date.today()))
    my_entry.delete(0, "end")
    my_entry.insert(END, '$')
    save_to_file()

def delete_task():
    lb.delete(ANCHOR)
    save_to_file()

# setup for tk
root = Tk()
root.geometry('700x600+500+200')
root.title('Expense Tracker - Andrew Riker')
root.config(bg='#181818')
root.resizable(width=False, height=False)
frame = Frame(root)
frame.pack(pady=18)

# setup for listbox
lb = Listbox(
    frame,
    width=50,
    height=12,
    font=('Times', 18),
    bd=0,
    fg='#181818',
    highlightthickness=0,
    selectbackground='#c5cbe1',
    activestyle="none",
)
lb.pack(side=LEFT, fill=BOTH, pady=12, padx=12)

# configuring scrollbar
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)
lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

# reading save file
read_file()
for i in save_data:
    lb.insert(END, i)

# setup for entry field
my_entry = Entry(root, font=('times', 24))
my_entry.insert(END, '$')
my_entry.pack(pady=20)

# setup for buttons
button_frame = Frame(root)
button_frame.pack(pady=20)
# button for adding expenses
addTask_btn = Button(
    button_frame,
    text='Add Expense',
    font=('times 14'),
    bg='#008080',
    padx=20,
    pady=10,
    command=new_task
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)
# button for deleting selected expenses
delTask_btn = Button(
    button_frame,
    text='Delete Expense',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=delete_task
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

root.mainloop()
