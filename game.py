# Example 3

# Import and initialize pygame
import pygame
from random import randint
pygame.init()
# Configure the screen
screen = pygame.display.set_mode([500, 500])


# Game Object
class GameObject(pygame.sprite.Sprite):
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    self.surf = pygame.image.load(image)
    self.x = x
    self.y = y
  
  def render(self, screen):
    screen.blit(self.surf, (self.x, self.y))


class Apple(GameObject):
  def __init__(self):
    super(Apple, self).__init__(0, 0, 'apple.png')
    self.dx = 0
    self.dy = (randint(0, 200) / 100) + 1
    self.reset()

  def move(self):
    self.x += self.dx
    self.y += self.dy
    if self.y > 500: 
      self.reset()

  def reset(self):
    self.x = randint(50, 400)
    self.y = -64
    


# Make an instance of GameObject
apple = Apple()


# Get the clock
clock = pygame.time.Clock()


# Create the game loop
running = True
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  # Clear screen
  screen.fill((255, 255, 255))
  # # Draw apple
  apple.move()
  apple.render(screen)
  # # Update the window
  pygame.display.flip()

  # tick the clock!
  clock.tick(60)