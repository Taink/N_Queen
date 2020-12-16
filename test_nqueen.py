import pytest
import time
from nqueen_solving import *


def generate_board(size):
    return [[0 for x in range(size)] for y in range(size)]


class TestUtils:
    def get_wrong_board_full(self):
        board = [[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 0, 1],
                 [0, 0, 1, 0]]
        return board

    def get_board_soluce(self):
        board = [[0, 0, 1, 0],
                 [1, 0, 0, 0],
                 [0, 0, 0, 1],
                 [0, 1, 0, 0]]
        return board

    def get_good_board_not_full(self):
        board = [[0, 0, 0, 0],
                 [1, 0, 0, 0],
                 [0, 0, 0, 1],
                 [0, 1, 0, 0]]
        return board

    def test_print(self, capsys):
        board = generate_board(4)

        print_board(4, board)

        captured = capsys.readouterr()
        assert captured.out == " 0 0 0 0\n 0 0 0 0\n 0 0 0 0\n 0 0 0 0\n"

    def test_can_t_attack_empty(self):
        board = generate_board(4)
        assert can_t_attack(4, board)

    def test_can_t_attach_soluce(self):
        board = self.get_board_soluce()
        assert can_t_attack(4, board)

    def test_can_t_attack_full(self):
        board = self.get_good_board_not_full()
        assert can_t_attack(4, board)

    def test_can_attack(self):
        board = self.get_wrong_board_full()
        assert not can_t_attack(4, board)

    def test_is_soluce_empty(self):
        board = generate_board(4)
        is_a_soluce, nb_queen = is_soluce(4, board)
        assert not is_a_soluce
        assert nb_queen == 0

    def test_is_soluce_soluce(self):
        board = self.get_board_soluce()
        is_a_soluce, nb_queen = is_soluce(4, board)
        assert is_a_soluce
        assert nb_queen == 4

    def test_is_soluce_not_full(self):
        board = self.get_good_board_not_full()
        is_a_soluce, nb_queen = is_soluce(4, board)
        assert not is_a_soluce
        assert nb_queen == 3

    def test_is_not_soluce(self):
        board = self.get_wrong_board_full()
        is_a_soluce, nb_queen = is_soluce(4, board)
        assert not is_a_soluce
        assert nb_queen == 4


class TestSmall:
    def test_solve_three_x_three(self):
        board_size = 3
        board = generate_board(board_size)
        board, solved = solve_n_queen_small(board_size, board)
        assert not solved

    def test_solve_four_x_four(self):
        board_size = 4
        board = generate_board(board_size)
        board, solved = solve_n_queen_small(board_size, board)
        assert solved

        is_a_soluce, nb_queen = is_soluce(board_size, board)
        assert is_a_soluce
        assert nb_queen == board_size

    @pytest.mark.parametrize("board_size", [5, 6, 7, 8, 9, 10])
    def test_solve_N_x_N(self, board_size):
        board = generate_board(board_size)

        board, solved = solve_n_queen_small(board_size, board)
        assert solved

        is_a_soluce, nb_queen = is_soluce(board_size, board)
        assert is_a_soluce
        assert nb_queen == board_size


class TestMedium:
    @pytest.mark.parametrize("board_size", [15, 20])
    def test_solve_N_x_N_with_small_func(self, board_size):
        board = generate_board(board_size)

        t1 = time.time()
        board, solved = solve_n_queen_small(board_size, board)
        assert solved
        t2 = time.time()
        print(f"\nTest of size {board_size} took {t2-t1} seconds to be solved")

        is_a_soluce, nb_queen = is_soluce(board_size, board)
        assert is_a_soluce
        assert nb_queen == board_size


    @pytest.mark.parametrize("board_size", [20, 30, 50])
    def test_solve_N_x_N(self, board_size):
        board = generate_board(board_size)

        t1 = time.time()
        board, solved = solve_n_queen_big(board_size, board)
        assert solved
        t2 = time.time()
        print(f"\nTest of size {board_size} took {t2-t1} seconds to be solved")


class TestBig:
    @pytest.mark.parametrize("board_size", [50, 100])
    def test_solve_N_x_N(self, board_size):
        board = generate_board(board_size)

        t1 = time.time()
        board, solved = solve_n_queen_big(board_size, board)
        assert solved
        t2 = time.time()
        print(f"\nTest of size {board_size} took {t2-t1} seconds to be solved")


class TestAllSoluce:
    @pytest.mark.parametrize("board_size, nb_soluce", [(4,2), (5,10), (6,4), (7,40), (8,92)])
    def test_solve_N_x_N(self, board_size, nb_soluce):
        board = generate_board(board_size)
        boards = solve_n_queen_all_soluce(board_size, board)
        assert len(boards) == nb_soluce

        for soluce in boards:
            is_a_soluce, nb_queen = is_soluce(board_size, soluce)
            assert is_a_soluce
            assert nb_queen == board_size
