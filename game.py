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

# Initiate variables
crashed = False

# Loop 
while not crashed:
  for event in pygame.event.get(): # (Get all events and put them in list)
    if (event.type == pygame.QUIT): # If player clicks x (exits window)
      crashed = True # Ends loop (for now)

  pygame.display.update() # Updates screen
  clock.tick(30) # In fps 

# Quit
pygame.quit() # Kills game
quit() # Kills program


    


    




    

