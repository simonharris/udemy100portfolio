"""
Requirements:
Build a text-based version of the Tic Tac Toe game.
"""
import itertools
from pprint import pprint

BOARD_SIZE = 3

PLAYERS = ['X', 'O']
cycler = itertools.cycle(PLAYERS)

def game_board() -> list:
    # TODO: consider eg Pandas

    board = [[' ' for _ in  range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    return board


def print_board(board):
    pprint(board, width=30)


def take_turn(player: str, board: list):
    r = 1
    c = 2

    board[r][c] = player
    return board



def main():
    board = game_board()
    print_board(board)

    player = next(cycler)
    board = take_turn(player, board)
    print_board(board)



if __name__ == '__main__':
    main()