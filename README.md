# War
![Start Sreen](./readme/start_screen.jpg)

## Contents
    * Description
    * Features
    * Technologies
    * Challenges and Solutions
    * MVP
    * Stretch Goals
    * Screenshots

## Description
This project is built using Python and Pygame. meant to be a basic recreation of the popular card game, "War." 

### Features
* 

## Technologies
* Python
* Pygame

## Challenges and Solutions
* Creating a new card for each round
    * 
    ```
    if new_card:
        card1 = player_card_image() 
        card_val_suit1 = cards[card1[1]]
        card_val1 = card_val_suit1[:-1]
        cards.remove(card_val_suit1)
        card2 = comp_card_image()
        card_val_suit2 = cards[card2[1]]
        card_val2 = card_val_suit2[:-1] 
        cards.remove(card_val_suit2)   
    ```
* Creating an array to store the deck of cards
    *
    ```
    cards = []
    suits = ['h','s','d','c']
    for s in suits:
        for c in range(1,14):
            cards.append(str(c)+s)

    ```
* Game Logic

## MVP
* 

## Stretch Goals
* Create point counter system
* Implement Full "War" Functionality for a tie

## Screenshots
* Main Game

![Game Screen](./readme/end_screen.jpg)
