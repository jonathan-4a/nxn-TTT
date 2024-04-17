from config import *
from gui import Window

class Board:
  def __init__(self, size=SIZE) -> None:
    self.size = size
    self.state = [EMPTY]*self.size**2
    self.players = [X, O]
    self.total_moves = 0
    self.curr_player = self.players[0]

  def update_board(self, player, pos):
    if pos < len(self.state) and self.state[pos] == EMPTY:
      self.state[pos] = player
      self.total_moves += 1
      
      return True
    return False
  
  def get_empty_cells(self):
    return [p for p in range(len(self.state)) if self.state[p] == EMPTY]
  
  def get_opponent(self):
     return self.players[(self.total_moves + 1)%2]
  
  def get_curr_player(self):
    return self.players[(self.total_moves)%2]
  
  def check_game_end(self, player):

    # Check rows
    for i in range(0, self.size ** 2, self.size):
        if all(self.state[i + j] == player for j in range(self.size)):
            print("from rows")
            return 1

    # Check columns
    for i in range(self.size):
        if all(self.state[i + j * self.size] == player for j in range(self.size)):
            print("from cols")
            return 1

    # Check main diagonal
    if all(self.state[i * (self.size + 1)] == player for i in range(self.size)):
        print("from main d")
        return 1

    # Check anti-diagonal
    if all(self.state[(self.size - 1) * (i + 1)] == player for i in range(self.size)):
        print("from anit d")
        
        return 1
    
    # check for draw
    if self.total_moves == self.size**2: return 0

    # game still going
    return -1