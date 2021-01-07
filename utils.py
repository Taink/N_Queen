Coordinates = tuple[int, int]
Chessboard = list[list[int]]


def is_diagonal(coord_a: Coordinates, coord_b: Coordinates) -> bool:
    x1, y1 = coord_a
    x2, y2 = coord_b
    return abs(x1 - x2) == abs(y1 - y2)


def is_attacking(coord_a: Coordinates, coord_b: Coordinates) -> bool:
    x1, y1 = coord_a
    x2, y2 = coord_b
    return (x1 == x2) or (y1 == y2) or is_diagonal(coord_a, coord_b)


def has_attacking(queen_locations: list[Coordinates]) -> bool:
    for i, q in enumerate(queen_locations):
        for q2 in queen_locations[i + 1:]:
            if is_attacking(q, q2):
                return True
    return False


def get_queens_from_board(size: int, board: Chessboard) -> list[Coordinates]:
    result: list[tuple[int, int]] = []
    for x in range(size):
        for y in range(size):
            if board[x][y] == 1:
                result.append((x, y))
    return result


def print_board(size: int, board: Chessboard) -> None:
    for x in range(size):
        result = ""
        for y in range(size):
            result = result + " " + str(board[x][y])
        print(result)


def can_t_attack(size: int, board: Chessboard) -> bool:
    queens = get_queens_from_board(size, board)
    return not has_attacking(queens)


def is_soluce(size: int, board: Chessboard) -> tuple[bool, int]:
    if not board:
        return False, 0
    nb_queen = len(get_queens_from_board(size, board))
    return can_t_attack(size, board) and nb_queen == size, nb_queen
