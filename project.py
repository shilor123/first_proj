import pygame
pygame.init()
back = (0, 255, 0) 
mw = pygame.display.set_mode((500, 500)) 
mw.fill(back) 
clock = pygame.time.Clock()
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None): 
      self.rect = pygame.Rect(x, y, width, height) 
      self.fill_color = back 
      if color: 
          self.fill_color = color 
    def color(self, new_color): 
      self.fill_color = new_color 
    def fill(self): 
      pygame.draw.rect(mw, self.fill_color, self.rect) 
    def collidepoint(self, x, y): 
      return self.rect.collidepoint(x, y)       
    def colliderect(self, rect): 
      return self.rect.colliderect(rect)

class Picture(Area): 
    def __init__(self, filename, x=0, y=0, width=10, height=10): 
      Area.__init__(self, x=x, y=y, width=width, height=height, color=None) 
      self.image = pygame.image.load(filename)

    def draw(self): 
      mw.blit(self.image, (self.rect.x, self.rect.y))