# Copyright Lisa Kraatz 

# Imports
import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define Colors
black = '#000000'
white = '#ffffff'

# Player
playerWidth = 100

#  Game Screen
displayWidth = 800
displayHeight = 600
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))

pygame.display.set_caption('Name of game in progress')

# Game Clock (fps)
clock = pygame.time.Clock()

# Player Character Image
playerImg = (pygame.image.load('player.png'))

# Enemies
enemy1 = pygame.image.load('frog.png')
enemy2 = pygame.image.load('snail.png')
enemy3 = pygame.image.load('wasp.png')

randomEnemies = [enemy1, enemy2, enemy3]

class Enemy:
  def __init__(self):
    self.image = randomEnemy = random.choice(randomEnemies)
    self.x = random.randrange(0,displayWidth)
    self.y = -600 # Pixels off screen

    originalWidth = randomEnemy.get_width() 
    originalHeight = randomEnemy.get_height()
    self.width = int(originalWidth * 4) # transform.scale requires int
    self.height = int(originalHeight / originalWidth * self.width)
    
    self.image = pygame.transform.scale(randomEnemy,(self.width,self.height))

    self.speed = 3


# Score
def enemiesDodged(count):
  font = pygame.font.SysFont(None, 25)
  text = font.render('Dodged: '+ str(count), True, black)
  gameDisplay.blit(text, (0,0))

# Player 
def player(x,y):
  gameDisplay.blit(playerImg, (x,y)) # Bliting (Block Image Transfer): copies pixels from one surface onto another
  
 
# Message Box
def textObjects(text, font):
  textSurface = font.render(text, True, black)
  return textSurface, textSurface.get_rect() 

# Message Display
def msgDisplay(text):
  largeText = pygame.font.Font('freesansbold.ttf',115)
  textSurf, textRect = textObjects(text, largeText) # Reference surface, rectangle of text
  textRect.center = ((displayWidth / 2),displayHeight / 2)
  gameDisplay.blit(textSurf, textRect) 

  pygame.display.update()

  time.sleep(3)
  gameLoop() # Starts game over

# Crash function
def crash():
  msgDisplay('You crashed')


# Game Loop
def gameLoop():
  x = (displayWidth * 0.45) # Middle of screen (Player image is referenced from top left corner)
  y = (displayHeight * 0.7) # Bottom of screen

  xChange = 0

  # Initiate variables
  dodgeCount = 0
  gameExit = False

  enemy = Enemy()

  # Event Handling Loop
  while not gameExit:
    for event in pygame.event.get(): # (Get all events and put them in list)
      # Player exists window
      if (event.type == pygame.QUIT):
        pygame.quit()
        quit()

      # Key is pressed (Player Movement)
      if (event.type == pygame.KEYDOWN): 
        if (event.key == pygame.K_LEFT): # Left Arrow key
          xChange = -5
        elif (event.key == pygame.K_RIGHT): # Right Arrow Key
          xChange = 5

      # Key Release (Stop moving when not pressed)
      if (event.type == pygame.KEYUP):
        if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
          xChange = 0

    x += xChange # Update player position

    # Colorize screen
    gameDisplay.fill(white)

    # Display enemies

    enemyCount = random.randint(1,5)
    enemies = []

    for x in range(enemyCount):
      enemies.append(Enemy())

    for i in range(len(enemies)):
      gameDisplay.blit(en.image, (en.x, en.y))
      enemy.y += en.speed

      # Repeat enemies
      if (enemy.y > displayHeight):
        dodgeCount += 1
        
        newSpeed = enemy.speed
        enemies[i] = Enemy() # Create new enemy
        newSpeed += dodgeCount * 0.5
        enemy.speed = newSpeed
    

    # Show player
    player(x,y) 

    # Display dodge count
    enemiesDodged(dodgeCount)

    # Crash if edges of screen hit
    if (x > displayWidth - playerWidth or x < 0): # Minus playerWidth because of upper left corner)
      crash()

    # Enemy crash
    if (y < enemy.y + enemy.height): # Y crossover (bottom line of enemy)
      # X collission/ crossover
      if (x > enemy.x and x < (enemy.x + enemy.width) or (x + playerWidth > enemy.x and x + playerWidth < (enemy.x + enemy.width))):
        crash()


    # Update screen
    pygame.display.update() 
    clock.tick(60) # In fps 


# Run Game Loop
gameLoop()
# Quit
pygame.quit() # Kills game
quit() # Kills program


    


    




    

