"""
Requirements:
-------------
Using what you have learnt about Python programming, you will build a
text-based version of the Tic Tac Toe game. The game should be playable in the
command line just like the Blackjack game we created on Day 11. It should be a
2-player game, where one person is "X" and the other plays "O".
"""
import itertools
from pprint import pprint


# config ----------------------------------------------------------------------


BOARD_SIZE = 3
PLAYERS = ['X', 'O']
EMPTY = ' '

cycler = itertools.cycle(PLAYERS)


# functions etc ---------------------------------------------------------------


class BadTurn(Exception):

    GE_SYNTAX = 1
    GE_BADSQUARE = 2
    GE_OCCUPIED = 4

    MESSAGES = {
        GE_SYNTAX: 'Bad syntax',
        GE_BADSQUARE: 'Square does not exist',
        GE_OCCUPIED: 'Square occupied',
    }

    def __init__(self, which: int):
        self.which = which # needed?
        super().__init__(self.MESSAGES[which])


def game_board() -> list:
    # TODO: consider eg Pandas

    board = [[EMPTY for _ in  range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    return board


def print_board(board):
    # TODO: prettier printout
    print("\n")
    pprint(board, width=30)
    print("\n")

def next_player():
    return next(cycler)


def take_turn(player: str, board: list):

    print_board(board)
    entry = input(f"Square for player {player}: ")

    try:
        r, c = [int(ch) for ch in entry.split(' ')]
    except ValueError:
        raise BadTurn(BadTurn.GE_SYNTAX)

    try:
        if not board[r][c] == EMPTY:
            raise BadTurn(BadTurn.GE_OCCUPIED)
    except IndexError:
        raise BadTurn(BadTurn.GE_BADSQUARE)

    board[r][c] = player
    return board


# main loop -------------------------------------------------------------------


def main():

    board = game_board()
    game_over = False

    print('Welcome to the game!')

    while not game_over:

        player = next_player()
        turn_ok = False

        while not turn_ok:

            try:
                board = take_turn(player, board)
            except BadTurn as ge:
                print(f"\nPROBLEM!! {ge}")
                print("Please try again...")
            else:
                turn_ok = True

        # TODO: win detection!
        # TODO: and in fact winner detection

    # TODO: print out some kind of congrats


# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()
