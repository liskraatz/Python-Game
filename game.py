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

# Enemy Images
enemy1 = pygame.image.load('frog.png')
enemy2 = pygame.image.load('snail.png')
enemy3 = pygame.image.load('wasp.png')

randomEnemies = [enemy1, enemy2, enemy3]

# Score
def enemiesDodged(count):
  font = pygame.font.SysFont(None, 25)
  text = font.render('Dodged: '+ str(count), True, black)
  gameDisplay.blit(text, (0,0))

# Player 
def player(x,y):
  gameDisplay.blit(playerImg, (x,y)) # Bliting (Block Image Transfer): copies pixels from one surface onto another

# Enemies (Obstacles)
def enemies(image, enemyX, enemyY, enemyW, enemyH):
  gameDisplay.blit(image, (enemyX, enemyY))
 
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

  # Create enemy objects
  randomEnemy = random.choice(randomEnemies)
  originalWidth = randomEnemy.get_width() 
  originalHeight = randomEnemy.get_height()

  enemyStartX = random.randrange(0,displayWidth)
  enemyStartY = -600 # Pixels off screen
  enemySpeed = 4
  enemyWidth = int(originalWidth * 2) # trasform.scale requires int
  enemyHeight = int(originalHeight / originalWidth * enemyWidth)
  randomEnemy = pygame.transform.scale(randomEnemy,(enemyWidth,enemyHeight))

  # Initiate variables
  dodgeCount = 0
  gameExit = False

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

    # Enemies
    enemies(randomEnemy, enemyStartX, enemyStartY, enemyWidth, enemyHeight)
    enemyStartY += enemySpeed

    # Repeat enemy (blocks)
    if (enemyStartY > displayHeight):
      randomEnemy = random.choice(randomEnemies)
      enemyStartY = 0 - enemyHeight # Resets Y
      enemyStartX = random.randrange(0,displayWidth) # Resets X
      dodgeCount += 1

      # Difficulty
      enemySpeed += 0.5
      #enemyWidth += int((dodgeCount * 1.2))
      #enemyHeight += int((dodgeCount * 1.2))
      #randomEnemy = pygame.transform.scale(randomEnemy,(enemyWidth,enemyHeight)) # Scale image to fix hitbox
      enemyCount += 1
      

    # Show player
    player(x,y) 

    # Display dodge count
    enemiesDodged(dodgeCount)

    # Crash if edges of screen hit
    if (x > displayWidth - playerWidth or x < 0): # Minus playerWidth because of upper left corner)
      crash()

    # Enemy crash
    if (y < enemyStartY + enemyHeight): # Y crossover (bottom line of enemy)
      # X collission/ crossover
      if (x > enemyStartX and x < (enemyStartX + enemyWidth) or (x + playerWidth > enemyStartX and x + playerWidth < (enemyStartX + enemyWidth))):
        crash()


    # Update screen
    pygame.display.update() 
    clock.tick(60) # In fps 


# Run Game Loop
gameLoop()
# Quit
pygame.quit() # Kills game
quit() # Kills program


    


    




    

