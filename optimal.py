import random

import utils


def number_attacking(coords: tuple[int, int], queens: list[tuple[int, int]],
                     filter_queen: tuple[int, int] = None) -> int:
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


def most_constrained_col(N: int, board: list[list[int]], row: int) -> int:
    """
    Determines which column is the most constrained in the specified row.
    Ties are solved randomly.

    :param N: Size of the board
    :param board: Chess board (0 is void, 1 is queen)
    :param row: The row within which the cololumn should be
    :returns: (One of) the most constrained column(s) for the specified row
    """
    queens = utils.get_queens_from_board(N, board)
    conflicts = [number_attacking((row, col), queens) for col in range(N)]
    candidates = [i for i, v in enumerate(conflicts) if v <= min(conflicts)]
    return random.choice(candidates)


def conflicted_queen(N: int, board: list[list[int]]) -> tuple[int, int]:
    queens = utils.get_queens_from_board(N, board)
    # print(queens)
    attacked_queens = [queen for queen in queens if number_attacking(queen, queens, queen) > 0]
    # print(attacked_queens)
    # print(f'{len(attacked_queens)} queens attacked')

    return random.choice(attacked_queens)


def init(N: int, board: list[list[int]]) -> list[list[int]]:
    """
    Creates an initial assignment using a greedy algorithm that places
    queens in the least conflicting indices. Ties are solved randomly.

    :param N: Size of the board
    :param board: Chess board (0 is void, 1 is queen)
    :returns: A populated chess board with N queens
    """
    for i, row in enumerate(board):
        col_index = most_constrained_col(N, board, i)

        board[i][col_index] = 1
    return board


def repair(N: int, board: list[list[int]], repaired_queen: tuple[int, int]) -> list[list[int]]:
    board[repaired_queen[0]][repaired_queen[1]] = 0
    row = repaired_queen[0]

    col = most_constrained_col(N, board, row)
    board[row][col] = 1

    # print(f'repaired queen at {repaired_queen} to go at {(row, col)}')

    return board


def main(N: int, board: list[list[int]], max_iterations: int = 0):
    it = 1

    board = init(N, board)
    while not utils.is_soluce(N, board)[0]:
        next_queen = conflicted_queen(N, board)
        board = repair(N, board, next_queen)
        it += 1
        # utils.print_board(N, board)
        # print(f'it #{it}')
        if 0 < max_iterations < it:
            board = None
            break
    return board


def solve_n_queen_big(N: int, board: list[list[int]]) -> tuple[list[list[int]], bool]:
    solution = None
    retries = 10
    while solution is None:
        if retries < 1:
            break
        solution = main(N, board, 100)
        retries -= 1
    return solution, utils.is_soluce(N, solution)[0]
