import random
import math

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']*4
# deck = ['Ace', 9]*10
player_pot = 100.0
bet_placed = 0.0

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
        if card in ["Jack", "Queen", "King"]:
            total += 10
        elif card != "Ace":
            total += card
        else:
            total += 11
    aces = hand.count('Ace')
    for ace in range(aces):
        if total > 21:
            # an ace can be 11 or 1 so if the total is greater than 21 it should be a 1
            total -= 10
    return total


def outcomes(dhand, phand):
    # pint("---Dealer shows " + str(dhand))
    # print("you have" + str(phand))r
    pass


def score(dhand, phand):
    global player_pot, bet_placed
    """Ends the hand, tells the outcome and sets up replay"""
    if total(dhand) == 21 and total(phand) == 21:
        outcomes(dhand, phand)
        print("Both you and the dealer have 21. You push.")
    if total(phand) == 21:
        outcomes(dhand, phand)
        print("21! You Win")
        player_pot += bet_placed
    elif total(phand) > 21:
        outcomes(dhand, phand)
        print("You Busted. You Lose")
        player_pot -= bet_placed
    elif total(dhand) > 21:
        outcomes(dhand, phand)
        print("The Dealer Busted. You Win")
        player_pot += bet_placed
    elif total(phand) < total(dhand):
        outcomes(dhand, phand)
        print("The Dealer has a higher number. You Lose")
        player_pot -= bet_placed
    elif total(dhand) < total(phand):
        outcomes(dhand, phand)
        print("You have a higher number than the Dealer. You Win")
        player_pot += bet_placed
    elif total(dhand) == total(phand):
        outcomes(dhand, phand)
        print("You have pushed with the dealer")
    replay()


def blackjack(dhand, phand):
    """Checks for Blackjack between player and dealer"""
    global player_pot
    if total(phand) == 21:
        outcomes(dhand, phand)
        print("BlackJack You Win!")
        player_pot += bet_placed * 1.5
        replay()
    elif total(dhand) == 21:
        outcomes(dhand, phand)
        print("Dealer has BlackJack. You Lose.")
        player_pot -= bet_placed
        replay()

def replay():
    global player_pot, deck
    if player_pot <= 0:
        print('You are out of money. Goodbye')
        exit()
    another = input("Do you want to play again? (Yes/No) : ").lower()
    if another == "yes":
        if len(deck) < 20:
            deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
            print("The Deck has been shuffled")
        game()
    else:
        print("Game Over")
        exit()

def options(dhand, phand):
    """Runs player through options of game"""
    global bet_placed, player_pot, deck
    loop = 1
    while total(phand) <= 21:
        if phand[0] == phand[1] and loop == 1:
            choice = input("Do you want to [Hit], [Stay], [Double] or [Split]").lower()
        elif loop == 1:
            choice = input("Do you want to [Hit], [Stay] or [Double]").lower()
        else:
            choice = input("Do you want to [Hit] or [Stay]").lower()
        if choice == "hit":
            # if they hit, it removes a card and adds it to the hand
            card = deck.pop()
            phand.append(card)
            print("you now have" + str(phand) + " for a total of " + str(total(phand)))
            if total(phand) > 21:
                score(dhand, phand)
        elif choice == 'double' and loop == 1:
            double_bet = bet_placed
            if player_pot < bet_placed*2:
                double_bet = player_pot - bet_placed
                print('You have less than the amount you need to double. The remainder of your pot, {}, will be added '
                      'to your bet.'.format(player_pot-bet_placed))
            bet_placed += double_bet
            card = deck.pop()
            phand.append(card)
            print("you now have" + str(phand) + " for a total of " + str(total(phand)))
            if total(phand) > 21:
                score(dhand, phand)
            else:
                dealer(dhand, phand)
            break
        elif choice == 'split' and loop == 1:
            card1 = deck.pop()
            card2 = deck.pop()
            phand1 = [phand[0], card1]
            phand2 = [phand[1], card2]
            print('Your first hand is {}'.format(phand1))
            options(dhand, phand1)
            options(dhand, phand2)
        else:
            dealer(dhand, phand)
        loop += 1


def dealer(dhand, phand):
    print("---Dealer shows " + str(dhand) + 'for a total of ' + str(total(dhand)))
    while total(dhand) < 17:
        print("---Dealer hits")
        card = deck.pop()
        dhand.append(card)
        print("---Dealer now has " + str(dhand) + 'for a total of ' + str(total(dhand)))
    score(dhand, phand)


def bet():
    """Tells the player the pot and asks how much they want to bet."""
    global bet_placed
    bet_placed = (input('Your pot is {}. How much would you like to bet on this hand?'.format(player_pot)))
    while (not bet_placed.isdigit()) or float(bet_placed) > player_pot:
        bet_placed = (input('Please select a number for your bet that is within your pot.'))
    return float(bet_placed)


def game():
    global bet_placed
    bet_placed = bet()
    dhand = deal(deck)
    phand = deal(deck)
    # dhand = [5, 'Queen'] You can use this to make specific games where we've seen bugs
    # phand = [3, 6, 2]
    print("The dealer is showing a " + str(dhand[0]))
    print("You have a " + str(phand) + " for a total of " + str(total(phand)))
    blackjack(dhand, phand)
    options(dhand, phand)


def program():
    print("WELCOME TO BLACKJACK!")
    game()

if __name__ == "__main__":
    program()
