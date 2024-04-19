import pygame
import sys


from config import *

class Window:
  """
  Represents the game window for Tic Tac Toe.
  """
  def __init__(self):
    """
    Initialize the game window.
    """
    pygame.init()

    # Set up the game window
    self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption(f'{SIZE} X {SIZE} Tic Tac Toe!')
    self.screen.fill(BLACK)

    # Draw grid lines
    pygame.draw.rect(self.screen, WHITE, (0, 0, WIDTH, HEIGHT), LINE_THICKNESS*2)
    for i in range(1, SIZE):
        pygame.draw.rect(self.screen, WHITE, (0, 0, i*WIDTH/SIZE, HEIGHT), LINE_THICKNESS)
    for i in range(1, SIZE):
        pygame.draw.rect(self.screen, WHITE, (0, 0, WIDTH, i*HEIGHT/SIZE), LINE_THICKNESS)

    # Calculate cell dimensions
    self.cell_width =  WIDTH // SIZE
    self.cell_height = HEIGHT // SIZE
    
    pygame.display.update()


  def listen(self, callback):
    """
    Listen for user input events.

    Args:
        callback: Function to call when an input event occurs.
    """
    # start listening
    while True:
      for e in pygame.event.get():
        # if the event recived is close window
        if e.type == pygame.QUIT: 
            sys.exit(0)
        # if the event recived is a mousebutton click
        if e.type == pygame.MOUSEBUTTONDOWN: 
          # find the coordinates
          coord = pygame.mouse.get_pos()
          # convert coordinates to position(cell) clicked
          pos = self.find_pos_form_coord(coord)
          # send the pos to the callback by calling and passing pos as argument
          callback(pos=pos)


  def find_pos_form_coord(self, coord):
    """
    Convert coordinates to grid position.

    Args:
        coord: Tuple containing (x, y) coordinates.

    Returns:
        pos: Zero indexed position in the grid.
    """
    x, y = coord

    row = y // (WIDTH//SIZE)
    col = x // (WIDTH//SIZE)
    
    pos = row * SIZE + col
    return pos


  def disable_window(self):
    """
    Disable user input events.
    """
    pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
    
  def draw_symbol(self, player, pos):
    """
    Draw player's symbol on the grid.

    Args:
        player: Symbol to draw (X or O).
        pos: Position in the grid.
    """
    cell_width = WIDTH//SIZE
    cell_height = HEIGHT//SIZE

    font_size = int(cell_width)

    font_family = 'Arial'

    # identify player to set different colors and offset to correctly place the symbols
    if player == X:
        color = GREEN
        offset_x = cell_width*0.15
    elif player == O:
        color = BLUE
        offset_x = cell_width*0.1

    offset_y = -(cell_height*0.06)
    
    # Render symbol
    myfont = pygame.font.SysFont(font_family, font_size)
    textsurface = myfont.render(player, True, color)

    row = pos // SIZE
    col = pos % SIZE
    # Calculate position to draw symbol
    offset_x += col * cell_width
    offset_y += row * cell_height
    # Drawing the symbol and refreshing the window
    self.screen.blit(textsurface, (offset_x, offset_y))
    pygame.display.update()