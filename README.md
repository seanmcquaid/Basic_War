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
* Displays facedown cards at the start of the game and will populate a set of cards for each player once the spacebar is pressed. 
* Point counter to keep track of both player and computer points.
* Deck counter to keep track of both player and computer points.

## Technologies
* Python
* Pygame

## Challenges and Solutions
* Creating a new card for each round
    * While creating the initial versions of the game, I struggled to come up with an appropriate way

* Creating an array to store the deck of cards
    * As I was looking to actually populate the card images, I quickly realized that creating an array manually with the different image file names was inefficient. I decided to rename all the files to corresponding number values and suit letters from the game. Then I created a for loop in order to append the corresponding numbers and letters into an empty array for the cards. 

    ```
    cards = []
    suits = ['h','s','d','c']
    for s in suits:
        for c in range(1,14):
            cards.append(str(c)+s)
    ```
* 
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
* Game Logic

## MVP
* Create a basic version of the game "War" utilizing Python as the programming language and Pygame to display content.

## Stretch Goals
* Create deck counter and point counter system
    * Status: Completed
* Implement Full "War" Functionality for a tie
    * Status: Incomplete

## Screenshots
* Main Game

![Game Screen](./readme/end_screen.jpg)
