from game import Board
from gui import Window
from minimax import MiniMax
from config import *


class Game:
  def __init__(self) -> None:
    self.w = Window()
    self.b = Board()
    self.ai = MiniMax()
  
  def event(self, pos):
    curr_player = self.b.curr_player
    print("curr P: ", curr_player)
    updated = self.b.update_board(curr_player, pos)
    if updated:
      self.w.draw_symbol(curr_player, pos)

      game_end = self.b.check_game_end(curr_player)
      if game_end== 1:
        print("player: ", curr_player, "won!")
        self.w.disable_window()
      elif game_end == 0:
        print("Draw!")
      else:
        ai_move = self.ai.alphabeta(self.b,  float("-inf"), float("inf"), 0, self.b.get_curr_player())
        
        print("ai move", ai_move,self.b.get_curr_player())
        updated = self.b.update_board(self.b.get_curr_player(), ai_move[0])
        if updated:
          self.w.draw_symbol(O, ai_move[0])


  def start_game(self):
    self.w.listen(self.event)

if __name__ == "__main__":
  g = Game()
  g.start_game()