# Hangman game using python

# import libraries
import pygame
import random


# game settings
FPS = 30
HEIGHT = 600
WIDTH = 800

# colors
BLACK = (0,0,0)
WHITE = (255,255,255)

# create list of words
sports = ['soccer', 'basketball']

animals = ['zebra', 'dog']

people = ['Michael Jordan']

# initiate pygame and create a window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Game loop
running = True
while running:
    screen.fill(WHITE)

