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

# Tupla para saber la piedra seleccionada o movida por el jugador según sus coordenadas "x", "y" y su "color"
Stone = namedtuple('Stone', ('x', 'y', 'color'))


def set_board_up(stones_per_player=4):
    'Init stones and board, prepare functions to provide, act as their closure'

    # init board and game data here

    # Estado compartido que encapsula toda la información necesaria
    state = {
        'board': [[NO_PLAYER] * BSIZ for _ in range(BSIZ)],  # Tablero vacío de medida BSIZ x BSIZ
        'played_stones': [],         # Lista de piedras jugadas
        'curr_player': 0,            # Jugador actual ("0" es el jugador 1 o "1" es el jugador 2). Las fichas del jugador 1 serán 'X' y 'O' del jugador 2
        'stone_selected': True,      # Para saber si se ha seleccionado una piedra o no después de que los dos jugadores hayan movido todas sus piedras disponibles
        'total_stones': stones_per_player * 2,  # Total de piedras disponibles entre los dos jugadores
        'stone_itself': (None, None)  # Coordenadas de la piedra seleccionada
    }

    def stones():
        "return iterable with the stones already played"
        return state['played_stones']

    # Llamamos esta función una vez que todas las piedras sean jugadas. Seleccionamos
    # la piedra que queremos mover y retornamos True si el jugador ha colocado la piedra
    # en una casilla vacía
    def select_st(i, j):

        '''
        Select stone that current player intends to move. 
        Player must select a stone of his own.
        To be called only after all stones played.
        Report success by returning a boolean;
        '''

        # Guardamos el valor de clave 'board' en la variable board
        board = state['board']

        # Guardamos el valor de clave 'curr_player' en la variable curr_player
        curr_player = state['curr_player']

        # Miramos si se trata del jugador 0 que tiene que seleccionar la piedra y nos aseguramos también
        # de que las coordenadas "i" y "j" estén dentro del rango del tablero
        if curr_player == 0 and 0 <= i < BSIZ and 0 <= j < BSIZ:

            # Nos aseguramos de que la casilla seleccionada por el jugador sea una de sus piedras
            if board[i][j] == 'X':

                # Guardamos las coordenadas de la casilla seleccionada y guardamos las coordenadas
                # "x" y "y" en la variable stone_itself
                state['stone_itself'] = (i, j)

                # Incrementamos +1 al número total de piedras disponibles porque ahora el jugador 1 
                # ya puede mover una de sus piedras                  
                state['total_stones'] += 1

                # Hacemos que la variable stone_selected sea True para indicar que ya se ha seleccionado
                # una piedra                
                state['stone_selected'] = True

                # Retornamos True para reportar éxito
                return True
            
            # Retornamos False si la casilla seleccionada por el jugador no es una de sus piedras
            return False
        
        # Hacemos lo mismo que con el jugador 2 
        elif curr_player == 1 and 0 <= i < BSIZ and 0 <= j < BSIZ:
            if board[i][j] == 'O':
                state['stone_itself'] = (i, j)
                state['total_stones'] += 1
                state['stone_selected'] = True
                return True
            
            return False

    # Función para comprobar si los jugadores han hecho '' en raya horizontalmente, verticalmente o diagonalmente
    def end():

        'Test whether there are 3 aligned stones'

        # Guardamos el valor de la clave 'board' en la variable board 
        board = state['board']

        # Comprobar por filas
        for i in range(BSIZ):

            # Comprobamos si la primera piedra de la fila 'i' ([board[i][0]]) es igual que los otros elementos que 
            # también están en la misma fila (board[i][j]). Además, nos aseguramos que las casillas que estamos
            # comprobando no sea vacía (board[i][j] != " ").            
            if all(board[i][j] == board[i][0] and board[i][j] != NO_PLAYER for j in range(BSIZ)):
                
                # Retornamos True si alguna de las filas cumple lo anteriormente dicho
                return True

        # Comprobar por columnas
        for j in range(BSIZ):

            # Comprobamos si la primera piedra de la columna 'j' ([board[0][j]]) es igual que los otros elementos que 
            # también están en la misma columna (board[i][j]). 
            if all(board[i][j] == board[0][j] and board[i][j] != NO_PLAYER for i in range(BSIZ)):
                
                # Retornamos True si alguna de las columnas cumple lo anteriormente dicho
                return True

        # Comprobar por la diagonal principal:
        # Comprobamos si la piedra que se encuentra en la primera fila y columna (board[0][0]) es igual que los demás
        # piedras que se encuentran en la diagonal principal (board[i][i])
        if all(board[i][i] == board[0][0] and board[i][i] != NO_PLAYER for i in range(BSIZ)):
            
            # Retornamos True si la diagonal principal cumple lo anteriormente dicho
            return True

        # Comprobar por la diagonal secundaria
        # Comprobamos si la piedra que se encuentra en la primera fila y última columna (board[0][BSIZ-1]) es igual 
        # que los demás piedras que se encuentran en la diagonal secundaria (board[i][BSIZ - 1 - i])
        if all(board[i][BSIZ - 1 - i] == board[0][BSIZ - 1] and board[i][BSIZ - 1 - i] != NO_PLAYER for i in range(BSIZ)):
            
            # Retornamos True si la diagonal secundaria cumple lo anteriormente dicho
            return True

        # Si ninguna de las condiciones anteriores fueron ciertas, quiere decir que el juego aún no ha acabado
        return False


     # Función para mover las piedras dado unas coordenadas "i" y "j"
    def move_st(i, j):

        '''If valid square, move there selected stone and unselect it,
        then check for end of game, then select new stone for next
        player unless all stones already played; if square not valid, 
        do nothing and keep selected stone.
        
        Return 3 values: bool indicating whether a stone is
        already selected, current player, and boolean indicating
        the end of the game.
        '''

        # Guardamos los valores de las claves en variables con el mismo nombre que la clave 
        board = state['board']
        played_stones = state['played_stones']
        curr_player = state['curr_player']
        stone_selected = state['stone_selected']
        stone_itself = state['stone_itself']
        total_stones = state['total_stones']

        # Obtenemos las coordenadas "x" e "y" de la piedra seleccionada. Esto solo tendrá sentido una vez 
        # después de llamar a la función select_st(). Si no se ha llamado select_st(), "x" e "y" son "None"
        x, y = stone_itself

        # Nos aseguramos que las coordenadas seleccionadas por el jugador estén dentro del rango del tablero
        if not (0 <= i < BSIZ and 0 <= j < BSIZ) or board[i][j] != NO_PLAYER:
            return stone_selected, curr_player, end()

        # Nos aseguramos que la casilla escogida esté vacía
        if board[i][j] != " ": 
            return True, curr_player, end()

        # Si ninguno de las anteriores condiciones fueron ciertas, entonces, movemos la piedra del jugador 
        # actual a las coordenadas "i" y "j" que haya introducido
        if stone_selected:

            # Esto solo tiene sentido después de haber llamado a select_st()
            # Vemos si ha seleccionado alguna piedra o no en la función select_st()
            if x is not None and y is not None:

                # Eliminamos la piedra seleccionada por el jugador de la lista played_stones
                played_stones.remove(Stone(x, y, PLAYER_COLOR[curr_player]))
                
                # Hacemos que la casilla donde estaba la piedra seleccionada por el jugador esté vacía otra vez 
                board[x][y] = NO_PLAYER

            # Imprimos una 'X' en la casilla donde quiere mover la piedra el jugador 1, si es el jugador 2 imprimimos 'O'
            board[i][j] = 'X' if curr_player == 0 else 'O'

            # Añadimos la piedra jugada por el jugador actual en la lista played_stones
            played_stones.append(Stone(i, j, PLAYER_COLOR[curr_player]))
            
            # Cambiamos de jugador actual            
            state['curr_player'] = 1 - curr_player

            # Restamos -1 a la variable 'total_stones' para saber las piedras que aun están disponibles
            state['total_stones'] -= 1

            # Miramos el total de piedras aun disponibles, si es cero...
            if state['total_stones'] == 0:

                # ...entonces stone_selected = False porque ya no hay más piedras que mover por parte de los 
                # dos jugadores. De esta manera, entraríamos al bucle while donde el jugador actual tendría 
                # que seleccionar una de sus piedras y moverla
                state['stone_selected'] = False

        # Return 3 values: bool indicating whether a stone is already selected, current player, and boolean indicating the end of the game. 
        return state['stone_selected'], state['curr_player'], end()


    # Función para imprimir el tablero
    def draw_txt(end=False):

        '''
        Use ASCII characters to draw the board.
        '''

        # Guardamos el valor de la clave 'board' en la variable board
        board = state['board']

        # Recorre cada fila del tablero       
        for row in range(BSIZ):

            # Recorre cada columna de la fila actual            
            for col in range(BSIZ):

                # Si no es la última columna, imprime el contenido de la celda seguido de una barra vertical "|"
                if col < BSIZ - 1:
                    print("", board[row][col], "|", end="")


                # Si es la última columna, solo imprime el contenido de la celda
                else:

                    # Imprimimos " " para representar las casillas vacías, en vez de que salga -1 (NO_PLAYER))
                    if board[row][col] == NO_PLAYER:     
                        print("", " ", end="")

                    # Si no es una casilla vacía, imprime el valor que se encuentra en esos índices
                    print("", board[row][col], end="")

            # Termina la fila actual y pasa a una nueva línea
            print()

            # Si no es la última fila, imprime una línea divisoria con guiones para separar las filas
            if row < BSIZ - 1:
                print("-" * (BSIZ * 4 - 1))

    # return these 4 functions to make them available to the main program
    return stones, select_st, move_st, draw_txt
