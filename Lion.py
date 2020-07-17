import pygame

class Lion(pygame.sprite.Sprite): 
  def __init__(self, pos):
    super().__init__()
    self.image = pygame.image.load('lion1.png')
    self.image = pygame.transform.smoothscale(self.image, (100, 100))
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.image = pygame.transform.rotate(self.image, int(0))

    self.speed = pygame.math.Vector2(0, 0)

  def update(self):
    self.rect.move_ip(self.speed)
    if self.rect.top < 0 or self.rect.bottom > 600:
      self.speed[1] *= -1
      self.image = pygame.transform.flip(self.image, False, True)
      self.rect.move_ip(0, self.speed[1])    

    if self.rect.right < 0 or self.rect.left > 800:
      self.speed[0] *= -1
      self.image = pygame.transform.flip(self.image, True, False)
      self.rect.move_ip(self.speed[0], 0)  

  
