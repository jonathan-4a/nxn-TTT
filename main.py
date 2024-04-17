from game import Board
from gui import Window


class Game:
  def __init__(self) -> None:
    self.w = Window()
    self.b = Board()
  
  def event(self, pos):
    curr_player = self.b.get_curr_player()
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


  def start_game(self):
    self.w.listen(self.event)


if __name__ == "__main__":
  g = Game()
  g.start_game()