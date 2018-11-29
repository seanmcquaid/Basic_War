# miniconda access to run pygame
# cd ~/miniconda3/bin
# source activate py3k
# cd /Users/seanmcquaid/development/Projects/war

import pygame
from random import randint
from Text import Text

pygame.init()

screen_size = (600, 600)
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("War! The Card Game")
background_color = (0, 102, 0)


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
    new_card = True
    while game_on:       
        pygame_screen.fill(background_color)
        if (game_start == False):
            pygame_screen.blit(card_back(),[25, 200])
            pygame_screen.blit(card_back(),[400, 200])
            card1 = player_card_image() 
            card2 = comp_card_image()
            round_winner = ""
            winner = ""
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
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    game_on = False
                elif (event.type == pygame.KEYDOWN):
                    if (event.key == 32):
                        if len(cards) == 0:
                            if text.player_points > text.comp_points:
                                winner = "YOU WIN THE GAME! Press enter to close!"
                            elif text.player_points < text.comp_points:
                                winner = "YOU LOST TO THE COMP! Press enter to close!"
                            else:
                                winner = "YOU ACTUALLY TIED?! Press enter to close!"
                        else:
                            new_card = True
                    elif (len(cards) == 0 and event.key == 13):
                        game_on = False
                        
            if new_card:
                card1 = player_card_image() 
                card_val_suit1 = cards[card1[1]]
                card_val1 = card_val_suit1[:-1]
                cards.remove(card_val_suit1)
                card2 = comp_card_image()
                card_val_suit2 = cards[card2[1]]
                card_val2 = card_val_suit2[:-1] 
                cards.remove(card_val_suit2)            
                if (int(card_val1) > int(card_val2)):
                    text.player_point_inc()
                    round_winner = "You"
                elif (int(card_val1) < int(card_val2)):
                    text.comp_point_inc()
                    round_winner = "Comp"
                else:
                    round_winner = "Neither"
                new_card = False 

            text.player_point_counter()
            text.comp_point_counter()
            text.deck_counter(len(cards))
            text.draw_counters()
            text.winner_of_round(round_winner)
            text.draw_round_winner_player()
            text.winner_of_game(winner)
            text.draw_game_winner_player()
            pygame_screen.blit(card1[0],[25, 200])
            pygame_screen.blit(card2[0],[400, 200])    
                    
        pygame.display.flip()

main_game()