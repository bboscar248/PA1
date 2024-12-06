"""
Author: Jose L Balcazar, ORCID 0000-0003-4248-4528 
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

Headers for functions in abstract board for simple tic-tac-toe-like games, 2021.
Intended for Grau en Intel-ligencia Artificial, Programacio i Algorismes 1.
I would prefer to do everything in terms of object-oriented programming though.
"""

# Import: 
# color GRAY; PLAYER_COLOR, NO_PLAYER
# board dimension BSIZ
from constants import PLAYER_COLOR, BSIZ, NO_PLAYER, GRAY

# Data structure for stones
from collections import namedtuple

Stone = namedtuple('Stone', ('x', 'y', 'color'))


def set_board_up(stones_per_player = 4):
    'Init stones and board, prepare functions to provide, act as their closure'

    board = [[NO_PLAYER for _ in range(BSIZ)] for _ in range(BSIZ)]
    stones_played = []
    current_player = 0
    selected_stone = None


    def stones():
        "return iterable with the stones already played"
        return stones_played

    def select_st(i, j):
        '''
        Select stone that current player intends to move. 
        Player must select a stone of his own.
        To be called only after all stones played.
        Report success by returning a boolean;
        '''
        nonlocal selected_stone
        if board[i][j] == PLAYER_COLOR[current_player]:
            selected_stone = (i, j)
            return True
        return False

    def end():
        for i in range(BSIZ):
            for j in range(BSIZ):
                if board[i][j] != NO_PLAYER:
                    # Check horizontal, vertical, and diagonal alignments
                    if (j <= BSIZ - 3 and 
                        board[i][j] == board[i][j+1] == board[i][j+2]):
                        return True
                    if (i <= BSIZ - 3 and 
                        board[i][j] == board[i+1][j] == board[i+2][j]):
                        return True
                    if (i <= BSIZ - 3 and j <= BSIZ - 3 and 
                        board[i][j] == board[i+1][j+1] == board[i+2][j+2]):
                        return True
                    if (i >= 2 and j <= BSIZ - 3 and 
                        board[i][j] == board[i-1][j+1] == board[i-2][j+2]):
                        return True
        return False

    def move_st(i, j):
        '''If valid square, move there selected stone and unselect it,
        then check for end of game, then select new stone for next
        player unless all stones already played;
        if square not valid, do nothing and keep selected stone.
        Return 3 values: bool indicating whether a stone is
        already selected, current player, and boolean indicating
        the end of the game.
        '''
        nonlocal selected_stone, current_player
        if selected_stone and board[i][j] == NO_PLAYER:
            si, sj = selected_stone
            board[si][sj] = NO_PLAYER
            board[i][j] = PLAYER_COLOR[current_player]
            stones_played.append(Stone(i, j, PLAYER_COLOR[current_player]))
            selected_stone = None
            if end():
                return False, current_player, True
            current_player = 1 - current_player
        return selected_stone is not None, current_player, False

    def draw_txt(end=False):
        'Use ASCII characters to draw the board.'
        for row in board:
            print(' '.join(row))
        if end:
            print("Game Over")

    # return these 4 functions to make them available to the main program
    return stones, select_st, move_st, draw_txt