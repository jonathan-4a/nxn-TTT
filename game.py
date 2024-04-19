from config import *

class Board:
  """
  Represents the game board for Tic Tac Toe.
  """
  def __init__(self, size=SIZE) -> None:
    """
    Initialize the game board.

    Args:
        size: Size of the board (default is SIZE from config).
    """
    self.size = size
    # Initialize the board state with all cells empty
    self.state = [EMPTY]*self.size**2
    # Define players
    self.players = [X, O]
    # Track total moves made on the board
    self.total_moves = 0
    # Current player to make a move
    self.curr_player = self.players[0]

  def update_board(self, player, pos):
    """
    Update the board with the player's move.

    Args:
        player: Player making the move (X or O).
        pos: Position where the move is made.

    Returns:
        True if the move is valid and made successfully, False otherwise.
    """
    if pos < len(self.state) and self.state[pos] == EMPTY:
      # Update the board state and track the move
      self.state[pos] = player
      self.total_moves += 1
      # updating the current player to the opponent
      self.curr_player = self.get_curr_player()
      return True
    return False
  
  def get_empty_cells(self):
    """
    Get a list of empty cells on the board.

    Returns:
        List of positions of empty cells.
    """
    return [p for p in range(len(self.state)) if self.state[p] == EMPTY]
  
  def get_opponent(self):
    """
    Get the opponent player.

    Returns:
        Opponent player (X or O).
    """
    return self.players[(self.total_moves + 1)%2]
  
  def get_curr_player(self):
    """
    Get the current player.

    Returns:
        Current player (X or O).
    """
    return self.players[(self.total_moves)%2]
  
  def check_game_end(self, player):
    """
    Check if the game has ended.

    Args:
        player: Player to check for win.

    Returns:
        WIN if the player wins, DRAW if the game is a draw, CONT if the game continues.
    """
    # Check rows, columns, and diagonals for win
    # Check rows 
    for i in range(0, self.size ** 2, self.size):
        if all(self.state[i + j] == player for j in range(self.size)):
            return WIN

    # Check columns
    for i in range(self.size):
        if all(self.state[i + j * self.size] == player for j in range(self.size)):
            return WIN

    # Check main diagonal
    if all(self.state[i * (self.size + 1)] == player for i in range(self.size)):
        return WIN

    # Check anti-diagonal
    if all(self.state[(self.size - 1) * (i + 1)] == player for i in range(self.size)):       
        return WIN

    # check for draw
    if self.total_moves == self.size**2: 
       return DRAW

    # Game is still ongoing
    return CONT