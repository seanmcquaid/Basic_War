# miniconda access to run pygame
# cd ~/miniconda3/bin
# source activate py3k
# cd /Users/seanmcquaid/development/Projects/war
# python game.py

import pygame
from random import randint
from Text import Text
pygame.init()

screen_size = (600, 600)
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("War! The Card Game")

cards = []
suits = ['h','s','d','c']
for s in suits:
    for c in range(1,14):
        cards.append(str(c)+s)
print(cards)

rand_card = randint(0,53)
rand_card = randint(0,53)

def main_game():
    game_on = True

    while game_on == True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                game_on = False
        pygame_screen.fill((0,255,0))
        card_image = pygame.image.load('cards/' +cards[rand_card] + '.png')
        card_image2 = pygame.image.load('cards/' +cards[rand_card] + '.png')
        pygame_screen.blit(card_image,[0, 0])
        pygame_screen.blit(card_image2,[200,200])
        pygame.display.flip()

main_game()