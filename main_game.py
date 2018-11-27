# miniconda access to run pygame
# cd ~/miniconda3/bin
# source activate py3k
# cd /Users/seanmcquaid/development/Projects/war
# python game.py

import pygame
from random import randint
from User import User
from Text import Text
from Cards import Cards

pygame.init()

# ====== SCREEN SETTING =======
screen_size = (600, 600)
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("War! The Card Game")
background_color = (0, 102, 0)

# ==== OBJECTS ====

player = User()
text = Text(pygame_screen)

# ====== CREATING LOOP FOR DECK OF CARDS ======
cards = []
suits = ['h','s','d','c']
for s in suits:
    for c in range(1,14):
        cards.append(str(c)+s)
print(cards)

# ==== RANDOM NUMBERS FOR EACH CARD INDEX IN ARRAY =====
def random_number1():
    rand_card = randint(0,51)
    return rand_card
def random_number2():
    rand_card2 = randint(0,51)
    return rand_card2


# ==== IMAGES ======

start_card = pygame.image.load('cards/deck.png')
card_image = pygame.image.load('cards/' +cards[random_number1()] + '.png')
card_image2 = pygame.image.load('cards/' +cards[random_number2()] + '.png') 

def main_game():
    game_on = True
    game_start = False
    while game_on:       
        pygame_screen.fill(background_color)
        card1 = pygame.image.load('cards/' +cards[random_number1()] + '.png') 
        card2 = pygame.image.load('cards/' +cards[random_number2()] + '.png')
        if (game_start == False):
            pygame_screen.blit(start_card,[25, 200])
            pygame_screen.blit(start_card,[400, 200])
            text.title()
            text.draw_text()
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    game_on = False
                elif (event.type == pygame.KEYDOWN):
                    if (event.key == 32):
                        game_start = True
        for event in pygame.event.get():
            pygame_screen.blit(card1,[25, 200])
            pygame_screen.blit(card2,[400, 200])
            if (event.type == pygame.QUIT):
                game_on = False
            elif (event.type == pygame.KEYDOWN):
                if (event.key == 32):
                    pygame_screen.blit(card1,[25, 200])
                    pygame_screen.blit(card2,[400, 200])
                    text.player_point_counter()
                    text.draw_text()
                    text.comp_point_counter()
                    text.draw_text()
                    if (random_number1() > random_number2()):
                        print (str(random_number1()))
                        print (str(random_number2()))
                        print ("YOU WIN THIS ROUND!")
                        # point counter and update text
                    else:
                        print (str(random_number1()))
                        print (str(random_number2()))
                        print ("COMPUTER WINS THIS ROUND!")
        # pygame_screen.blit(card1,[25, 200])
        # pygame_screen.blit(card2,[400, 200])
        
        pygame.display.flip()


main_game()