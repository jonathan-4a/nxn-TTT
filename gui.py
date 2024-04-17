import pygame
import sys


from config import *

class Window:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption(f'{SIZE} X {SIZE} Tic Tac Toe!')
    self.screen.fill(BEIGE)
    pygame.draw.rect(self.screen, BLACK, (0, 0, WIDTH, HEIGHT), LINE_THICKNESS*2)

    for i in range(1, SIZE):
        pygame.draw.rect(self.screen, BLACK, (0, 0, i*WIDTH/SIZE, HEIGHT), LINE_THICKNESS)
    for i in range(1, SIZE):
        pygame.draw.rect(self.screen, BLACK, (0, 0, WIDTH, i*HEIGHT/SIZE), LINE_THICKNESS)

    self.cell_width =  WIDTH // SIZE
    self.cell_height = HEIGHT // SIZE
    
    pygame.display.update()


  def listen(self, callback):
      while True:
        for e in pygame.event.get():
          if e.type == pygame.QUIT: 
              sys.exit(0)

          if e.type == pygame.MOUSEBUTTONDOWN: 
            coord = pygame.mouse.get_pos()
            pos = self.find_pos_form_coord(coord)
            callback(pos=pos)


  def find_pos_form_coord(self, coord):
    x, y = coord

    row = y // (WIDTH//SIZE)
    col = x // (WIDTH//SIZE)
    
    pos = row * SIZE + col
    return pos

  def disable_window(self):
     pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
    
  def draw_symbol(self, player, pos):
      
      cell_width = WIDTH//SIZE
      cell_height = HEIGHT//SIZE

      font_size = int(cell_width)

      font_family = 'Arial'

      
      if player == X:
          color = GREEN
          offset_x = cell_width*0.15
      elif player == O:
          color = BLUE
          offset_x = cell_width*0.1

      offset_y = -(cell_height*0.06)
      
      myfont = pygame.font.SysFont(font_family, font_size)
      textsurface = myfont.render(player, True, color)  # text, anti-alias, color 

      print(pos)

      row = pos // SIZE
      col = pos % SIZE

      offset_x += col * cell_width
      offset_y += row * cell_height
      print()
      self.screen.blit(textsurface, (offset_x, offset_y))
      pygame.display.update()