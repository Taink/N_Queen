from utils import print_board, can_t_attack, is_soluce

def solve_n_queen_small(board_size: int, board):
    return board, solve_n_queen_small_helper(board_size, board, 0)

def solve_n_queen_small_helper(board_size, board, line):
    if line >= board_size:
        return True
    
    for y in range(board_size):
        board[y][line] = 1
        if not can_t_attack(board_size, board):
            board[y][line] = 0
        else:
            if solve_n_queen_small_helper(board_size, board, line + 1) == True:
                return True
        board[y][line] = 0
    return False