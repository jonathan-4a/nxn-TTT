from config import *
from copy import deepcopy

class MiniMax:
  """
  Implements the Minimax algorithm with alpha-beta pruning for Tic Tac Toe.
  """
  def alphabeta(self, board, alpha, beta, depth, player):
    """
    Minimax algorithm with alpha-beta pruning.

    Args:
        board: Current game board.
        alpha: Alpha value for pruning.
        beta: Beta value for pruning.
        depth: Current depth in the search tree.
        player: Current player (X or O).

    Returns:
        List containing the optimal move and its utility value.
    """
    if player == X:
        # Initialize optimal move for maximizing player
        optimal_move = [-1, float("-inf")]
    else:
        # Initialize optimal move for minimizing player
        optimal_move = [-1, float("inf")]
    # Get empty cells on the board
    empty_cells = board.get_empty_cells()

    # Check for terminal states
    if board.check_game_end(X) == WIN:
        # If X wins, return positive infinity (the highest possible)
        return [-1, float('inf')]
    if board.check_game_end(O) == WIN:
        # If O wins, return negative infinity (the lowest possible)
        return [-1, float('-inf')]
    if board.check_game_end(O) == DRAW:
        # If it's a draw, return 0
        return [-1, 0]
    
    # Evaluate leaf nodes
    if depth == DEPTH:
        # If the depth reachs the configured depth
        # Evaluate the utility of the current state instead of continuing
        result = self.eval_fun(board.state)
        return [-1, result]
    
    # Explore possible moves
    for cell in empty_cells:
        # Create a copy of the board
        temp_board = deepcopy(board)
        opp_player = temp_board.get_opponent()
        # Make a hypothetical move
        temp_board.update_board(player, cell)
        # Recursively call alphabeta for the current board
        score = self.alphabeta(temp_board, alpha, beta, depth + 1, opp_player)
        # Record the current move
        score[0] = cell
        # If minimizing player
        if player == O: 
            # If the score is less than current optimal score Update the optimal move (for minimizing)
            if score[1] < optimal_move[1]:
                optimal_move = score
            # Update beta value
            beta = min(beta, optimal_move[1])
            # Prune the branch if beta is less than or equal to alpha by breaking
            if beta <= alpha:
                break
        else:
            if score[1] > optimal_move[1]:
                optimal_move = score
            alpha = max(alpha, optimal_move[1])
            # Prune the branch if beta is less than or equal to alpha
            if beta <= alpha:
                break
    return optimal_move


  def eval_fun(self, state):
      """
      Evaluation function to determine the utility of a given state.

      Args:
          state: Current state of the board.

      Returns:
          Utility value of the state.
      """
      n = int(len(state)**0.5)
      # Dictionary to store count of X's and O's in a row/column/diagonal
      x_count = dict.fromkeys(range(n+1), 0)
      o_count = dict.fromkeys(range(n+1), 0)
      # the idea of this algorithm is it checks if the other 
      # players symbol is not in the row, col, or diagnols
      # and if so increments the value for the associated key (number of symbols)
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

      # Check diagonals
      main_d = []
      anti_d = []

      for i in range(0, len(state), n):
        row = state[i:i+n]
        main_d.append(row[int(i/n)])
        anti_d.append(row[n - int(i/n) - 1])

      # If there's no O in the main diagonal
      if O not in main_d:
          x_count[main_d.count(X)] += 1
      if X not in main_d:
          o_count[main_d.count(O)] += 1

      if O not in anti_d:
          x_count[anti_d.count(X)] += 1
      if X not in anti_d:
          o_count[anti_d.count(O)] += 1

      x_utility = 0
      # Calculate utility based on counts
      # I have weighted the counts with four so with the additional one symbols we have
      # without oppoents sysmbol in row, col, or diagonal, it in increased by four
      for k, v in x_count.items():
          x_utility += 4*k*v

      o_utility = 0

      for k, v in o_count.items():
          o_utility += 4*k*v
      # subtracting O to X => X is maximizing and O is minimizing
      return x_utility - o_utility
