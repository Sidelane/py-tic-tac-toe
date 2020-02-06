class Board:
    def __init__(self):
        self.board = ["0", "0", "0", "0", "0", "0", "0", "0", "0"]

    def draw(self):
        print()
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("-----------")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("-----------")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]}")
        print()

    def set_val(self, player, val):
        self.board[int(val)] = player.char

    def check_val(self, val):
        return self.board[int(val)]

    def check_if_won(self, player):
        if "0" not in self.board:
            return "Tie"
        if self.board[0] == player.char and self.board[1] == player.char and self.board[2] == player.char:
            return player.char
        elif self.board[3] == player.char and self.board[4] == player.char and self.board[5] == player.char:
            return player.char
        elif self.board[6] == player.char and self.board[7] == player.char and self.board[8] == player.char:
            return player.char
        elif self.board[0] == player.char and self.board[4] == player.char and self.board[8] == player.char:
            return player.char
        elif self.board[2] == player.char and self.board[4] == player.char and self.board[6] == player.char:
            return player.char
        elif self.board[1] == player.char and self.board[4] == player.char and self.board[7] == player.char:
            return player.char
        elif self.board[0] == player.char and self.board[3] == player.char and self.board[6] == player.char:
            return player.char
        elif self.board[2] == player.char and self.board[5] == player.char and self.board[8] == player.char:
            return player.char

    def clean_board(self):
        self.board = ["0", "0", "0", "0", "0", "0", "0", "0", "0"]
        
