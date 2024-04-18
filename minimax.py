from config import *
from copy import deepcopy

class MiniMax:

  def alphabeta(self, board, alpha, beta, depth, player):

      if player == X:
          best = [-1, float("-inf")]
      else:
          best = [-1, float("inf")]

      empty_cells = board.get_empty_cells()

      if board.check_game_end(X) == WIN:
          return [-1, float('inf')]
      if board.check_game_end(O) == WIN:
          return [-1, float('-inf')]
      if board.check_game_end(O) == DRAW:
          return [-1, 0]
      

      if depth == DEPTH:
          result = self.eval_fun(board.state)
          return [-1, result]
      

      for cell in empty_cells:
          temp_board = deepcopy(board)
          opp_player = temp_board.get_opponent()
          temp_board.update_board(player, cell)
          score = self.alphabeta(temp_board, alpha, beta, depth + 1, opp_player)
          score[0] = cell
          if player == O:
              if score[1] < best[1]:
                  best = score
              beta = min(beta, best[1])
              if beta <= alpha:
                  break
          else:
              if score[1] > best[1]:
                  best = score
              alpha = max(alpha, best[1])
              if beta <= alpha:
                  break
      return best


  def eval_fun(self, state):
      n = int(len(state)**0.5)

      x_count = dict.fromkeys(range(n+1), 0)
      o_count = dict.fromkeys(range(n+1), 0)

      # Check rows
      for i in range(0, len(state), n):
          row = state[i:i+n]
          if O not in row:
              x_count[row.count(X)] += 1
          if X not in row:
              o_count[row.count(O)] += 1

      # Check columns
      for i in range(n):
          col = state[i:len(state): n]
          if O not in col:
              x_count[col.count(X)] += 1
          if X not in col:
              o_count[col.count(O)] += 1

      # # Check diagonals
      main_d = []
      anti_d = []

      for i in range(0, len(state), n):
        row = state[i:i+n]
        main_d.append(row[int(i/n)])
        anti_d.append(row[n - int(i/n) - 1])
      
      if O not in main_d:
          x_count[main_d.count(X)] += 1
      if X not in main_d:
          o_count[main_d.count(O)] += 1

      if O not in anti_d:
          x_count[anti_d.count(X)] += 1
      if X not in anti_d:
          o_count[anti_d.count(O)] += 1

      x_utility = 0

      for k, v in x_count.items():
          x_utility += 2*k*v

      o_utility = 0

      for k, v in o_count.items():
          o_utility += 2*k*v

      return x_utility - o_utility
