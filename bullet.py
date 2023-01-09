import random
import pygame

class Bullet:
  surface = pygame.image.load("./image/circle.png")
  size = 7
  surface = pygame.transform.scale(surface, (size, size))
  x_direction = 1
  y_direction = 1

  def __init__(self, speed):
    self.speed = random.uniform(speed-0.03, speed+0.03)
    self.spawnPoint = random.choice(['left', 'right', 'up', 'down'])

    if self.spawnPoint == 'up':
      self.x_pos = random.randint(0, 680 - self.size)
      self.y_pos = 0

    if self.spawnPoint == 'down':
      self.x_pos = random.randint(0, 680 - self.size)
      self.y_pos = 480 - self.size 

    if self.spawnPoint == 'left':
      self.x_pos = 0
      self.y_pos = random.randint(0, 480 - self.size)

    if self.spawnPoint == 'right':
      self.x_pos = 680 - self.size
      self.y_pos = random.randint(0, 480 - self.size)

  def move(self, df):
    if self.x_pos <= 0:
      self.x_direction = 1
    if self.x_pos >= 680-7:
      self.x_direction = -1
    if self.y_pos < 0:
      self.y_direction = 1
    if self.y_pos >= 480-7:
      self.y_direction = -1
    
    self.x_pos = self.x_pos + self.speed * self.x_direction * df
    self.y_pos = self.y_pos + self.speed * self.y_direction * df
  
  def checkCollision(self, player):
    return abs(self.x_pos - player.x_pos) < 1.5 and abs(self.y_pos - player.y_pos) < 1.5
