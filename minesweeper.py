import random

class MineSweeper():

    def __init__(self, sze):
        self.size = sze * 2 + 8
        self.board = [[0 for _ in range(self.size + 2)] for _ in range(self.size + 2)]
        self.mines = [[False for _ in range(self.size + 2)] for _ in range(self.size + 2)]
        self.checked = [[False for _ in range(self.size)] for _ in range(self.size)]
        self.flagged = [[False for _ in range(self.size)] for _ in range(self.size)]
        self.mines_count = 0
        self.first_click = True

    def create_mines(self, x, y):
        for i in range(1, self.size + 1):
            for j in range(1, self.size + 1):
                if not (x - 1 <= j <= x + 1 and y - 1 <= i <= y + 1):
                    self.mines[i][j] = random.random() < 0.2
                    if self.mines[i][j]:
                        self.mines_count += 1
        # CREATES NUMBERS OF MINES SURROUNDING SQUARES
        for i in range(1, self.size + 1):
            for j in range(1, self.size + 1):
                for k in range(i-1, i+2):
                    for l in range(j-1, j+2):
                        if self.mines[k][l]:
                            self.board[i][j] += 1
        # ADDS MINES TO BOARD
        for i in range(1, self.size + 1):
            for j in range(1, self.size + 1):
                if self.mines[i][j]:
                    self.board[i][j] = '*'
        self.board = self.board[1:self.size+1]
        for i in range(len(self.board)):
            self.board[i] = self.board[i][1:self.size+1]
        print(self.board)

    def check_square(self, x, y):
        if not self.first_click:
            self.checked[x][y] = True
            if self.board[x][y] == '*':
                return '*'
            if self.board[x][y] == 0:
                for i in range(x-1, x+2):
                    for j in range(y-1, y+2):
                        if i >= 0 and j >= 0 and i < self.size and j < self.size:
                            if self.checked[i][j] == False:
                                self.check_square(i, j)
            return self.board[x][y]
        else:
            self.create_mines(x, y)
            print(self.board)
            self.first_click = False
            return self.check_square(x, y)


    def flag_square(self, x, y):
        if self.flagged[x][y]:
            self.flagged[x][y] = False
            if self.board[x][y] == '*':
                self.checked[x][y] = False
        else:
            self.flagged[x][y] = True
            if self.board[x][y] == '*':
                self.checked[x][y] = True

    def did_win(self):
        for i in self.checked:
            for j in i:
                if not j:
                    return False
        return True
