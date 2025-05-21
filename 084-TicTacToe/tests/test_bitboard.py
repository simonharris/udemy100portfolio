import unittest

from bitboard import player_state, player_won
from tictactoe import EMPTY as EM, game_board


P1 = 'X'
P2 = 'O'


class BitboardTestCase(unittest.TestCase):

    def test_player_state(self):

        self.assertEqual(player_state([], P1), 0)
        self.assertEqual(player_state([P1], P1), 1)

        board = game_board()
        board[0] = [P1, P2, P1]
        self.assertEqual(player_state(board, P1), 5)

        board = game_board()
        board[0] = [P1, P2, P1]
        board[1] = [P2, EM, P2]
        board[2] = [P1, EM, P1]
        self.assertEqual(player_state(board, P1), 325)
        self.assertEqual(player_state(board, P2), 42)


    def test_player_won(self):

        # new game
        board = game_board()
        self.assertFalse(player_won(board, P1))

        # row
        board = game_board()
        board[0] = [P1, P1, P1]
        self.assertTrue(player_won(board, P1))

        # column
        board = game_board()
        board[0] = [P1, P2, EM]
        board[1] = [EM, P2, P2]
        board[2] = [P1, P2, P1]
        self.assertTrue(player_won(board, P2))

        # diagonal
        board = game_board()
        board[0] = [P1, P2, EM]
        board[1] = [P2, P1, P2]
        board[2] = [P1, EM, P1]
        self.assertTrue(player_won(board, P1))

        # draw
        board = game_board()
        board[0] = [P1, P2, EM]
        board[1] = [P2, P1, P2]
        board[2] = [P1, EM, P2]
        self.assertFalse(player_won(board, P1))
        self.assertFalse(player_won(board, P2))
