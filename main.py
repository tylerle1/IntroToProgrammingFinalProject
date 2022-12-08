# Hangman game using python

# sources
# https://www.youtube.com/watch?v=8SzTzvrWaAA&ab_channel=ClearCode

# import libraries
import pygame, sys
import random


# game settings
FPS = 30
HEIGHT = 600
WIDTH = 800
# font = pygame.font.SysFont('Arial', 35)


# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


# load hangman images
# make images a list
images = []
# create a loop that runs 7 times for each image
for i in range(7):
    # each time the loop runs it adds a number so we can load every image
    image = pygame.image.load("hangman" + str(i) + ".png")
    # "append" adds it
    images.append(image)

# game variables
game_status = 0

# initiate pygame and create a window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


# create class for buttons with letters
class Button:
    def __init__(self, pos, width, height, text)

# make clock
clock = pygame.time.Clock()

running = True

# Game loop
while running:
    clock.tick(FPS)

    screen.fill(WHITE)

    # draw buttons
    
    # blit function goes into the images loop and selects the one based on the game status
    screen.blit(images[game_status], (150, 100))

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            running = False
    # updates the display
    pygame.display.update()

pygame.quit()