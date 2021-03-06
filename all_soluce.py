from copy import deepcopy

from utils import get_queens_from_board, Chessboard
from optimal import number_attacking


class Solver:
    def __init__(self, board_size: int, board: Chessboard):
        self.solutions: list[Chessboard] = []
        self.board_size = board_size
        self.board = board

    def find_solutions(self, row: int = 0) -> None:
        if row == self.board_size:
            self.solutions.append(deepcopy(self.board))

        else:
            queens = get_queens_from_board(self.board_size, self.board)
            for col in [col for col in range(self.board_size)
                        if number_attacking((row, col), queens) == 0]:
                self.board[row][col] = 1
                self.find_solutions(row + 1)
                self.board[row][col] = 0


def solve_n_queen_all_soluce(board_size: int, board: Chessboard) -> list[Chessboard]:
    s = Solver(board_size, board)
    s.find_solutions()
    return s.solutions
