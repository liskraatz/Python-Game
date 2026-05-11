# Copyright Lisa Kraatz 

# Imports
import pygame

# Initialize pygame
pygame.init()

# Define Colors
black = '#000000'
white = '#ffffff'

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

x = (displayWidth * 0.45) # Middle of screen (Player image is referenced from top left corner)
y = (displayHeight * 0.7) # Bottom of screen

xChange = 0



# Initiate variables
crashed = False

# Event Handling Loop
while not crashed:
  for event in pygame.event.get(): # (Get all events and put them in list)
    # Player exists window
    if (event.type == pygame.QUIT):
      crashed = True # Ends loop (for now)
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

  x += xChange # 


  gameDisplay.fill(white) # Colorize screen
  player(x,y) # Show player
  pygame.display.update() # Update screen
  clock.tick(60) # In fps 

# Quit
pygame.quit() # Kills game
quit() # Kills program


    


    




    

