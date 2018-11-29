import os
import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

# def num_decks():
#     print("How many decks do you want to play with?")
#     decks = input()


def deal(deck):
    hand = []
    for i in range(2):
	    random.shuffle(deck)
	    card = deck.pop()
	    if card == 11:card = "Jack"
	    if card == 12:card = "Queen"
	    if card == 13:card = "King"
	    if card == 14:card = "Ace"
	    hand.append(card)
    return hand

def total(hand):
    total = 0
    for card in hand:
        if card is "Jack" or card is "Queen" or card is "King":
            total += 10
        elif card is "Ace":
            if total >= 11:
                total += 1
            else:
                total += 11
        else:
            total += card
    return total


def outcomes(dhand, phand):
    print("dealer has" + str(dhand))
    print("you have" + str(phand))

def score(dhand, phand):
    if total(phand) == 21:
        outcomes(dhand, phand)
        print("BlackJack! You Win")
    elif total(dhand) == 21:
        outcomes(dhand, phand)
        print("Dealer has a BlackJack")
    elif total(phand) > 21:
        outcomes(dhand, phand)
        print("You Busted. You Lose")
    elif total(dhand) > 21:
        outcomes(dhand, phand)
        print("The Dealer Busted. You Win")
    elif total(phand) < total(dhand):
        outcomes(dhand, phand)
        print("The Dealer has a higher number. You Lose")
    elif total(dhand) < total(phand):
        outcomes(dhand, phand)
        print("You have a higher number than the Dealer. You Win")
    elif total(dhand) == total(phand):
        outcomes(dhand, phand)
        print("You have pushed with the dealer")
    replay()


def blackjack(dhand, phand):
    if total(phand) == 21:
        outcomes(dhand, phand)
        print("BlackJack You Win!")
        replay()
    elif total(dhand) == 21:
        outcomes(dhand, phand)
        print("Dealer has BlackJack. You Lose.")
        replay()

def replay():
    another = input("Do you want to play again? (Yes/No) : ").lower()
    if another == "yes":
        dhand = []
        phand = []
        # if len(deck) < 20:
        #     deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
        #     print("The Deck has been shuffled")
        game()
    else:
        print("Game Over")
        exit()

def options(dhand, phand):
    while total(phand) < 21:
        choice = input("Do you want to [Hit], or [Stay]").lower()
        if choice == "hit":
            card = deck.pop()
            if card == 11:card = "Jack"
            if card == 12:card = "Queen"
            if card == 13:card = "King"
            if card == 14:card = "Ace"
            phand.append(card)
            print("you now have" + str(phand) + " for a total of " + str(total(phand)))
            if total(phand) >= 21:
                score(dhand, phand)
        else:
            dealer(dhand, phand)

def dealer(dhand, phand):
    while total(dhand) < 17:
        print("dealer hits")
        card = deck.pop()
        if card == 11:card = "Jack"
        if card == 12:card = "Queen"
        if card == 13:card = "King"
        if card == 14:card = "Ace"
        dhand.append(card)
        print("dealer now has" + str(dhand))
    score(dhand, phand)




def game():
	choice = 0
	print("WELCOME TO BLACKJACK!")
	dhand = deal(deck)
	phand = deal(deck)
	print("The dealer is showing a " + str(dhand[0]))
	print("You have a " + str(phand) + " for a total of " + str(total(phand)))
	blackjack(dhand, phand)
	options(dhand, phand)

if __name__ == "__main__":
   game()
