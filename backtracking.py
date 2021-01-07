from utils import can_t_attack, Chessboard


def solve_n_queen_small(board_size: int, board: Chessboard) -> tuple[Chessboard, bool]:
    return board, solve_n_queen_small_helper(board_size, board, 0)


def solve_n_queen_small_helper(board_size: int, board: Chessboard, line: int) -> bool:
    """
    Look on a line to position a queen then recursive call

    :param board_size: Size of the board
    :param board: Chess board (0 is void, 1 is queen)
    :param line: current line
    :return: If the board is one of the solutions
    """
    if line >= board_size:
        return True

    for y in range(board_size):
        board[y][line] = 1
        if not can_t_attack(board_size, board):
            board[y][line] = 0
        else:
            if solve_n_queen_small_helper(board_size, board, line + 1):
                return True
        board[y][line] = 0
    return False
