# Copyright Lisa Kraatz 

# Imports
import pygame
import time

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
playerImg = pygame.image.load('player.png')
def player(x,y):
  gameDisplay.blit(playerImg, (x,y)) # Bliting player image to coordinates 

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
  gameExit = False

  # Event Handling Loop
  while not gameExit:
    for event in pygame.event.get(): # (Get all events and put them in list)
      # Player exists window
      if (event.type == pygame.QUIT):
        pygame.quit()
        quit()

      # Key is pressed
      if (event.type == pygame.KEYDOWN): 
        if (event.key == pygame.K_LEFT): # Left Arrow key
          xChange = -5
        elif (event.key == pygame.K_RIGHT): # Right Arrow Key
          xChange = 5

      # Key Release
      if (event.type == pygame.KEYUP):
        if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
          xChange = 0

    
          
    x += xChange # Update player position

    gameDisplay.fill(white) # Colorize screen
    player(x,y) # Show player

    # Crash if edges of screen hit
    if (x > displayWidth - playerWidth or x < 0): # Minus playerWidth because of upper left corner)
      crash()


    # Update screen
    pygame.display.update() 
    clock.tick(60) # In fps 

# Run Game Loop
gameLoop()
# Quit
pygame.quit() # Kills game
quit() # Kills program


    


    




    

