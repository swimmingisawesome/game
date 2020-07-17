import pygame
pygame.init()
from Tapir import *
from Lion import *

screen_info = pygame.display.Info()
print(screen_info)

w = pygame.display.set_mode((800, 600))
c = pygame.time.Clock()
color = (0, 255, 0)




Player1 = Tapir((20, 300))
Player2 = Lion((780, 300))



def main():
  while True:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key== pygame.K_RIGHT:
          Player1.speed[0] = 10
        if event.key== pygame.K_DOWN:
          Player1.speed[1] = 10
        if event.key== pygame.K_UP:
          Player1.speed[1] = -10
        if event.key== pygame.K_LEFT:
          Player1.speed[0] = -10
        if event.key == pygame.K_d:
          Player2.speed[0] = 10
        if event.key== pygame.K_s:
          Player2.speed[1] = 10
        if event.key== pygame.K_w:
          Player2.speed[1] = -10
        if event.key== pygame.K_a:
          Player2.speed[0] = -10
      if event.type == pygame.KEYUP:
        if event.key== pygame.K_d:
          Player2.speed[0] = 0
        if event.key== pygame.K_s:
          Player2.speed[1] = 0
        if event.key== pygame.K_w:
          Player2.speed[1] = 0
        if event.key== pygame.K_a:
          Player2.speed[0] = 0

        if event.key== pygame.K_RIGHT:
          Player1.speed[0] = 0
        if event.key== pygame.K_DOWN:
          Player1.speed[1] = 0
        if event.key== pygame.K_UP:
          Player1.speed[1] = 0
        if event.key== pygame.K_LEFT:
          Player1.speed[0] = 0
    
    Player1.update()
    Player2.update()
    c.tick(60)
    w.fill(color)
    w.blit(Player1.image, Player1.rect)
    w.blit(Player2.image, Player2.rect)
    pygame.display.flip()


if __name__=='__main__':
  main() 

