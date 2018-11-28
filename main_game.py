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

screen_size = (600, 600)
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("War! The Card Game")
background_color = (0, 102, 0)


player = User()
text = Text(pygame_screen)

cards = []
suits = ['h','s','d','c']
for s in suits:
    for c in range(1,14):
        cards.append(str(c)+s)

def player_card_image():
    rand_card1 = randint(0,len(cards)-1)
    card_image1 = pygame.image.load('cards/' + cards[rand_card1] + '.png')
    return [card_image1,rand_card1]
def comp_card_image():
    rand_card2 = randint(0,len(cards)-1)
    card_image2 = pygame.image.load('cards/' + cards[rand_card2] + '.png') 
    return [card_image2,rand_card2]
def card_back():
    start_card = pygame.image.load('cards/deck.png') 
    return start_card

def main_game():
    game_on = True
    game_start = False
    while game_on:       
        pygame_screen.fill(background_color)
        if (game_start == False):
            pygame_screen.blit(card_back(),[25, 200])
            pygame_screen.blit(card_back(),[400, 200])
            card1 = player_card_image() 
            card2 = comp_card_image()
            card_val1 = cards[card1[1]]
            card_val2 = cards[card2[1]]
            text.instructions()
            text.draw_instructions()
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
            pygame_screen.blit(card1[0],[25, 200])
            pygame_screen.blit(card2[0],[400, 200])
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    game_on = False
                elif (event.type == pygame.KEYDOWN):
                    if (event.key == 32):
                        card1 = player_card_image() 
                        card2 = comp_card_image()
                        card_val_suit1 = cards[card1[1]]
                        card_val_suit2 = cards[card2[1]]
                        card_val1 = card_val_suit1[:-1]
                        card_val2 = card_val_suit2[:-1]
                        print (cards)
                        print (len(cards))
                        if len(cards) >=2:
                            cards.remove(card_val_suit1)
                            cards.remove(card_val_suit2)
                        if (int(card_val1) > int(card_val2)):
                            print ("Player: "+str(card_val1))
                            print ("Computer: "+str(card_val2))
                            print ("Player wins")
                        elif (int(card_val1) < int(card_val2)):
                            print ("Player: "+str(card_val1))
                            print ("Computer: "+str(card_val2))
                            print ("Computer wins")
                        else:
                            print ("Player: "+str(card_val1))
                            print ("Computer: "+str(card_val2))
                            print ("you tied")
                            
                    
        pygame.display.flip()

main_game()