import random
import math

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']*4
pot = 100
bet = 0

# def num_decks():
#     print("How many decks do you want to play with?")
#     decks = input()


def deal(deck):
    """Deals two cards and removes them from the deck"""
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        hand.append(card)
    return hand


def total(hand):
    """Sums up the total for the hand submitted"""
    total = 0
    for card in hand:
        if card is "Jack" or card is "Queen" or card is "King":
            total += 10
        elif card != "Ace":
            total += card
        else:
            total += 11
    if total > 21 and hand.count('Ace') > 0:
        # an ace can be 11 or 1 so if the total is greater than 21 it should be a 1
        total -= 10
        if total > 21 and hand.count('Ace') > 1:
            total -= 10
            if total > 21 and hand.count('Ace') > 2:
                total -= 10
                if total > 21 and hand.count('Ace') > 3:
                    total -= 10
                    if total > 21 and hand.count('Ace') > 4:
                        total -= 10
    return total


def outcomes(dhand, phand):
    # pint("---Dealer shows " + str(dhand))
    # print("you have" + str(phand))r
    pass


def score(dhand, phand):
    """Ends the hand, tells the outcome and sets up replay"""
    if total(dhand) == 21 and total(phand) == 21:
        outcomes(dhand, phand)
        print("Both you and the dealer have 21. You push.")
    if total(phand) == 21:
        outcomes(dhand, phand)
        print("21! You Win")
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
    """Checks for Blackjack between player and dealer"""
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
    """Runs player through options of game"""
    while total(phand) < 21:
        choice = input("Do you want to [Hit], or [Stay]").lower()
        if choice == "hit":
            # if they hit, it removes a card and adds it to the hand
            card = deck.pop()
            phand.append(card)
            print("you now have" + str(phand) + " for a total of " + str(total(phand)))
            if total(phand) >= 21:
                score(dhand, phand)
        else:
            dealer(dhand, phand)


def dealer(dhand, phand):
    print("---Dealer shows " + str(dhand) + 'for a total of ' + str(total(dhand)))
    while total(dhand) < 17:
        print("---Dealer hits")
        card = deck.pop()
        dhand.append(card)
        print("---Dealer now has " + str(dhand) + 'for a total of ' + str(total(dhand)))
    score(dhand, phand)


def bet():
    """Tells the player the pot and asks how much they want to bet. Need to work on verifying inputs"""
    bet = (input('Your pot is {}. How much would you like to bet on this hand?'.format(pot)))
    print(type(bet))
    while type(int(bet))!= int:
        bet = (input('Please select a number for your bet'))
    while bet > pot:
        bet = (input('Please select an amount less than your pot'))
    bet = int(bet)

    
def game():
    choice = 0
    print("WELCOME TO BLACKJACK!")
    bet()
    dhand = deal(deck)
    phand = deal(deck)
    print("The dealer is showing a " + str(dhand[0]))
    print("You have a " + str(phand) + " for a total of " + str(total(phand)))
    blackjack(dhand, phand)
    options(dhand, phand)


if __name__ == "__main__":
    game()
