##Jose Lopez
##Tic Tac Toe
##09/10/2021
import random
from tkinter import *
from tkinter import ttk

#To use hexadecimal you need "#ffffff"(must have the hashtag and be a string)

##This class is just the entire game
class Game():
    ##This is only used to hold all of the global variables and run the main function
    def __init__(self):
        self.root = Tk()
        self.AI_wins = 0
        self.column_var = []
        self.diagonal_var = []
        self.pl1_wins = 0
        self.pl2_wins = 0
        self.ending_text = ""
        self.winner = [False, None]
        self.turn = 0
        self.size = IntVar()
        self.board_text = []
        self.color = 'white'
        self.gameboard_color = "black"
        self.gameboard_text_color = "white"
        self.text_color = 'black'
        self.Font = "lucida"
        self.All_Fonts = ["arial", "athelas", "ayutha", "baskerville", "batang", "courier", "lucida"]
        #8
        self.All_Colors = ["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta"]
        self.Game_Starter()

    ##Internal Functions made here
    #Finished
    def Done(self, test_font, test_background_color, test_gameboard_color):
        dark_colors = ["black", "blue"]
        self.Font = test_font
        self.color = test_background_color
        if test_background_color in dark_colors:
            self.text_color = "white"
        else:
            self.text_color = "black"
        self.gameboard_color = test_gameboard_color
        if test_gameboard_color in dark_colors:
            self.text_color = "white"
        else:
            self.text_color = "black"

        self.Game_Starter_Click()
    #Finished
    def Default(self):
        self.color = 'white'
        self.gameboard_color = "black"
        self.gameboard_text_color = "white"
        self.text_color = 'black'
        self.Font = "lucida"

        self.Settings_Click()
    #Finished
    def Clear_Screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    #Finished
    def Make_System_Board(self):
        self.board_text = []
        for r in range(self.size.get()):
            self.board_text.append([])
            for c in range(self.size.get()):
                self.board_text[r].append(None)
    #Finihsed
    def Check_Winner(self):
        #Checks for row winner
        for row in self.board_text:
            for number in range(1, len(row)):
                if (row[number - 1] == row[number]) & (row[number] != None):
                    self.winner[0] = True
                else:
                    self.winner[0] = False
                    break
                self.winner[1] = row[number]
            if self.winner[0] == True:
                return
        #Created a new list of the columns only
        self.column_var = []
        for r in range(self.size.get()):
            self.column_var.append([])
            for c in range(self.size.get()):
                self.column_var[r].append(self.board_text[c][r])
        #Checks the columns list for any winners
        for column in self.column_var:
            for number in range(1, len(column)):
                if (column[number - 1] == column[number]) & (column[number] != None):
                    self.winner[0] = True
                else:
                    self.winner[0] = False
                    break
                self.winner[1] = column[number - 1]
            if self.winner[0] == True:
                return
        #Creates a new list of the diagonals
        self.diagonal_var = []
        self.diagonal_var.append([])
        #Appends top left to bottom left diaganol to list
        for i in range(self.size.get()):
            self.diagonal_var[0].append(self.board_text[i][i])
        self.diagonal_var.append([])
        #Appends top right to bottom right diaganol to list
        for i in range(self.size.get()):
            self.diagonal_var[1].append(self.board_text[i][self.size.get() - (i + 1)])
        #Checks all diaganols for a winner
        for diagonal in self.diagonal_var:
            for number in range(1, len(diagonal)):
                if (diagonal[number - 1] == diagonal[number]) & (diagonal[number] != None):
                    self.winner[0] = True
                else:
                    self.winner[0] = False
                    break
                self.winner[1] = diagonal[number - 1]
            if self.winner[0] == True:
                return
        #Resets the winner back to none
        self.winner[1] = None
        if self.turn == 9:
            self.winner[0] = True
    #Finished
    def Multiplayer_Find_Winner(self):
        if self.winner[1] == "X":
            self.ending_text = "Congratulations Player 1 you have won!"
            self.pl1_wins += 1
        elif self.winner[1] == "O":
            self.ending_text = "Congratulations Player 2 you have won!"
            self.pl2_wins += 1
        elif self.turn == 9:
            self.ending_text = "No one wins. Super stinky game!"
        else:
            print("Error in Find_Winner")
            self.root.destroy()
    #Unfinished
    def Singleplayer_Find_Winner(self):
        if self.winner[1] == "X":
            self.ending_text = "Congratulations Player 1 you have won!"
            self.pl1_wins += 1
        elif self.winner[1] == "O":
            self.ending_text = "Too bad the AI has won! You lost!"
            self.AI_wins += 1
        elif self.turn == 9:
            self.ending_text = "No one wins. Super stinky game!"
        else:
            print("Error in Find_Winner")
            self.root.destroy()
    #Unfinihsed
    def AI_Move(self):
        while True:
            r = random.randint(0, self.size.get() - 1)
            c = random.randint(0, self.size.get() - 1)
            print(r, c)
            if self.board_text[r][c] == None:
                self.board_text[r][c] = "O"
                break
        self.Singleplayer()

    ##Press functions for the moves in the game
    #Finished
    def Press_Multiplayer(self, r, c):
        if self.board_text[r][c] == None:
            self.Make_Move(r, c)
        else:
            return
    #Unfinished
    def Press_Singleplayer(self, r, c):
        if self.board_text[r][c] == None:
            self.Make_Move(r, c)
        else:
            return
        self.Check_Winner()

        if self.winner[0] == True:
            self.Singleplayer_Winner_Screen()
        self.AI_Move()


    ##GUI functions made here
    #Unfinished
    def Settings_Screen(self):
        self.Clear_Screen()
        test_font = StringVar()
        test_background_color = StringVar()
        test_gameboard_color = StringVar()

        self.root.title("Settings")

        Label(self.root, text="Font", font=self.Font, bg=self.color, fg=self.text_color, width=15).grid(row=0, column=0)
        test_font.set(self.Font)
        OptionMenu(self.root, test_font, *self.All_Fonts).grid(row=0, column=1)
        Button(self.root, text="Test", bg=self.color, fg=self.text_color, width=15).grid(row=0, column=2)

        Label(self.root, text="Background\nColor", font=self.Font, bg=self.color,
              fg=self.text_color, width=15).grid(row=1, column=0)
        test_background_color.set(self.color)
        OptionMenu(self.root, test_background_color, *self.All_Colors).grid(row=1, column=1)
        Button(self.root, text="Test", bg=self.color, fg=self.text_color, width=15).grid(row=1, column=2)

        Label(self.root, text="Gameboard\nColor", font=self.Font, bg=self.color,
              fg=self.text_color, width=15).grid(row=2, column=0)
        test_gameboard_color.set(self.color)
        OptionMenu(self.root, test_gameboard_color, *self.All_Colors).grid(row=2, column=1)
        Button(self.root, text="Test", bg=self.color, fg=self.text_color, width=15).grid(row=2, column=2)

        Button(self.root, text="Done", font=self.Font, bg=self.color, fg=self.text_color,
               width=15, height=5, command=lambda: self.Done(test_font.get(),
                                                             test_background_color.get(),
                                                             test_gameboard_color.get())).grid(row=5, column=0)
        Button(self.root, text="Set Default", font=self.Font, bg=self.color, fg=self.text_color,
               width=15, height=5, command=self.Default).grid(row=5, column=1)
        Button(self.root, text="Back", font=self.Font, bg=self.color, fg=self.text_color,
               width=15, height=5, command=self.Game_Starter_Click).grid(row=5, column=2)
        self.root.mainloop()
    #Finished
    def Make_Game_Board_Multiplayer(self):
        Button(self.root, text="Forfeit", command=self.root.destroy, width=6, bg='red').grid(row=0, column=0)
        Button()
        for r in range(self.size.get()):
            for c in range(self.size.get()):
                Button(self.root, text=self.board_text[r][c], width=6, height=3,
                       bg=self.gameboard_color, fg=self.gameboard_text_color,
                       command=lambda row=r, column=c: self.Press_Multiplayer(row, column)).grid(row=r + 1, column=c)
    #Finished
    def Make_Game_Board_Singleplayer(self):
        Button(self.root, text="Forfeit", command=self.root.destroy, width=6, bg='red').grid(row=0, column=0)
        Button()
        for r in range(self.size.get()):
            for c in range(self.size.get()):
                Button(self.root, text=self.board_text[r][c], width=6, height=3, bg=self.gameboard_color,
                       command=lambda row=r, column=c: self.Press_Singleplayer(row, column)).grid(row=r + 1, column=c)
    #Finished
    def Make_Move(self, r, c):
        if (self.turn % 2) == 0:
            self.board_text[r][c] = "X"
        elif (self.turn % 2) != 0:
            self.board_text[r][c] = "O"
        self.turn += 1
        self.Multiplayer()
    #Finished
    def Multiplayer_Winner_Screen(self):
        self.Multiplayer_Find_Winner()
        self.Clear_Screen()
        print(self.ending_text)
        Label(self.root, text=("Player 1 wins: " + str(self.pl1_wins)), width=15, height=5, bg=self.color
              , fg=self.text_color).grid(row=0, column=0)
        Label(self.root, text=("Player 2 wins: " + str(self.pl2_wins)), width=15, height=5, bg=self.color
              , fg=self.text_color).grid(row=0, column=1)
        Label(self.root, text=self.ending_text, width=30, height=2, bg=self.color, fg=self.text_color).grid(row=1, column=0, columnspan=2)
        Button(self.root, text="Restart", command=self.Multiplayer_Restart, bg='red', fg="black", height=5, width=15).grid(row=2, column=0)
        Button(self.root, text="Home", command=self.Game_Starter_Click, bg='red', fg="black", height=5, width=15).grid(row=2, column=1)
        self.root.mainloop()
    #Unfinished
    def Singleplayer_Winner_Screen(self):
        self.Singleplayer_Find_Winner()
        self.Clear_Screen()
        print(self.ending_text)
        Label(self.root, text=("Player 1 wins: " + str(self.pl1_wins)), width=15, bg='black'
              , fg='white').grid(row=0, column=0)
        Label(self.root, text=("AI wins: " + str(self.AI_wins)), width=15, bg='black'
              , fg='white').grid(row=0, column=1)
        Label(self.root, text=self.ending_text, width=30, bg='black', fg='white').grid(row=1, column=0, columnspan=2)
        Button(self.root, text="Restart", command=self.Singleplayer_Restart, bg='yellow', height=5, width=15).grid(row=2, column=0)
        Button(self.root, text="Exit", command=self.Game_Starter_Click, bg='red', height=5, width=15).grid(row=2, column=1)
        self.root.mainloop()

    ##Game modes made here
    #Finsihed(Unless needed to be enumerated)
    def Multiplayer(self):
        self.Clear_Screen()

        self.root.title("Multiplayer")

        self.Make_Game_Board_Multiplayer()

        self.Check_Winner()

        if self.winner[0] == True:
            self.Multiplayer_Winner_Screen()

        self.root.mainloop()
    #Finsihed(Unless needed to be enumerated)
    def Singleplayer(self):
        self.Clear_Screen()

        self.root.title("Singleplayer")

        self.Make_Game_Board_Singleplayer()

        self.Check_Winner()

        if self.winner[0] == True:
            self.Singleplayer_Winner_Screen()

        self.root.mainloop()

    ##Click functions for the game modes
    #Finsihed
    def Singleplayer_Click(self):
        self.pl1_wins = 0
        self.AI_wins = 0
        if self.size.get() == 0 or (self.size.get() % 2) == 0:
            return
        self.Make_System_Board()
        self.Singleplayer()
    #Finsihed
    def Multiplayer_Click(self):
        self.pl1_wins = 0
        self.pl2_wins = 0
        if self.size.get() == 0 or (self.size.get() % 2) == 0:
            return
        self.Make_System_Board()
        self.Multiplayer()
    #Finished
    def Settings_Click(self):
        self.Clear_Screen()
        self.Settings_Screen()
    #Finished
    def Game_Starter_Click(self):
        self.Clear_Screen()
        self.Game_Starter()
    #Finished
    def Multiplayer_Restart(self):
        self.Clear_Screen()
        self.ending_text = ""
        self.winner = [False, None]
        self.turn = 0
        self.board_text = []
        self.Make_System_Board()
        self.Multiplayer()
    #Finished
    def Singleplayer_Restart(self):
        self.Clear_Screen()
        self.ending_text = ""
        self.winner = [False, None]
        self.turn = 0
        self.board_text = []
        self.Make_System_Board()
        self.Singleplayer()


    ##Beginning of the program where they choose size and game mode
    def Game_Starter(self):
        self.root.title("Start")
        self.root.configure(bg=self.color)
        Button(self.root, text="Singleplayer", bg="yellow", font=self.Font, width=20, height=10, command=self.Singleplayer_Click).grid(row=0, column=0)
        Button(self.root, text="Multiplayer", bg="yellow", font=self.Font, width=20, height=10, command=self.Multiplayer_Click).grid(row=0, column=1)
        Label(self.root, text="Enter the size of the board\n(1 - 9)(odd number)", bg=self.color, fg=self.text_color).grid(row=1, column=0)
        Entry(self.root, textvariable=self.size).grid(row=1, column=1)
        Button(self.root, text="Exit", font=self.Font, width=20, bg="red", height=5, command=self.root.destroy).grid(row=3, column=0)
        Button(self.root, text="Settings", font=self.Font, width=20, bg="red", height=5, command=self.Settings_Click).grid(row=3, column=1)
        self.root.mainloop()



if __name__ == '__main__':
    Game()
