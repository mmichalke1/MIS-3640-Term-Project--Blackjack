#!/usr/bin/python

#Import Library
import pygame
from pygame.locals import *
import random
import copy

#Load Images
icon = pygame.image.load('resources/icon.png')
cBack = pygame.image.load('resources/cards/cardback.png')
diamondA = pygame.image.load('resources/cards/ad.png')
clubA = pygame.image.load('resources/cards/ac.png')
heartA = pygame.image.load('resources/cards/ah.png')
spadeA = pygame.image.load('resources/cards/as.png')
diamond2 = pygame.image.load('resources/cards/2d.png')
club2 = pygame.image.load('resources/cards/2c.png')
heart2 = pygame.image.load('resources/cards/2h.png')
spade2 = pygame.image.load('resources/cards/2s.png')
diamond3 = pygame.image.load('resources/cards/3d.png')
club3 = pygame.image.load('resources/cards/3c.png')
heart3 = pygame.image.load('resources/cards/3h.png')
spade3 = pygame.image.load('resources/cards/3s.png')
diamond4 = pygame.image.load('resources/cards/4d.png')
club4 = pygame.image.load('resources/cards/4c.png')
heart4 = pygame.image.load('resources/cards/4h.png')
spade4 = pygame.image.load('resources/cards/4s.png')
diamond5 = pygame.image.load('resources/cards/5d.png')
club5 = pygame.image.load('resources/cards/5c.png')
heart5 = pygame.image.load('resources/cards/5h.png')
spade5 = pygame.image.load('resources/cards/5s.png')
diamond6 = pygame.image.load('resources/cards/6d.png')
club6 = pygame.image.load('resources/cards/6c.png')
heart6 = pygame.image.load('resources/cards/6h.png')
spade6 = pygame.image.load('resources/cards/6s.png')
diamond7 = pygame.image.load('resources/cards/7d.png')
club7 = pygame.image.load('resources/cards/7c.png')
heart7 = pygame.image.load('resources/cards/7h.png')
spade7 = pygame.image.load('resources/cards/7s.png')
diamond8 = pygame.image.load('resources/cards/8d.png')
club8 = pygame.image.load('resources/cards/8c.png')
heart8 = pygame.image.load('resources/cards/8h.png')
spade8 = pygame.image.load('resources/cards/8s.png')
diamond9 = pygame.image.load('resources/cards/9d.png')
club9 = pygame.image.load('resources/cards/9c.png')
heart9 = pygame.image.load('resources/cards/9h.png')
spade9 = pygame.image.load('resources/cards/9s.png')
diamond10 = pygame.image.load('resources/cards/10d.png')
club10 = pygame.image.load('resources/cards/10c.png')
heart10 = pygame.image.load('resources/cards/10h.png')
spade10 = pygame.image.load('resources/cards/10s.png')
diamondJ = pygame.image.load('resources/cards/jd.png')
clubJ = pygame.image.load('resources/cards/jc.png')
heartJ = pygame.image.load('resources/cards/jh.png')
spadeJ = pygame.image.load('resources/cards/js.png')
diamondQ = pygame.image.load('resources/cards/qd.png')
clubQ = pygame.image.load('resources/cards/qc.png')
heartQ = pygame.image.load('resources/cards/qh.png')
spadeQ = pygame.image.load('resources/cards/qs.png')
diamondK = pygame.image.load('resources/cards/kd.png')
clubK = pygame.image.load('resources/cards/kc.png')
heartK = pygame.image.load('resources/cards/kh.png')
spadeK = pygame.image.load('resources/cards/ks.png')

#Set Icon
pygame.display.set_icon(icon)

#Global Constants
black = (0,0,0)
white = (255,255,255)
gray = (192,192,192)

cards = [ diamondA, clubA, heartA, spadeA, \
          diamond2, club2, heart2, spade2, \
          diamond3, club3, heart3, spade3, \
          diamond4, club4, heart4, spade4, \
          diamond5, club5, heart5, spade5, \
          diamond6, club6, heart6, spade6, \
          diamond7, club7, heart7, spade7, \
          diamond8, club8, heart8, spade8, \
          diamond9, club9, heart9, spade9, \
          diamond10, club10, heart10, spade10, \
          diamondJ, clubJ, heartJ, spadeJ, \
          diamondQ, clubQ, heartQ, spadeQ, \
          diamondK, clubK, heartK, spadeK ]
cardA = [ diamondA, clubA, heartA, spadeA ]
card2 = [ diamond2, club2, heart2, spade2 ]
card3 = [ diamond3, club3, heart3, spade3 ]
card4 = [ diamond4, club4, heart4, spade4 ]
card5 = [ diamond5, club5, heart5, spade5 ]
card6 = [ diamond6, club6, heart6, spade6 ]
card7 = [ diamond7, club7, heart7, spade7 ]
card8 = [ diamond8, club8, heart8, spade8 ]
card9 = [ diamond9, club9, heart9, spade9 ]
card10 = [ diamond10, club10, heart10, spade10, \
            diamondJ, clubJ, heartJ, spadeJ, \
            diamondQ, clubQ, heartQ, spadeQ, \
            diamondK, clubK, heartK, spadeK ]

def getAmt(card):
    ''' Returns the amount the card is worth.
E.g. Ace is default 11. 10/Jack/Queen/King is 10.'''
    if card in cardA:
        return 11
    elif card in card2:
        return 2
    elif card in card3:
        return 3
    elif card in card4:
        return 4
    elif card in card5:
        return 5
    elif card in card6:
        return 6
    elif card in card7:
        return 7
    elif card in card8:
        return 8
    elif card in card9:
        return 9
    elif card in card10:
        return 10
    else:
        print('getAmt broke')
        exit()

def genCard(cList, xList):
    '''Generates an card from cList, removes it from cList, and appends it to xList.
Returns if card is Ace and the card itself.'''
    cA = 0
    card = random.choice(cList)
    cList.remove(card)
    xList.append(card)
    if card in cardA:
        cA = 1
    return card, cA

def initGame(cList, uList, dList):
    '''Generates two cards for dealer and user, one at a time for each.
        Returns if card is Ace and the total amount of the cards per person.'''
    userA = 0
    dealA = 0
    card1, cA = genCard(cList, uList)
    userA += cA
    card2, cA = genCard(cList, dList)
    dealA += cA
    card3, cA = genCard(cList, uList)
    userA += cA
    card4, cA = genCard(cList, dList)
    dealA += cA
    return getAmt(card1) + getAmt(card3), userA, getAmt(card2) + getAmt(card4), dealA

def main():
    #Local Variable
    ccards = copy.copy(cards)
    stand = False
    newGame = True
    userCard = []
    dealCard = []
    playerPot = 100
    playerBet = 0
   
    #Initialize Game
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Blackjack')
    font = pygame.font.SysFont('arial', 15)
    hitTxt = font.render('Hit', 1, black)
    standTxt = font.render('Stand', 1, black)
    doubleTxt = font.render('Double Down', 1, black)
    restartTxt = font.render('New Game', 1, black)
    gameoverTxt = font.render('GAME OVER', 1, white)
    newBetTxt = font.render('Place your bet!', 1, white)
    # Added bet features
    bet1Txt = font.render('5', 1, black)
    bet2Txt = font.render('10', 1, black)
    bet3Txt = font.render('15', 1, black)

    userSum, userA, dealSum, dealA = 0, 0, 0, 0
    userSumTxt = font.render(str(userSum), 1, black)

    #Fill Background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((80, 150, 15))
    hitB = pygame.draw.rect(background, gray, (10, 445, 75, 25))
    standB = pygame.draw.rect(background, gray, (95, 445, 75, 25))
    doubleB = pygame.draw.rect(background, gray, (180, 445, 115, 25))
    ratioB = pygame.draw.rect(background, gray, (555, 420, 75, 50))
    # Create buttons for betting and scoreboard
    bet1B = pygame.draw.rect(background, gray, (305, 445, 25, 25))
    bet2B = pygame.draw.rect(background, gray, (335, 445, 25, 25))
    bet3B = pygame.draw.rect(background, gray, (365, 445, 25, 25))
    scoreboard = pygame.draw.rect(background, gray, (555, 200, 75, 75))

    hit = 0
    play = 0    #flag variable. if its 0, the game has not been started yet.
    #Event Loop
    while True:
        gameover = True if (userSum >= 21 and userA == 0) or len(userCard) == 5 else False
        if len(userCard) == 2 and userSum == 21:
            gameover = True
            playerBet = playerBet*1.5
        elif len(dealCard) == 2 and dealSum == 21:
            gameover = True

        # checks for mouse clicks on buttons for bets


        #background needs to be redisplayed because it gets updated
        # Keeps pot and bets updated
        potTxt = font.render('Pot: %i' % playerPot, 1, black)
        betTxt = font.render('Bet: %i' % playerBet, 1, black)


        #checks for mouse clicks on buttons
        for event in pygame.event.get():
            # checks for clicks for certain bet amounts provided
            if event.type == pygame.MOUSEBUTTONDOWN and bet1B.collidepoint(pygame.mouse.get_pos()) and play == 0:
                playerBet = 5
            elif event.type == pygame.MOUSEBUTTONDOWN and bet2B.collidepoint(pygame.mouse.get_pos()) and play == 0:
                playerBet = 10
            elif event.type == pygame.MOUSEBUTTONDOWN and bet3B.collidepoint(pygame.mouse.get_pos()) and play == 0:
                playerBet = 15


            if event.type == QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not (gameover or stand) and hitB.collidepoint(pygame.mouse.get_pos()):
                # gives player a card if they don't break blackjack rules
                # hit is a flag variable. You can not double if you've already hit
                hit = 1
                card, cA = genCard(ccards, userCard)
                userA += cA
                userSum += getAmt(card)
                while userSum > 21 and userA > 0:
                    userA -= 1
                    userSum -= 10
            elif event.type == pygame.MOUSEBUTTONDOWN and not gameover and standB.collidepoint(pygame.mouse.get_pos()):
                #when player stands, the dealer plays
                stand = True
                while dealSum <= 17:
                    card, cA = genCard(ccards, dealCard)
                    dealA += cA
                    dealSum += getAmt(card)
                    while dealSum > 21 and dealA > 0:
                        dealA -= 1
                        dealSum -= 10
            elif event.type == pygame.MOUSEBUTTONDOWN and not (gameover or stand) and doubleB.collidepoint(pygame.mouse.get_pos()) and hit == 0:
                # doubles a players bet and gives them one card. Dealers play
                playerBet = playerBet*2
                card, cA = genCard(ccards, userCard)
                userA += cA
                userSum += getAmt(card)
                while userSum > 21 and userA > 0:
                    userA -= 1
                    userSum -= 10
                stand = True
                # Dealer plays
                while dealSum <= 17:
                    card, cA = genCard(ccards, dealCard)
                    dealA += cA
                    dealSum += getAmt(card)
                    while dealSum > 21 and dealA > 0:
                        dealA -= 1
                        dealSum -= 10
            elif event.type == pygame.MOUSEBUTTONDOWN and (gameover or stand or newGame) and restartB.collidepoint(pygame.mouse.get_pos()):
                # restarts the game, updating scores
                if userSum == dealSum:
                    pass
                elif userSum <= 21 and len(userCard) == 5:
                    playerPot += playerBet
                elif dealSum < userSum <= 21 or dealSum > 21:
                    playerPot += playerBet
                else:
                    playerPot -= playerBet
                play = 1
                gameover = False
                stand = False
                newGame = False
                userCard = []
                dealCard = []
                ccards = copy.copy(cards)
                userSum, userA, dealSum, dealA = initGame(ccards, userCard, dealCard)
                restartB = pygame.draw.rect(background, (80, 150, 15), (270, 225, 75, 25))

        # loads words into program
        screen.blit(background, (0, 0))
        screen.blit(hitTxt, (39, 448))
        screen.blit(standTxt, (116, 448))
        screen.blit(doubleTxt, (201, 448))
        screen.blit(bet1Txt, (315, 448))
        screen.blit(bet2Txt, (340, 448))
        screen.blit(bet3Txt, (370, 448))
        screen.blit(potTxt, (565, 423))
        screen.blit(betTxt, (565, 448))

        dScoreTxt = font.render('Dealer: %i' %dealSum, 1, black)
        uScoreTxt = font.render('Player: %i' % userSum, 1, black)
        scoreTxt = font.render('Score', 1, black)
        screen.blit(uScoreTxt, (560, 250))
        screen.blit(scoreTxt, (575, 205))

        #displays dealer's cards
        for card in dealCard:
            x = 10 + dealCard.index(card) * 110
            screen.blit(card, (x, 10))
        if newGame:
            pass
        else:
            screen.blit(cBack, (120, 10))

        #displays player's cards
        for card in userCard:
            x = 10 + userCard.index(card) * 110
            screen.blit(card, (x, 295))

        #when game is over, draws restart button and text, and shows the dealer's second card
        if gameover or stand:
            # checks to see if you won, lost or pushed
            if dealSum < userSum <= 21 or dealSum > 21:
                gameoverTxt = font.render('You win!', 1, white)
            elif dealSum == userSum:
                gameoverTxt = font.render('You pushed!', 1, white)
            else:
                gameoverTxt = font.render('You lose!', 1, white)
            screen.blit(dScoreTxt, (560, 230))
            screen.blit(gameoverTxt, (270, 200))
            screen.blit(newBetTxt, (270, 260))
            restartB = pygame.draw.rect(background, gray, (270, 225, 75, 25))
            screen.blit(restartTxt, (275, 228))
            screen.blit(dealCard[1], (120, 10))
            hit = 0
            play = 0
        elif newGame:
            screen.blit(restartTxt, (275, 228))
            restartB = pygame.draw.rect(background, gray, (270, 225, 75, 25))
            screen.blit(newBetTxt, (270, 260))
            hit = 0
            play = 0
        pygame.display.update()
            

if __name__ == '__main__':
    main()
