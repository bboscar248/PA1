# Import constants (assuming constants.py is in the same directory)
from constants import PLAYER_COLOR, BSIZ, NO_PLAYER, GRAY

# Data structure for stones
from collections import namedtuple

Stone = namedtuple('Stone', ('x', 'y', 'color'))


def set_board_up(stones_per_player=4):
    """
    Initializes the board and game state.

    Args:
        stones_per_player (int, optional): The number of stones each player starts with. Defaults to 4.

    Returns:
        tuple: A tuple containing functions for accessing and manipulating the game state.
    """

    # Initialize board with empty cells
    board = [[NO_PLAYER for _ in range(BSIZ)] for _ in range(BSIZ)]

    # List of played stones
    played_stones = []

    # Current player (0 or 1)
    current_player = 0

    # Flag for selected stone
    stone_selected = False

    # Flag for game end
    end = False

    # Total number of stones remaining
    total_stones = stones_per_player * 2

    def stones():
        """
        Returns an iterable of the played stones.
        """
        return iter(played_stones)

    def select_stone(i, j):
        """
        Selects a stone for the current player if it's their own stone.

        Args:
            i (int): Row index of the stone.
            j (int): Column index of the stone.

        Returns:
            bool: True if a stone was selected, False otherwise.
        """
        nonlocal stone_selected
        if board[i][j] == PLAYER_COLOR[current_player]:
            stone_selected = (i, j)
            return True
        return False

    def end():
        """
        Checks if there are three aligned stones on the board.

        Returns:
            bool: True if the game has ended, False otherwise.
        """
        # Check rows, columns, and diagonals for a win
        for i in range(BSIZ):
            if all(board[i][j] == board[i][0] and board[i][j] != NO_PLAYER for j in range(BSIZ)) or \
               all(board[j][i] == board[0][i] and board[j][i] != NO_PLAYER for j in range(BSIZ)):
                return True
        for i in range(BSIZ):
            if all(board[i][i] == board[0][0] and board[i][i] != NO_PLAYER for i in range(BSIZ)) or \
               all(board[i][BSIZ - 1 - i] == board[0][BSIZ - 1] and board[i][BSIZ - 1 - i] != NO_PLAYER for i in range(BSIZ)):
                return True
        return False

    def move_stone(i, j):
        """
        Moves a selected stone or places a new stone if the move is valid.

        Args:
            i (int): Row index of the destination square.
            j (int): Column index of the destination square.

        Returns:
            tuple: A tuple containing the stone selection state, current player, and game end state.
        """
        nonlocal stone_selected, current_player, end, total_stones

        # Check for valid coordinates
        if not (0 <= i < BSIZ and 0 <= j < BSIZ):
            return stone_selected, current_player, end

        # Place a new stone
        if total_stones > 0:
            if board[i][j] == NO_PLAYER:
                board[i][j] = PLAYER_COLOR[current_player]
                played_stones.append(Stone(i, j, PLAYER_COLOR[current_player]))
                total_stones -= 1
                current_player = 1 - current_player
                end = end()
                return stone_selected, current_player, end

        # Move existing stone
        if stone_selected:
            old_i, old_j = stone_selected
            if board[i][j] == NO_PLAYER:
                board[old_i][old_j] = NO_PLAYER
                board[i][j] = PLAYER_COLOR[current_player]
                played_stones.append(Stone(i, j, PLAYER_COLOR[current_player]))
                current_player = 1 - current_player
                end = end()
                stone_selected = False
                return stone_selected, current_player, end

        # Select stone for move
        if select_stone(i, j):
            return stone_selected, current_player, end

        return stone_selected, current_player, end

    def draw_txt():
        """
        Draws the board using ASCII characters.
        """
        for row in board:
            print(' '.join('X' if cell == 'X' else 'O' if cell == 'O' else '.' for cell in row))
        if end:
            print("El juego ha terminado.")
        else:
            print(f"Turno del jugador {current_player + 1}")

        return draw_txt

    # Return functions
    return stones, select_stone, move_stone, draw_txt