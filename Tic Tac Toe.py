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
counter = 0
size = IntVar()
board_text = []
turn = 0

def press_Multiplayer(r, c, turn):
    if (turn % 2) == 0:
        board_text[r][c] = "X"
    elif (turn % 2) != 0:
        board_text[r][c] = "O"
    print(turn)
    turn += 1
    print(turn)
    Multiplayer()

def Make_System_Board(size):
    for r in range(size):
        board_text.append([])
        for c in range(size):
            board_text[r].append("")

def Make_Game_Board(size, turn):
    for r in range(size):
        for c in range(size):
            Button(root, text=board_text[r][c], width=10, height=5, command=lambda row=r, column=c: press_Multiplayer(row, column, turn)).grid(row=r, column=c)


def Singleplayer():
    Clear_Screen()

    Make_Game_Board(size.get(), turn)

    root.mainloop()

def Multiplayer():
    Clear_Screen()

    Make_Game_Board(size.get(), turn)

    root.mainloop()

def Singleplayer_Click():
    if size.get() <= 0:
        return
    Make_System_Board(size.get())
    Singleplayer()

def Multiplayer_Click():
    if size.get() <= 0:
        return
    Make_System_Board(size.get())
    Multiplayer()

def Game_Starter():
    root.title("Start")
    Button(root, text="Singleplayer", width=20, height=10, command=Singleplayer_Click).grid(row=0, column=0)
    Button(root, text="Multiplayer", width=20, height=10, command=Multiplayer_Click).grid(row=0, column=1)
    Label(root, text="Enter the size of the board(1 - 9)(odd number)").grid(row=1, column=0)
    Entry(root, textvariable=size).grid(row=1, column=1)
    Button(root, text="Exit", width=40, bg="red", height=5, command=root.destroy).grid(row=3, columnspan=2)
    root.mainloop()


if __name__ == '__main__':
    Game_Starter()
