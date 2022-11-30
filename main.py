# Hangman game using python

# import libraries
import pygame
import random


# game settings
FPS = 30
HEIGHT = 600
WIDTH = 800
# font = pygame.font.SysFont('Arial', 35)


# colors
BLACK = (0,0,0)
WHITE = (255,255,255)





# load images

# load hangman images
pygame.image.load("hangman0.png")
pygame.image.load("hangman1.png")
pygame.image.load("hangman2.png")
pygame.image.load("hangman3.png")
pygame.image.load("hangman4.png")
pygame.image.load("hangman5.png")
pygame.image.load("hangman6.png")


# initiate pygame and create a window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


# create class for buttons with letters
class Buttons():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


# make clock
clock = pygame.time.Clock()

running = True

# Game loop
while running:
    clock.tick(FPS)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # checks the position of the mouse
            pos = pygame.mouse.get_pos()
            print (pos)

pygame.quit()