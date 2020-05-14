from typing import List
import cProfile
import pstats

board3 = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
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
        self.size = 9
        self.empty_cells = None
        self.squares = None
        self.nums_in_row = None
        self.nums_in_col = None

    def nums_in_sqr(self, row, col):
        row_shifter = 0 if row < 3 else 3 if row < 6 else 6
        quadrant_idx = row_shifter + int((col + 1) * 0.3)
        return self.squares[quadrant_idx]

    def populate_number_structs(self):
        self.size = 9
        self.empty_cells = []
        self.squares = []
        self.nums_in_row = []
        self.nums_in_col = []
        for i in range(0, self.size):
            self.squares.append({'1', '2', '3', '4', '5', '6', '7', '8', '9'})
            self.nums_in_row.append({'1', '2', '3', '4', '5', '6', '7', '8', '9'})
            self.nums_in_col.append({'1', '2', '3', '4', '5', '6', '7', '8', '9'})

        for row in range(0, self.size):
            for col in range(0, self.size):
                if self.board[row][col] != '.':
                    self.nums_in_sqr(row, col).discard(self.board[row][col])
                    self.nums_in_col[col].discard(self.board[row][col])
                    self.nums_in_row[row].discard(self.board[row][col])
                else:
                    self.empty_cells.append((row, col))

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board = board
        self.populate_number_structs()
        self.solve_next(self.empty_cells.__len__())

    def solve_next(self, cell_idx):
        cell_idx -= 1
        if cell_idx < 0:
            return True
        cell = self.empty_cells[cell_idx]
        row = cell[0]
        col = cell[1]

        for s in self.nums_in_sqr(row, col).intersection(self.nums_in_col[col], self.nums_in_row[row]):
            self.add_number_on_board(row, col, s)
            if self.solve_next(cell_idx):
                return True
            # Backtracking starts here
            self.del_number_on_board(row, col, s)

        return False

    def add_number_on_board(self, row, col, num):
        self.board[row][col] = num
        self.nums_in_sqr(row, col).discard(num)
        self.nums_in_row[row].discard(num)
        self.nums_in_col[col].discard(num)

    def del_number_on_board(self, row, col, num):
        self.board[row][col] = '.'
        self.nums_in_sqr(row, col).add(num)
        self.nums_in_row[row].add(num)
        self.nums_in_col[col].add(num)


s = Solution()
# print_board(board)
# s.solveSudoku(board3)
# print_board(board3)

profile = cProfile.Profile()
profile.runcall(s.solveSudoku, board3)
ps = pstats.Stats(profile)
ps.print_stats()
