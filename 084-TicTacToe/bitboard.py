from config import BOARD_SIZE


# This is where the arbitrary board size utopianism breaks down for now, but it
# wouldn't be hard to generate these dynamically
WIN_STATES = [
    # rows
    0b111_000_000,
    0b000_111_000,
    0b000_000_111,
    # columns
    0b100_100_100,
    0b010_010_010,
    0b001_001_001,
    # diagonals
    0b100_010_001,
    0b001_010_100,
]


def player_state(board: list, player: str) -> int:

    bitboard = 0

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            bitboard |= int(cell==player) << (i * BOARD_SIZE + j)

    return bitboard


def player_won(board: list, player: str) -> bool:

    state = player_state(board, player)

    for win in WIN_STATES:
        if win & state == win:
            return True

    return False
