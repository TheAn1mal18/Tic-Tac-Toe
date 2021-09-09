##Jose Lopez
##09/08/2021
##Tic Tac Toe
from tkinter import *
from tkinter import ttk
def Clear_Screen():
    for widget in root.winfo_children():
        widget.destroy()

root = Tk()
##VARIABLES
rows = IntVar()
columns = IntVar()

def Make_Game_Board(rows, columns):
    for r in range(rows):
        for c in range(columns):
            Button(root, text="", width=10, height=5).grid(row=r, column=c)

def Singleplayer():
    if rows.get() == 0 or columns.get() == 0:
        return
    Clear_Screen()
    Make_Game_Board(rows.get(), columns.get())
    root.mainloop()

def Multiplayer():
    if rows.get() == 0 or columns.get() == 0:
        return
    Clear_Screen()
    Make_Game_Board(rows.get(), columns.get())
    root.mainloop()

def Game_Starter():
    root.title("Start")
    Button(root, text="Singleplayer", width=20, height=10, command=Singleplayer).grid(row=0, column=0)
    Button(root, text="Multiplayer", width=20, height=10, command=Multiplayer).grid(row=0, column=1)
    Label(root, text="Rows on Board").grid(row=1, column=0)
    Entry(root, textvariable=rows).grid(row=1, column=1)
    Label(root, text="Columns on Board").grid(row=2, column=0)
    Entry(root, textvariable=columns).grid(row=2, column=1)
    Button(root, text="Exit", width=40, bg="red", height=5, command=root.destroy).grid(row=3, columnspan=2)

    root.mainloop()


if __name__ == '__main__':
    Game_Starter()
