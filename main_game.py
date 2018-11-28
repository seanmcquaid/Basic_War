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

# ==== RANDOM NUMBERS FOR EACH CARD INDEX IN ARRAY =====
rand_card1 = randint(0,51)
rand_card2 = randint(0,51)
def card_image1():
    card_image1 = pygame.image.load('cards/' + cards[rand_card1] + '.png')
    return card_image1
def card_image2():
    card_image2 = pygame.image.load('cards/' + cards[rand_card2] + '.png') 
    return card_image2

# ==== IMAGES ======

start_card = pygame.image.load('cards/deck.png') 

def main_game():
    game_on = True
    game_start = False
    while game_on:       
        pygame_screen.fill(background_color)
        card1 = card_image1() 
        card2 = card_image2()
        if (game_start == False):
            pygame_screen.blit(start_card,[25, 200])
            pygame_screen.blit(start_card,[400, 200])
            text.title()
            text.draw_title_text()
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    game_on = False
                elif (event.type == pygame.KEYDOWN):
                    if (event.key == 32):
                        game_start = True
        else: 
            text.player_point_counter()
            text.comp_point_counter()
            text.deck_counter()
            text.draw_counters()
            pygame_screen.blit(card1,[25, 200])
            pygame_screen.blit(card2,[400, 200])
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    game_on = False
                # elif (event.type == pygame.KEYDOWN):
                    # if (event.key == 32):
                        #need to figure out how to UPDATE THIS BLIT
                    
        pygame.display.flip()

main_game()