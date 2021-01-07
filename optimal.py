import random

import utils
from utils import Chessboard, Coordinates


def number_attacking(coords: Coordinates, queens: list[Coordinates],
                     filter_queen: Coordinates = None) -> int:
    """
    Determines the number of attacking queens for specific coordinates,
    optionally excluding one queen

    :param coords: Coordinates for which you want the least
    :param queens:
    :param filter_queen: An optional queen for which conflicts are not calculated
    :return: The number of constraint violations
    """
    result = 0
    for q in queens:
        if filter_queen and q is filter_queen:
            continue
        if utils.is_attacking(coords, q):
            # print(f'{coords} is attacked by queen at {q}')
            result += 1
    # print(f'{coords} attacked {result} time(s)')
    return result


def most_constrained_col(board_size: int, board: Chessboard, row: int) -> int:
    """
    Determines which column is the most constrained in the specified row.
    Ties are solved randomly.

    :param board_size: Size of the board
    :param board: Chess board (0 is void, 1 is queen)
    :param row: The row within which the cololumn should be
    :returns: (One of) the most constrained column(s) for the specified row
    """
    queens = utils.get_queens_from_board(board_size, board)
    conflicts = [number_attacking((row, col), queens) for col in range(board_size)]
    candidates = [i for i, v in enumerate(conflicts) if v <= min(conflicts)]
    return random.choice(candidates)


def conflicted_queen(board_size: int, board: Chessboard) -> Coordinates:
    queens = utils.get_queens_from_board(board_size, board)
    # print(queens)
    attacked_queens = [queen for queen in queens if number_attacking(queen, queens, queen) > 0]
    # print(attacked_queens)
    # print(f'{len(attacked_queens)} queens attacked')

    return random.choice(attacked_queens)


def init(board_size: int, board: Chessboard) -> Chessboard:
    """
    Creates an initial assignment using a greedy algorithm that places
    queens in the least conflicting indices. Ties are solved randomly.

    :param board_size: Size of the board
    :param board: Chess board (0 is void, 1 is queen)
    :returns: A populated chess board with N queens
    """
    for i, row in enumerate(board):
        col_index = most_constrained_col(board_size, board, i)

        board[i][col_index] = 1
    return board


def repair(board_size: int, board: Chessboard, repaired_queen: Coordinates) -> Chessboard:
    board[repaired_queen[0]][repaired_queen[1]] = 0
    row = repaired_queen[0]

    col = most_constrained_col(board_size, board, row)
    board[row][col] = 1

    # print(f'repaired queen at {repaired_queen} to go at {(row, col)}')

    return board


def main(board_size: int, board: Chessboard, max_iterations: int = 0) -> Chessboard:
    it = 1

    board = init(board_size, board)
    while not utils.is_soluce(board_size, board)[0]:
        next_queen = conflicted_queen(board_size, board)
        board = repair(board_size, board, next_queen)
        it += 1
        # utils.print_board(N, board)
        # print(f'it #{it}')
        if 0 < max_iterations < it:
            board = None
            break
    return board


def solve_n_queen_big(board_size: int, board: Chessboard) -> tuple[Chessboard, bool]:
    solution = None
    retries = 10
    while solution is None:
        if retries < 1:
            break
        solution = main(board_size, board, 100)
        retries -= 1
    return solution, utils.is_soluce(board_size, solution)[0]
