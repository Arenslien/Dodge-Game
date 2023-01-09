# import library
import pygame
import random
from player import Player
from bullet import Bullet

# Initialize Pygame
pygame.init()

# 1. Variable Declare
clock = pygame.time.Clock()

# Screen Setting
screen_width = 680 # Screen Width
screen_height = 480 # Screen Height
screen = pygame.display.set_mode((screen_width, screen_height)) # Screen Setting

# Title Setting
pygame.display.set_caption("dodge") 

# Background Image
background = pygame.image.load("./image/background.jpg")

# Player Character Setting
player = Player("./image/spaceship.png", 30, 0.2)

# Level & Speed
level = 1
speed = [0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.11, 0.12, 0.13]

# Timer
play_time = 0

#################################
#          Start Screen         #
#################################
key_SPACE = False

level_x = 130
while True:
  screen.fill((0,0,0))
  
  # dodge game
  font = pygame.font.Font(None, 50)
  title = font.render("dodge game", True, (255, 255, 255))
  screen.blit(title, (240, 100))

  # press game
  font = pygame.font.Font(None, 50)
  space = font.render("press space", True, (255, 255, 255))
  screen.blit(space, (240, 150))

  # level
  level_text = font.render('level: ', True, (255, 255, 255))
  screen.blit(level_text, (70, 200))

  # level 1 ~ 10
  mouse = pygame.mouse.get_pos()

  for i in range(10):
    if level == i+1:
      level_text = font.render(str(i+1), True, (255, 0, 0))
    else:
      level_text = font.render(str(i+1), True, (255, 255, 255))
      
    screen.blit(level_text, (level_x+((i+1)*40), 200))

  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      for i in range(10):
        if mouse[0] in range(level_x+((i+1)*40), level_x+((i+1)*40)+20) and mouse[1] in range(200, 250):
          level = i+1

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        key_SPACE = True


  pygame.display.flip()

  if key_SPACE: break

# Bullet Setting
bullets = []

for i in range(20+level*2):
  bullets.append(Bullet(speed[level-1]))


#################################
#           Main Loop           #
#################################
running = True
start_ticks = pygame.time.get_ticks()

while running:
  df = clock.tick(60) # 게임 프레임 설정
  screen.blit(background, (0, 0))
  # 화면 그리기
  screen.blit(player.character, (player.x_pos, player.y_pos))

  for bullet in bullets:
    screen.blit(bullet.surface, (bullet.x_pos, bullet.y_pos))

  # 충돌시 종료
  for bullet in bullets:
    if bullet.checkCollision(player):
        running = False
        break

  for event in pygame.event.get():
    # QUIT 이벤트시 종료
    if event.type == pygame.QUIT:
      running = False

    # Player Chracter Event
    elif event.type == pygame.KEYDOWN:
      player.checkKeyDownEvent(event)
    elif event.type == pygame.KEYUP:
      player.checkKeyUpEvent(event)

  # 오브젝트 업데이트
  player.move(df) # 플레이어

  for bullet in bullets: # 총알
    bullet.move(df)

  pygame.display.flip()

end_ticks = pygame.time.get_ticks()

#################################
#          End Screen         #
#################################
key_SPACE = False

level_x = 130
running = True

while running:
  screen.fill((0,0,0))
  
  # dodge game
  font = pygame.font.Font(None, 50)
  title = font.render("Game Over", True, (255, 255, 255))
  screen.blit(title, (240, 100))

  # press game
  font = pygame.font.Font(None, 50)
  score = font.render("Score : {}".format((end_ticks - start_ticks)/1000), True, (255, 255, 255))
  screen.blit(score, (240, 150))
  
  pygame.display.flip()

  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        key_SPACE = True

  if key_SPACE: break

# Exit Pygame
pygame.quit()

