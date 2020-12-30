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
            break
        if utils.is_attacking(coords, q):
            # print(f'{coords} is attacked by queen at {q}')
            result += 1
    return result


def init(N: int, board: list[list[int]]) -> list[list[int]]:
    """
    Creates an initial assignment using a greedy algorithm that places
    queens in the least conflicting indices. Ties are solved randomly.

    :param N: Size of the board
    :param board: Chess board (0 is void, 1 is queen)
    :returns: A populated chess board with N queens
    """
    for i, row in enumerate(board):
        queens = utils.get_queens_from_board(N, board)
        conflicts = [number_attacking((i, col), queens) for col in range(N)]

        candidates = [index for index, value in enumerate(conflicts) if value <= min(conflicts)]
        col_index = random.choice(candidates)

        board[i][col_index] = 1
    return board


def main(N: int, board: list[list[int]], max_iterations: int):
    it = 1

    while not utils.is_soluce(N, board)[0]:
        board = init(N, board)
        it += 1
        if it > max_iterations:
            board = None
            break
    return board


def solve_n_queen_big(N: int, board: list[list[int]]) -> tuple[list[list[int]], bool] :
    return board, utils.is_soluce(N, main(N, board, 100))[0]
