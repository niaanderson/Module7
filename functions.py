import random

def randomCardsForDealerHand ():
    dealerHand =[]
    starterNumberOfCards=2
    for currentCard in range(starterNumberOfCards):
        dealerHand.append(random.randint(1,10))

def dealerTotalSumFunction ():
    dealerTotalSum = dealerHand[0] + dealerHand[1]

def showDealerHand():
    dealerVisibleCards =[dealerHand[0]]
    print( "The dealer has 2 cards. One card is a: \n")
    print(dealerVisibleCards)

def randomCardsForUserHand ():
    userHand = []
    starterNumberOfCards=2
    for currentCard in range(starterNumberOfCards):
        userHand.append(random.randint(1,10))
    print("Your current hand is: \n")
    print(userHand)

def userTotalSumFunction ():
    sumOfTotal = userHand[0] + userHand[1] + userHand[2] + userHand[3]  + userHand[4]
    print( "Your current total is: \n")
    print(sumOfTotal)

def round1To4Rules ():
    if sumOfTotal == 21:
        print("You won!")
    elif sumOfTotal > 21:
        print("You lost!")
    elif sumOfTotal < 21:
        #Round 2
        hit = input("Do you want to hit and take another card? \nEnter yes to hit and anything else for no: \n")
        print("You selected: " + hit)

def hit ():
    newNumber= random.randint(1,10)
    print("You recieved a: \n")
    print(newNumber)

    userHand.append(newNumber)

    print("Your current hand is: \n")
    print(userHand)

def finalRoundRules ():
    if sumOfTotal == 21:
        print("You won!")
    elif sumOfTotal > dealerTotalSum and sumOfTotal < 21:
        print( "You won!")
     elif sumOfTotal < dealerTotalSum:
        print( "Sorry. You have lost.")
    else:
        print("You lost!")
                
def fullDealerHandReveal ():   
    print( "The dealer's hand was: \n")
    print(dealerHand)
    print( "The dealer's total was: \n")
    print(dealerTotalSum)
                
def openEndMessageFile ():
    openFile= open("openFile.txt", "w")
    openFile.write("Congratulations! You just played my first Python game! TY :) I hope you had as much fun playing the game, as I did creating it!")
    openFile.close()    

def readEndMessageFile ():
    openFile= open("openFile.txt", "r")
    print(openFile.read())

# How do I put this all together??