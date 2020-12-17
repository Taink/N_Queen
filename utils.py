# import math


def is_diagonal(coord_a: tuple[int, int], coord_b: tuple[int, int]):
    x1, y1 = coord_a
    x2, y2 = coord_b
    return abs(x1 - x2) == abs(y1 - y2)


def is_attacking(coord_a: tuple[int, int], coord_b: tuple[int, int]):
    x1, y1 = coord_a
    x2, y2 = coord_b
    return (x1 == x2) or (y1 == y2) or is_diagonal(coord_a, coord_b)


def has_attacking(queen_locations: list[tuple[int, int]]):
    for i, q in enumerate(queen_locations):
        for q2 in queen_locations[i + 1:]:
            if is_attacking(q, q2):
                return True
    return False


def print_board(size, board):
    for i in range(size):
        result = ""
        for j in range(size):
            result = result + " " + str(board[i][j])
        print(result)


def can_t_attack(size, board):
    pass  # TODO


def is_soluce(size, board):
    nb_queen = len()
    return can_t_attack(size, board)
