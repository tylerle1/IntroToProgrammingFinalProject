# Hangman game using python

# sources
# 
# source for images - https://www.youtube.com/watch?v=UEO1B_llDnc&ab_channel=TechWithTim 

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

# make clock
clock = pygame.time.Clock()

# make font
font = pygame.font.SysFont("Arial", 20)


# create class for buttons with letters
class Button:
    def __init__(self, text, pos, font, background = "black", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.change_text(text, background)
 
    def change_text(self, text, background= "black"):
        self.text = self.font.render(text, 1, (WHITE))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(background)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
 
    def show(self):
        screen.blit(button1.surface, (self.x, self.y))
        # screen.blit(button2.surface, (self.x, self.y))
        # screen.blit(button3.surface, (self.x, self.y))
        # screen.blit(button4.surface, (self.x, self.y))
        # screen.blit(button5.surface, (self.x, self.y))
        # screen.blit(button6.surface, (self.x, self.y))
        # screen.blit(button7.surface, (self.x, self.y))
        # screen.blit(button8.surface, (self.x, self.y))
        # screen.blit(button9.surface, (self.x, self.y))
        # screen.blit(button10.surface, (self.x, self.y))
        # screen.blit(button11.surface, (self.x, self.y))
        # screen.blit(button12.surface, (self.x, self.y))
        # screen.blit(button13.surface, (self.x, self.y))
        # screen.blit(button14.surface, (self.x, self.y))
        # screen.blit(button15.surface, (self.x, self.y))
        # screen.blit(button16.surface, (self.x, self.y))
        # screen.blit(button17.surface, (self.x, self.y))
        # screen.blit(button18.surface, (self.x, self.y))
        # screen.blit(button19.surface, (self.x, self.y))
        # screen.blit(button20.surface, (self.x, self.y))
        # screen.blit(button21.surface, (self.x, self.y))
        # screen.blit(button22.surface, (self.x, self.y))
        # screen.blit(button23.surface, (self.x, self.y))
        # screen.blit(button24.surface, (self.x, self.y))
        # screen.blit(button25.surface, (self.x, self.y))
        # screen.blit(button26.surface, (self.x, self.y))
 
    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, background="WHITE")
 
 # instance of Button class
button1 = Button("A",  (100, 400), font=50, background="black", feedback=" ")
# button2 = Button("B",  (145, 400), font=50, background="black", feedback=" ")
# button3 = Button("C",  (190, 400), font=50, background="black", feedback=" ")
# button4 = Button("D",  (235, 400), font=50, background="black", feedback=" ")
# button5 = Button("E",  (280, 400), font=50, background="black", feedback=" ")
# button6 = Button("F",  (325, 400), font=50, background="black", feedback=" ")
# button7 = Button("G",  (370, 400), font=50, background="black", feedback=" ")
# button8 = Button("H",  (405, 400), font=50, background="black", feedback=" ")
# button9 = Button("I",  (450, 400), font=50, background="black", feedback=" ")
# button10 = Button("J",  (495, 400), font=50, background="black", feedback=" ")
# button11 = Button("K",  (540, 400), font=50, background="black", feedback=" ")
# button12 = Button("L",  (585, 400), font=50, background="black", feedback=" ")
# button13 = Button("M",  (630, 400), font=50, background="black", feedback=" ")
# button14 = Button("N",  (100, 500), font=50, background="black", feedback=" ")
# button15 = Button("O",  (145, 500), font=50, background="black", feedback=" ")
# button16 = Button("P",  (190, 500), font=50, background="black", feedback=" ")
# button17 = Button("Q",  (235, 500), font=50, background="black", feedback=" ")
# button18 = Button("R",  (280, 500), font=50, background="black", feedback=" ")
# button19 = Button("S",  (325, 500), font=50, background="black", feedback=" ")
# button20 = Button("T",  (370, 500), font=50, background="black", feedback=" ")
# button21 = Button("U",  (405, 500), font=50, background="black", feedback=" ")
# button22 = Button("V",  (450, 500), font=50, background="black", feedback=" ")
# button23 = Button("W",  (495, 500), font=50, background="black", feedback=" ")
# button24 = Button("X",  (540, 500), font=50, background="black", feedback=" ")
# button25 = Button("Y",  (585, 500), font=50, background="black", feedback=" ")
# button26 = Button("Z",  (630, 500), font=50, background="black", feedback=" ")

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
        button1.click(event)
    button1.show()
    if event.type == pygame.QUIT:
        button2.click(event)
    button1.show

    # updates the display
    pygame.display.update()

pygame.quit()