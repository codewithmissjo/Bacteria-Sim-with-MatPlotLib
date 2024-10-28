import pygame
import random

class Virus(pygame.sprite.Sprite):
  def __init__(self, pos, split_time):
    super().__init__()
    # how the virus looks
    self.image = pygame.image.load("virus.png")
    self.image = pygame.transform.scale(self.image, (20, 20))
    self.rect = self.image.get_rect()
    # where is the virus
    self.rect.center = pos
    # how fast does it move
    self.speed = pygame.math.Vector2(0, 100)
    self.time = 0
    self.split_time = split_time

  def update(self, group):
    self.time += 1
    self.rect.move_ip(self.speed)
    #if the sprite touches the top or the bottom of the screen, the y speed needs to change direction
    if self.rect.top <= 0:
      self.speed[1] *= -1
      self.rect.top = 1
    elif self.rect.bottom >= 300:
      self.speed[1] *= -1
      self.rect.bottom = 299

    if self.rect.left <= 0:
      self.speed[0] *= -1
      self.rect.left = 1
    elif self.rect.right >= 400:
      self.speed[0] *= -1
      self.rect.right = 399

    if random.randint(0, 20) == 0:
      rotation = random.choice([-15, 15])
      self.speed.rotate_ip(rotation)

    if self.time % self.split_time == 0:
      group.add(Virus(self.rect.center, self.split_time))



      