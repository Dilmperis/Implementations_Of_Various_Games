import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        # Create a frame to hold the Tic Tac Toe board and center it
        self.frame = tk.Frame(root)
        self.frame.pack(expand=True, pady=20)  

        self.current_player = "X"
        self.board = [" "] * 9

        # Create buttons 
        self.buttons = [tk.Button(self.frame, text=" ", font=('Arial', 24), width=5, height=2,
                                  command=lambda i=i: self.make_move(i)) for i in range(9)]

        for i, button in enumerate(self.buttons):
            row = i // 3
            col = i % 3
            button.grid(row=row, column=col)

        # Game history variables
        self.x_wins = 0
        self.o_wins = 0
        self.draws = 0
        self.total_games = 0

        # Display game history
        self.history_label = tk.Label(root, text=self.get_history_text(), font=('Arial', 14))
        self.history_label.pack(pady=10)

        # Create a reset button below the frame
        self.reset_button = tk.Button(root, text="Reset Board", command=self.reset_board)
        self.reset_button.pack(pady=5)

        # Create a new game button to reset the entire game including the history
        self.new_game_button = tk.Button(root, text="New Game", command=self.new_game)
        self.new_game_button.pack(pady=5)

    def make_move(self, index):
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            if self.check_winner():
                self.update_winner(self.current_player)
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif " " not in self.board:
                self.draws += 1
                self.total_games += 1
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

            self.history_label.config(text=self.get_history_text())

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]             # diagonals
        ]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return True

        return False

    def update_winner(self, player):
        if player == "X":
            self.x_wins += 1
        elif player == "O":
            self.o_wins += 1
        self.total_games += 1

    def reset_board(self):
        self.board = [" "] * 9
        self.current_player = "X"
        for button in self.buttons:
            button.config(text=" ")

    def new_game(self):
        # Reset game history
        self.x_wins = 0
        self.o_wins = 0
        self.draws = 0
        self.total_games = 0
        self.reset_board()
        self.history_label.config(text=self.get_history_text())

    def get_history_text(self):
        return (f"Total Games: {self.total_games}\n\n"
                f"Winner Player 'X': {self.x_wins} \n"
                f"Winner Player 'O': {self.o_wins} \n"
                f"Draws: {self.draws} "
                )

if __name__ == "__main__":
    root = tk.Tk()

    # Set the minimum size for the window to ensure the board is visible
    root.minsize(300, 400)

    game = TicTacToe(root)
    root.mainloop()
