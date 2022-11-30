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






# load hangman images
# make an images list
images = []
# create a loop that runs 7 times for each image
for i in range(7):
    # each time the loop runs it adds a string so we can load every image
    image = pygame.image.load("C:\Github\IntrotoProgramming2022\IntroToProgrammingFinalProject\IntroToProgrammingFinalProject\images")
    # "append" adds it
    images.append(image)

# game variables
game_status = 0

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
    # blit function goes into the images loop and selects the one based on the game status
    screen.blit(images[game_status], (150, 100))
    # updates the display
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # checks the position of the mouse
            pos = pygame.mouse.get_pos()
            print (pos)

pygame.quit()