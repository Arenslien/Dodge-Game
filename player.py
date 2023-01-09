import pygame

class Player:
  move_left = False
  move_right = False
  move_up = False
  move_down = False

  def __init__(self, image, size, speed):
    self.character = pygame.image.load(image)
    self.size = size
    self.character = pygame.transform.scale(self.character, (self.size, self.size))
    self.x_pos = 680/2 - self.size/2
    self.y_pos = 480/2 - self.size/2
    self.speed = speed

  def move(self, df):
    if self.move_left:
      self.x_pos = self.x_pos - self.speed * df
    if self.move_right:
      self.x_pos = self.x_pos + self.speed * df
    if self.move_up:
      self.y_pos = self.y_pos - self.speed * df
    if self.move_down:
      self.y_pos = self.y_pos + self.speed * df

  def checkKeyDownEvent(self, event):
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT: 
        self.move_left = True
      if event.key == pygame.K_RIGHT:
        self.move_right = True
      if event.key == pygame.K_UP:
        self.move_up = True
      if event.key == pygame.K_DOWN:
        self.move_down = True
  
  def checkKeyUpEvent(self, event):
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT: 
        self.move_left = False
      if event.key == pygame.K_RIGHT:
        self.move_right = False
      if event.key == pygame.K_UP:
        self.move_up = False
      if event.key == pygame.K_DOWN:
        self.move_down = False