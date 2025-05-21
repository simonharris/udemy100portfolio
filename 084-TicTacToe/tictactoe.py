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

from bitboard import player_won
from config import (
    BOARD_SIZE,
    EMPTY,
    PLAYERS
)


# setup  ----------------------------------------------------------------------


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
    return [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def print_board(board):
    print("\n")
    pprint(board, width=20)
    print("\n")


def next_player() -> str:
    return next(cycler)


def take_turn(player: str, board: list) -> list:

    print_board(board)
    entry = input(f"Square for player {player}: ")

    try:
        r, c = [int(ch) for ch in entry.split(' ')]
    except ValueError as ex:
        raise BadTurn(BadTurn.GE_SYNTAX) from ex

    try:
        if not board[r][c] == EMPTY:
            raise BadTurn(BadTurn.GE_OCCUPIED)
    except IndexError as ex:
        raise BadTurn(BadTurn.GE_BADSQUARE) from ex

    board[r][c] = player
    return board


def board_full(board: list) -> bool:
    return all(square != EMPTY for row in board for square in row)


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

        if player_won(board, player):
            print(f"\nTHE WIN GOES TO {player}!!")
            game_over = True

        elif board_full(board):
            print("\nIT'S A DRAW!!")
            game_over = True

    print("GAME OVER!!")
    print("Final board:")
    print_board(board)


# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()
