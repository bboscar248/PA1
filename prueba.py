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

    # init board and game data here

    # Inicializamos la tabla BSIZxBSIZ con las casillas vacías
    board = [[NO_PLAYER]*BSIZ for _ in range(BSIZ)]

    # Lista para guardar las piedras jugadas
    played_stones = []

    # Para saber a qué jugador le toca // 0 --> Jugador 1 y 1 --> Jugador 2 
    # También tenemos pensado la ficha 'X' para el jugador 1 y la ficha 'O' para el jugador 2
    curr_player = 0

    # Para saber si se ha seleccionado una piedra o no
    stone_selected = True

    # Para saber si el juego ha terminado o no
    end = False

    # El número total de piedras disponibles
    total_stones = stones_per_player * 2
    

    def stones():
        "return iterable with the stones already played"
        for item in played_stones:
            return item


    # Llamamos esta función una vez que todas las piedras sean jugadas. Seleccionamos
    # la piedra que queremos mover y retornamos un boolean si ha colocado la piedra
    # en una casilla vacía
    def select_st(i, j):

        '''
        Select stone that current player intends to move. 
        Player must select a stone of his own.
        To be called only after all stones played.
        Report success by returning a boolean;
        '''
        
        # Hacemos que la variable curr_player sea nonlocal
        nonlocal curr_player

        pass


    # Para comprobar si han hecho 3 en raya horizontalmente, verticalmente o diagonalmente
    def end():
        'Test whether there are 3 aligned stones'

        # Comprobar filas
        for i in range(BSIZ):
            if all(board[i][j] == board[i][0] and board[i][j] != NO_PLAYER for j in range(BSIZ)):
                return True

        # Comprobar columnas
        for j in range(BSIZ):
            if all(board[i][j] == board[0][j] and board[i][j] != NO_PLAYER for i in range(BSIZ)):
                return True

        # Comprobar diagonal principal
        if all(board[i][i] == board[0][0] and board[i][i] != NO_PLAYER for i in range(BSIZ)):
            return True

        # Comprobar diagonal secundaria
        if all(board[i][BSIZ - 1 - i] == board[0][BSIZ - 1] and board[i][BSIZ - 1 - i] != NO_PLAYER for i in range(BSIZ)):
            return True
        
        # Si ninguna de las condiciones anteriores fueron ciertas, quiere decir que el juego aún no ha acabado
        return False


    def move_st(i, j):

        '''If valid square, move there selected stone and unselect it,
        then check for end of game, then select new stone for next
        player unless all stones already played; if square not valid, 
        do nothing and keep selected stone.
        
        Return 3 values: bool indicating whether a stone is
        already selected, current player, and boolean indicating
        the end of the game.
        '''

        # Hacemos que las variables curr_player, stone_selected, end y total_stones sean nonlocal
        nonlocal curr_player, stone_selected, end, total_stones
        
        # stone_selected, curr_player, end = move_st(int(i), int(j))

        # Nos aseguramos que las coordenadas seleccionados por el jugador estén dentro del rango del tablero
        if not(0 <= i < BSIZ and 0 <= j < BSIZ): 
            return True, curr_player, end
        
        # Nos aseguramos que la casilla escogida esté vacía
        if board[i][j] != NO_PLAYER: 
            return True, curr_player, end

        # Si ninguno de los anteriores fueron ciertas, entonces, movemos la piedra del jugador a las coordenadas que haya concretado
        if stone_selected:  

            # Si se trata del jugador 1
            if curr_player == 0: 
                board[i][j] = 'X'

            # Si se trata del jugador 2
            elif curr_player == 1: 
                board[i][j] = 'O'

            # Cambiamos de jugador
            curr_player = 1 - curr_player

            # Restamos -1 a la variable 'total_stones' para saber las piedras aún disponibles
            total_stones -= 1

            if total_stones < 2: 
                # Vemos si alguno de los jugadores ha ganado o no
                end = end()

            # Tenemos que ver que si las piedras disponibles es 0, que stone_selected = False
            if total_stones == 0: 

                # Ya no hay más piedras que seleccionar
                stone_selected = False

        # Return 3 values: bool indicating whether a stone is already selected, current player, and boolean indicating the end of the game. 
        return stone_selected, curr_player, end

    

    def draw_txt(end = False):
        'Use ASCII characters to draw the board.'
        pass


    # return these 4 functions to make them available to the main program
    return stones, select_st, move_st, draw_txt