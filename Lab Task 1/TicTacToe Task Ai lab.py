class TicTacToe:
    def __init__(self, size):
        self.size = size
        self.board = [" "] * (size * size)
        self.current_player = "X"

    def display_board(self):
        print("\n")
        for i in range(0, len(self.board), self.size):
            row = " | ".join(self.board[i:i + self.size])
            print(row)
            if i < len(self.board) - self.size:
                print("--+" * (self.size - 1) + "--")
        print("\n")

    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
            return True
        else:
            print("That spot is already taken!")
            return False

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        b = self.board
        s = self.size

        # Check rows
        for r in range(0, len(b), s):
            if b[r] != " " and all(b[r] == b[r + c] for c in range(s)):
                return True

        # Check columns
        for c in range(s):
            if b[c] != " " and all(b[c] == b[c + r * s] for r in range(s)):
                return True

        # Check main diagonal
        if b[0] != " " and all(b[0] == b[i * (s + 1)] for i in range(s)):
            return True

        # Check anti-diagonal
        if b[s - 1] != " " and all(b[s - 1] == b[(i + 1) * (s - 1)] for i in range(s)):
            return True

        return False

    def is_draw(self):
        return " " not in self.board

    def play(self):
        print("Welcome to Tic-Tac-Toe!")
        self.display_board()

        while True:
            try:
                position = int(input(f"Player {self.current_player}, enter your move (1-{len(self.board)}): ")) - 1
                if position < 0 or position >= len(self.board):
                    print(f"Invalid position! Choose between 1-{len(self.board)}.")
                    continue
            except ValueError:
                print("Please enter a valid number.")
                continue

            if self.make_move(position):
                self.display_board()

                if self.check_winner():
                    print(f"Player {self.current_player} wins!")
                    break
                elif self.is_draw():
                    print("It's a draw!")
                    break
                else:
                    self.switch_player()


# Ask user for board size
try:
    size = int(input("Enter board size (e.g., 3 for 3x3): "))
    if size < 3:
        print("Minimum size is 3! Using default 3x3.")
        size = 3
except ValueError:
    print("Invalid input! Using default 3x3.")
    size = 3

# Run the game
game = TicTacToe(size)
game.play()