# import math

def is_diagonal(coord_a: tuple[int, int], coord_b: tuple[int, int]) -> bool:
    x1, y1 = coord_a
    x2, y2 = coord_b
    return abs(x1 - x2) == abs(y1 - y2)


def is_attacking(coord_a: tuple[int, int], coord_b: tuple[int, int]) -> bool:
    x1, y1 = coord_a
    x2, y2 = coord_b
    return (x1 == x2) or (y1 == y2) or is_diagonal(coord_a, coord_b)


def has_attacking(queen_locations: list[tuple[int, int]]) -> bool:
    for i, q in enumerate(queen_locations):
        for q2 in queen_locations[i + 1:]:
            if is_attacking(q, q2):
                return True
    return False


def get_queens_from_board(size: int, board: list[list[int]]) -> list[tuple[int, int]]:
    result: list[tuple[int, int]] = []
    for x in range(size):
        for y in range(size):
            if board[x][y] == 1:
                result.append((x, y))
    return result


def print_board(size: int, board: list[list[int]]) -> None:
    for i in range(size):
        result = ""
        for j in range(size):
            result = result + " " + str(board[i][j])
        print(result)


def can_t_attack(size: int, board: list[list[int]]) -> bool:
    queens = get_queens_from_board(size, board)
    return not has_attacking(queens)


def is_soluce(size, board):
    nb_queen = len(get_queens_from_board(size, board))
    return can_t_attack(size, board) and nb_queen == size, nb_queen
