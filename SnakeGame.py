# Importing packages from tkinter
from tkinter import *
from tkinter import messagebox

# Variables for player and game state
Player1 = 'X'
stop_game = False

# Function to handle button clicks
def clicked(r, c):
    global Player1
    global stop_game

    if states[r][c] == 0 and not stop_game:
        b[r][c].configure(text=Player1, bg="lightblue" if Player1 == 'X' else "lightgreen")
        states[r][c] = Player1

        check_if_win()

        if Player1 == 'X':
            Player1 = 'O'
        else:
            Player1 = 'X'
        player_turn_label.config(text=f"Player {Player1}'s Turn")

# Function to check if a player has won
def check_if_win():
    global stop_game

    # Check rows and columns
    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] != 0:  # Row check
            stop_game = True
            highlight_winner(i, 0, i, 1, i, 2)
            messagebox.showinfo("Winner", states[i][0] + " Won!")
            disable_all_buttons()
            return
        if states[0][i] == states[1][i] == states[2][i] != 0:  # Column check
            stop_game = True
            highlight_winner(0, i, 1, i, 2, i)
            messagebox.showinfo("Winner", states[0][i] + " Won!")
            disable_all_buttons()
            return

    # Check diagonals
    if states[0][0] == states[1][1] == states[2][2] != 0:  # Main diagonal
        stop_game = True
        highlight_winner(0, 0, 1, 1, 2, 2)
        messagebox.showinfo("Winner", states[0][0] + " Won!")
        disable_all_buttons()
        return
    if states[0][2] == states[1][1] == states[2][0] != 0:  # Anti-diagonal
        stop_game = True
        highlight_winner(0, 2, 1, 1, 2, 0)
        messagebox.showinfo("Winner", states[0][2] + " Won!")
        disable_all_buttons()
        return

    # Check for tie
    if all(states[i][j] != 0 for i in range(3) for j in range(3)):
        stop_game = True
        messagebox.showinfo("Tie", "It's a tie!")
        disable_all_buttons()

# Function to highlight the winning buttons
def highlight_winner(r1, c1, r2, c2, r3, c3):
    b[r1][c1].config(bg="yellow")
    b[r2][c2].config(bg="yellow")
    b[r3][c3].config(bg="yellow")

# Function to disable all buttons after the game ends
def disable_all_buttons():
    for i in range(3):
        for j in range(3):
            b[i][j].configure(state=DISABLED)

# Function to reset the game
def reset_game():
    global Player1, stop_game, states
    Player1 = 'X'
    stop_game = False
    player_turn_label.config(text="Player X's Turn")
    states = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            b[i][j].config(text="", bg="SystemButtonFace", state=NORMAL)

# Create the main window
root = Tk()
root.title("Tic Tac Toe")
root.resizable(0, 0)

# Create a frame for the Tic-Tac-Toe grid
frame = Frame(root)
frame.pack(pady=20)

# Create a label to display which player's turn it is
player_turn_label = Label(root, text="Player X's Turn", font=("Helvetica", 16))
player_turn_label.pack()

# Create buttons and states for the game
b = [[None, None, None], [None, None, None], [None, None, None]]
states = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Place buttons in the grid
for i in range(3):
    for j in range(3):
        b[i][j] = Button(frame, height=4, width=8, font=("Helvetica", "20"), command=lambda r=i, c=j: clicked(r, c))
        b[i][j].grid(row=i, column=j)

# Add a reset button
reset_button = Button(root, text="Reset Game", font=("Helvetica", 14), command=reset_game)
reset_button.pack(pady=10)

# Start the main event loop
root.mainloop()
