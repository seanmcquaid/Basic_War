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
* Displays facedown cards at the start of the game and will populate a set of cards for each player every time the spacebar is pressed
* Point counter to keep track of both player and computer points
* Deck counter to keep track of how many cards are left in the deck
* End screen that populates when the length of the cards is equal to zero

## Technologies
* Python
* Pygame

## Challenges and Solutions
* Populating a new card for each round for each player
    * While creating the initial versions of the game, I struggled to come up with an appropriate way to group my code so I can generate new cards and distribute points at the same time. I found that basing my logic on the new card being generated yielded the results I was looking to get.

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
    if (int(card_val1) > int(card_val2)):
        text.player_point_inc()
        round_winner = "You"
    elif (int(card_val1) < int(card_val2)):
        text.comp_point_inc()
        round_winner = "Comp"
    else:
        round_winner = "Neither"
    new_card = False 
    ```

* Creating an array to store the deck of cards
    * As I was looking to actually populate the card images, I quickly realized that creating an array manually with the different image file names was inefficient. I decided to rename all the files to corresponding number values and suit letters from the game. Then I created a for loop in order to append the corresponding numbers and letters into an empty array for the cards. 

    ```
    cards = []
    suits = ['h','s','d','c']
    for s in suits:
        for c in range(1,14):
            cards.append(str(c)+s)
    ```

* Using resuable functions to draw the cards for both the player and computer
    * After completing my solution for storing a deck of cards, I needed a way to populate these images! I did so but concatenating a string for the image path using a random number from 0 to  the length of the cards array minus 1. 

    ```
     def player_card_image():
        rand_card1 = randint(0,len(cards)-1)
        card_image1 = pygame.image.load('cards/' + cards[rand_card1] + '.png')
        return [card_image1,rand_card1]

    def comp_card_image():
        rand_card2 = randint(0,len(cards)-1)
        card_image2 = pygame.image.load('cards/' + cards[rand_card2] + '.png') 
        return [card_image2,rand_card2]
    ```

## MVP
* Create a basic version of the game "War" utilizing Python as the programming language and Pygame to display content.
* Requirements
    * Must utilize elements of OOP
    * Start screen displays prior to actual main game 
    * Game logic must be in place to determine winner and loser
    * Option to close game after winner is determined


## Stretch Goals
* Create deck counter and point counter system
    * Status: Completed
* Implement Full "War" Functionality for a tie
    * Status: Incomplete

## Screenshots
* Main Game

![Game Screen](./readme/end_screen.jpg)
