import tkinter
from tkinter import *
from tkinter import messagebox
from functools import partial


# nest whole program in a function to call it again in order to reset the board.
def tictactoe():
    # ----------------------- FUNCTIONS ----------------------------------
    def o_turn(row, col, button):
        global i
        # checked_positions is for marking what box has been ticked in the back end.
        # the button arg is to config the button image to let the player know which buttons have been marked.
        if checked_positions[row][col] == "":
            button.config(image=whose_turn(i))
            checked_positions[row][col] = "X" if i % 2 == 0 else "O"
            i += 1
            check_for_winner()
        else:
            messagebox.showinfo(title="Error", message="This block already has been chosen.")

    def whose_turn(p):
        if p % 2 == 0:
            return o_img
        else:
            return x_img


    def check_for_winner():
        # Check for 'X' winning positions
        if (
            (checked_positions[0][0] == checked_positions[0][1] == checked_positions[0][2] == "X") or
            (checked_positions[1][0] == checked_positions[1][1] == checked_positions[1][2] == "X") or
            (checked_positions[2][0] == checked_positions[2][1] == checked_positions[2][2] == "X") or
            (checked_positions[0][0] == checked_positions[1][0] == checked_positions[2][0] == "X") or
            (checked_positions[0][1] == checked_positions[1][1] == checked_positions[2][1] == "X") or
            (checked_positions[0][2] == checked_positions[1][2] == checked_positions[2][2] == "X") or
            (checked_positions[0][0] == checked_positions[1][1] == checked_positions[2][2] == "X") or
            (checked_positions[0][2] == checked_positions[1][1] == checked_positions[2][0] == "X")
        ):
            return check_winner("O")
        # Check for 'O' winning positions
        elif (
            (checked_positions[0][0] == checked_positions[0][1] == checked_positions[0][2] == "O") or
            (checked_positions[1][0] == checked_positions[1][1] == checked_positions[1][2] == "O") or
            (checked_positions[2][0] == checked_positions[2][1] == checked_positions[2][2] == "O") or
            (checked_positions[0][0] == checked_positions[1][0] == checked_positions[2][0] == "O") or
            (checked_positions[0][1] == checked_positions[1][1] == checked_positions[2][1] == "O") or
            (checked_positions[0][2] == checked_positions[1][2] == checked_positions[2][2] == "O") or
            (checked_positions[0][0] == checked_positions[1][1] == checked_positions[2][2] == "O") or
            (checked_positions[0][2] == checked_positions[1][1] == checked_positions[2][0] == "O")
        ):
            return check_winner("X")

    # Display who won
    def check_winner(x):
        result = tkinter.messagebox.askretrycancel(title=f"PLAYER {x} WON!", message="Play another match?")
        # if play again, reset the game, otherwise quit the program.
        if result is True:
            window.destroy()
            tictactoe()
        else:
            return quit()

    # ------------------- FUNCTIONS END -------------------------

    # init tk window
    window = Tk()
    window.geometry("500x500")

    # Make all grids equal weight
    for r in range(3):
        window.rowconfigure(r, weight=1)
        window.columnconfigure(r, weight=1)

    # add X and O img variables.
    x_img = PhotoImage(file="X.png")
    o_img = PhotoImage(file="O.png")

    # init button list with 3 nested lists for row and column
    button_list = [[], [], []]

    # First column
    top_left_but = Button(command=lambda: o_turn(0, 0, top_left_but))
    top_left_but.grid(column=0, row=0, sticky='nesw')
    button_list[0].append(0)

    top_mid_but = Button(command=lambda: o_turn(0, 1, top_mid_but))
    top_mid_but.grid(column=1, row=0, sticky='nesw')
    button_list[0].append(1)

    top_right_but = Button(command=lambda: o_turn(0, 2, top_right_but))
    top_right_but.grid(column=2, row=0, sticky='nesw')
    button_list[0].append(2)

    # Second column
    mid_left_but = Button(command=lambda: o_turn(1, 0, mid_left_but))
    mid_left_but.grid(column=0, row=1, sticky='nesw')
    button_list[1].append(0)

    mid_but = Button(command=lambda: o_turn(1, 1, mid_but))
    mid_but.grid(column=1, row=1, sticky='nesw')
    button_list[1].append(1)

    mid_right_but = Button(command=lambda: o_turn(1, 2, mid_right_but))
    mid_right_but.grid(column=2, row=1, sticky='nesw')
    button_list[1].append(2)

    # Third column

    bot_left_but = Button(command=lambda: o_turn(2, 0, bot_left_but))
    bot_left_but.grid(column=0, row=2, sticky='nesw')
    button_list[2].append(0)

    bot_mid_but = Button (command=lambda: o_turn(2, 1, bot_mid_but))
    bot_mid_but.grid(column=1, row=2, sticky='nesw')
    button_list[2].append(1)

    bot_right_but = Button(command=lambda: o_turn(2, 2, bot_right_but))
    bot_right_but.grid(column=2, row=2, sticky='nesw')
    button_list[2].append(2)

    # Init empty list of strings to modify later
    checked_positions = [["", "", ""], ["", "", ""], ["", "", ""]]

    window.mainloop()


i = 2
tictactoe()
