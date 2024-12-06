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


# Stone: Representa una piedra con coordenadas (x, y) y un color asociado
Stone = namedtuple('Stone', ('x', 'y', 'color'))

def set_board_up(stones_per_player = 4):
    'Init stones and board, prepare functions to provide, act as their closure'

    # init board and game data here

	#Inicializamos el tablero de juego con NO_PLAYER (casillas vacías)
    board = [[NO_PLAYER for _ in range(BSIZ)] for _ in range(BSIZ)]

    # 1 para Jugador 1, 2 para Jugador 2 (comienza el jugador 1)
    current_player = 1

 	# Lista para almacenar las piedras jugadas
    played_stones = []


	# Devolverá las piedras jugadas
    def stones():
        "return iterable with the stones already played"
        
        # Devolvemos las piedras jugadas
        return played_stones



	# Permite seleccionar una piedra del jugador actual
    def select_st(i, j):
        '''
        Select stone that current player intends to move.
        Player must select a stone of his own.
        To be called only after all stones played.
        Report success by returning a boolean;
        '''
        
        # Seleccionamos una piedra del jugador actual (debe ser de su propio color)
        return board[i][j] == PLAYER_COLOR[current_player] 


 	# Verifica si el juego terminó
    def end():
        'Test whether there are 3 aligned stones'
        
        for i in range(BSIZ): 
             
            # Verificamos las horizontales y las verticales
            if all(board[i][j] == PLAYER_COLOR[current_player] for j in range(BSIZ)) or \
                all(board[j][i] == PLAYER_COLOR[current_player] for j in range(BSIZ)):
                    return f"Jugador {current_player} ha ganado" 

            # Verificamos la diagonal principal
            if all(board[i][i] == PLAYER_COLOR[current_player] for i in range(BSIZ)) or \
                all(board[BSIZ - 1 - i ] == PLAYER_COLOR[current_player] for i in range(BSIZ)): # Verificamos la diagonal secudaria
                    return f"Jugador {current_player} ha ganado" 

        # Retornamos None si ninguno ha ganado
        return None


 	# Maneja el movimiento de una piedra seleccionada y verifica el estado del juego
    def move_st(i, j):
        '''If valid square, move there selected stone and unselect it,
        then check for end of game, then select new stone for next
        player unless all stones already played;
        if square not valid, do nothing and keep selected stone.
        Return 3 values: bool indicating whether a stone is
        already selected, current player, and boolean indicating
        the end of the game.
        '''
      
        # Coloca una piedra en la casilla selecionada si está vacía
        #Verificamos que la casilla esté vacía
        if board[i][j] == NO_PLAYER: 

            # Coloca la piedra del jugador actual 
            board[i][j] = PLAYER_COLOR[current_player]


 	# Dibuja el tablero en formato ASCII.
    def draw_txt(end = False):
        'Use ASCII characters to draw the board.'
        pass


    # return these 4 functions to make them available to the main program
    return stones, select_st, move_st, draw_txt