# Hangman game using python


# source for images - https://www.youtube.com/watch?v=UEO1B_llDnc&ab_channel=TechWithTim 

# import libraries
import pygame
import random


# game settings
FPS = 30
HEIGHT = 600
WIDTH = 800


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

# make clock
clock = pygame.time.Clock()

# make font
font = pygame.font.SysFont("Arial", 20)

word = "word"
characters = []
underScores = []
charactersRect = []
x = 0
for c in word:
    font = pygame.font.SysFont("Arial", 50)
    text = font.render(c, 1, (BLACK))
    tileSize = font.size(c)[0]
    underScores.append(pygame.Rect(200 + 40 * x, 380, tileSize, 3))
    characters.append(text)
    charactersRect.append(((200 + 40 * x), 330))
    x += 1

show = [True] * 26
# create class for buttons with letters
class Button:
    def __init__(self, idx, text, pos, font, background = "white", feedback=""):
        self.char = text
        self.idx = idx
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        self.change_text(text, background)
        self.feedback = feedback
 
    def change_text(self, text, background= "white"):
        self.text = self.font.render(text, 1, (BLACK))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(background)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
 

    def show(self, button):
        screen.blit(button.surface, (self.x, self.y))
 
    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, background="WHITE")
                    found = False
                    for i in range(len(word)):
                        if (word[i] == self.char):
                            found = True
                            showWord[i] = True
                    if (not found):
                        global game_status
                        game_status += 1
                    show[self.idx] = False
                    
                    

showWord = [False] * len(word)
buttons = []

curX = 100
for i in range(0, 13):
    buttons.append(Button(i, chr(65 + i), (curX, 400), font = 50))
    curX = 100 + 45 * (i + 1)
curX = 100
for i in range (13, 26):
    buttons.append(Button(i, chr(65 + i), (curX, 500), font = 50))
    curX = 100 + 45 * (i - 12)



running = True
# Game loop
while running:
    clock.tick(FPS)

    screen.fill(WHITE)


    # blit function goes into the images loop and selects the one based on the game status
    screen.blit(images[game_status], (150, 100))
    for item in underScores:
        pygame.draw.rect(screen, BLACK, item)
    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            running = False
            # draw buttons
        for button in buttons:
            if (show[button.idx]):
                button.click(event)
    for button in buttons:
        if (show[button.idx]):
            button.show(button)

    for i in range (len(characters)):
        if (showWord[i]):
            screen.blit(characters[i], (charactersRect[i]))
    check = True
    for i in showWord:
        check = check and i
    if (check):
        print("YOU WIN")
        pygame.quit()
        quit()
    # updates the display
    pygame.display.update()

pygame.quit()