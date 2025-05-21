import unittest

from tictactoe import BOARD_SIZE, EMPTY, board_full, game_board

class BoardTestCase(unittest.TestCase):

    def test_board_full(self):

        self.assertFalse(board_full([[EMPTY]]))
        self.assertTrue(board_full([['X']]))

        self.assertFalse(board_full(game_board()))

        board = [['X' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.assertTrue(board_full(board))
