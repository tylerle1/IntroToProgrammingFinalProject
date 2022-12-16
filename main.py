# Tyler Le

# Hangman game

# source for images - https://www.youtube.com/watch?v=UEO1B_llDnc&ab_channel=TechWithTim 
# source for buttons - https://pythonprogramming.altervista.org/buttons-in-pygame/?doing_wp_cron=1671168230.8327438831329345703125 

# import libraries
import pygame
import random
from random import randint

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
for i in range(6):
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
def draw_text(screen, text, size, color, x, y):
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

# word lists
Athletes = ["LEBRONJAMES", "RONALDO", "MESSI", "MICHAELJORDAN", "TIGERWOODS", "BABERUTH", "MUHAMMEDALI", "USAINBOLT"]
Artists = ["DRAKE", "BEYONCE", "TAYLORSWIFT", "MICHAELJACKSON", "JUSTINBIEBER", "ADELE", "BRUNOMARS", ""]
Fruits = ["BANANA", "APPLE", "GRAPE", "STRAWBERRY", "BLUEBERRY", "ORANGE", "AVOCADO", "LEMON", "WATERMELON", "PEACH"]
Animals = ["ZEBRA", "SNAKE", "KANGAROO", "GORILLA", "ELEPHANT", "PANDA", "DOLPHIN", "LEOPARD", "CHEETAH", "MONKEY"]
Countries = ["AMERICA", "MEXICO", "CANADA", "ITALY", "ENGLAND", "FRANCE", "GERMANY", "PHILIPPINES", "JAPAN", "EGYPT", "BRAZIL", "UKRAINE", "AUSTRALIA"]
Cities = ["SANJOSE", "SEATTLE", "NEWYORK", "SANFRANCISCO", "LASVEGAS", "PARIS", "DUBAI", "AMSTERDAM", "ROME", "SYDNEY", "JERUSALEM"]
categorys = ["athletes", "artists", "fruits", "animals", "countries", "cities"]

word = ''
category = categorys[randint(0, len (categorys) - 1)]
if category == "animals":
    word = Animals[randint(0, len (Animals) - 1)]
if category == "artists":
    word = Artists[randint(0, len (Artists) - 1)]
if category == "fruits":
    word = Fruits[randint(0, len (Fruits) - 1)]
if category == "animals":
    word = Animals[randint(0, len (Animals) - 1)]
if category == "countries":
    word = Countries[randint(0, len (Countries) - 1)]
if category == "cities":
    word = Cities[randint(0, len (Cities) - 1)]



# making these variables into lists
characters = []
underScores = []
charactersRect = []
x = 0

# for loop for drawing the lines under the letters and the letters
for c in word:
    # making the text
    font = pygame.font.SysFont("Arial", 50)
    text = font.render(c, 1, (BLACK))
    tileSize = font.size(c)[0]

    # adding the underscores or lines by using pygames rectangle
    underScores.append(pygame.Rect(250 + 40 * x, 330, tileSize, 3))
    characters.append(text)
    # this is where the characters or letters are drawn
    charactersRect.append(((250 + 40 * x), 280))
    x += 1

show = [True] * 26

# create class for buttons with letters and make it clickable
class Button:
    def __init__(self, index, text, pos, font, background = WHITE, feedback=""):
        self.char = text
        self.index = index
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        self.change_text(text, background)
        self.feedback = feedback

    def change_text(self, text, background= WHITE):
        self.text = self.font.render(text, 1, (BLACK))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(background)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self, button):
        screen.blit(button.surface, (self.x, self.y))
 
    # function for clicking the button
    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, background="white")
                    # checking if what the user clicks is equal to the "word"
                    found = False
                    for i in range(len(word)):
                        if (word[i] == self.char):
                            found = True
                            showWord[i] = True
                    # if the user doesnt click correctly then it changes the image
                    if (not found):
                        global game_status
                        game_status += 1
                    show[self.index] = False
                    
showWord = [False] * len(word)
buttons = []

# create instance of buttons
# curX is the current x position
curX = 100
# for loop for the first thirteen letters on top row
for i in range(0, 13):
    buttons.append(Button(i, chr(65 + i), (curX, 400), font = 50))
    curX = 100 + 45 * (i + 1)
curX = 100
# the bottom row
for i in range (13, 26):
    buttons.append(Button(i, chr(65 + i), (curX, 500), font = 50))
    curX = 100 + 45 * (i - 12)

game_started = False
running = True
# Game loop
while running:
    clock.tick(FPS)

    screen.fill(WHITE)
    draw_text(screen, category, 50, BLACK, 390, 20)

    # draw images
    screen.blit(images[game_status], (100, 125))

    for item in underScores:
        pygame.draw.rect(screen, BLACK, item)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            # draw buttons
        for button in buttons:
            if (show[button.index]):
                button.click(event)
    for button in buttons:
        if (show[button.index]):
            button.show(button)

    # draw letters
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
        # screen.fill(BLACK)
        # draw_text(screen, "CLICK SPACE TO PLAY AGAIN", 50, WHITE, 400, 300)
        # for event in pygame.event.get():
        # # check for closed window
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_SPACE:
                    #print("idk how to work u")
                    

        
    # updates the display
    pygame.display.update()

pygame.quit()