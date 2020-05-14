from typing import List

board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],

         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],

         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


def print_board(board):
    for r in board:
        s = ""
        for c in r:
            s += str(c) + " "
        print(s)
    print()


class Solution:
    def __init__(self):
        self.board = []
        self.size = 3
        self.empty_cells = []

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board = board
        self.size = board.__len__()
        self.empty_cells = [(row, col) for row in range(0, self.size) for col in range(0, self.size)
                            if board[row][col] == '.']
        self.solve_next(self.empty_cells.__len__())

    def solve_next(self, cell_idx):
        cell_idx -= 1
        if cell_idx < 0:
            return True
        cell = self.empty_cells[cell_idx]
        row = cell[0]
        col = cell[1]

        for s in self.possible_numbers_for_cell(row, col):
            self.board[row][col] = s
            if self.solve_next(cell_idx):
                return True
            self.board[row][col] = '.'

        return False

    def possible_numbers_for_cell(self, r, c) -> []:
        s = set()
        for i in range(1, self.size + 1):
            s.add(str(i))
        for i in range(0, self.size):
            if self.board[r][i] in s:
                s.remove(self.board[r][i])

        for i in range(0, self.size):
            if self.board[i][c] in s:
                s.remove(self.board[i][c])
        self.remove_same_in_square(r, c, s)
        return s

    def remove_same_in_square(self, row, col, possible_digits: set):
        sq_row = 0 if row < 3 else 3
        sq_col = 0 if col < 3 else 3

        if row > 5:
            sq_row = 6
        if col > 5:
            sq_col = 6

        for r in range(sq_row, sq_row + 3):
            for c in range(sq_col, sq_col + 3):
                if self.board[r][c] in possible_digits:
                    possible_digits.remove(self.board[r][c])


s = Solution()
print_board(board)
s.solveSudoku(board)
print_board(board)
