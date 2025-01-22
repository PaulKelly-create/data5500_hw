'''
This is an example of how to create a DeckOfCards object, shuffle it, and deal cards to play a game
'''

from DeckOfCards import *

#loop for game to keep going
game = 1
while game == 1: 
    print("Welcome to Black Jack!\n")
    deck = DeckOfCards()
    print("Deck before shuffled: ")
    deck.print_deck()
    deck.shuffle_deck()
    print("\nDeck after shuffled: ")
    deck.print_deck()


    # deal two cards to the user
    card = deck.get_card()
    print("\nCard number 1 is: ", card)
    card2 = deck.get_card()
    print("Card number 2 is: ", card2)

    score = 0
    # calculate the user's hand score
    score += card.val
    score += card2.val
    print("Your score is: ", score)




    # ask user if they would like a "hit" (another card)
    hit = input("Would you like a hit?(y/n) ")
    if hit == "y":
        y = 1
    else:
        y = 2
        
    number = 2
    while y == 1:
        number += 1
        card3 = deck.get_card()
        print("Card number ", number, "is :", card3)
        score += card3.val
        print("new score: ", score)
        if score > 21:
            another = input("Oops, you busted! Game over!\nAnother game?(y/n)")
            if another == "n":
                print ("Thanks for playing, better luck next time!")
                game = 2
                y = 3
            else:
                y = 3
        else:
            hit = input("would you like a hit?(y/n) ")
            if hit == "y":
                y = 1
            else:
                y = 2

    while y == 2:
        dcard = deck.get_card()
        print("Dealer card number 1 is: ", dcard)
        dcard2 = deck.get_card()
        print("Dealer card number 2 is: ", dcard2)

        dscore = 0
        # calculate the dealers hand score
        dscore += dcard.val
        dscore += dcard2.val
        print("Dealer score is: ", dscore)

        #Make a loop for the dealer
        dnumber = 2
        while dscore < score:
            dnumber += 1
            dcard3 = deck.get_card()
            print("Card number ", dnumber, "is :", dcard3)
            dscore += dcard3.val
            print("Dealer new score: ", dscore)
            if dscore > 21:
                again = input("You won, congrats!!\nWant to play again?(y/n) ")
                if again == "n":
                    y = 3
                    game = 2
                else:
                    y = 3
                    game = 1
            elif dscore <= 21 and dscore > score:
                again = input("Dealer score is higher, you lose!!\nWant to play again?(y/n) ")
                if again == "n":
                    y = 3
                    game = 2
                else:
                    y = 3
                    game = 1
            else:
                pass


    
    
