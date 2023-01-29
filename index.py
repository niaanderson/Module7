import random

def main():
    #Round 1

    #Dealer Hand
    dealerHand =[]
    starterNumberOfCards=2
    for currentCard in range(starterNumberOfCards):
        dealerHand.append(random.randint(1,10))

    dealerTotalSum = dealerHand[0] + dealerHand[1]

    dealerVisibleCards =[dealerHand[0]]
    print( "The dealer has 2 cards. One card is a: \n")
    print(dealerVisibleCards)

    #User Hand
    userHand = []
    starterNumberOfCards=2
    for currentCard in range(starterNumberOfCards):
        userHand.append(random.randint(1,10))
    print("Your current hand is: \n")
    print(userHand)

    #Decision Structure
    sumOfTotal = userHand[0] + userHand[1]
    print( "Your current total is: \n")
    print(sumOfTotal)
    if sumOfTotal == 21:
        print("You won!")
    elif sumOfTotal > 21:
        print("You lost!")
    elif sumOfTotal < 21:
        #Round 2
        hit = input("Do you want to hit and take another card? \nEnter yes to hit and anything else for no: \n")
        print("You selected: " + hit)

        newNumber= random.randint(1,10)
        print("You recieved a: \n")
        print(newNumber)

        userHand.append(newNumber)

        print("Your current hand is: \n")
        print(userHand)
        
        #Decision Structure
        sumOfTotal = userHand[0] + userHand[1] + userHand[2]
        print( "Your current total is: \n")
        print(sumOfTotal)
        if sumOfTotal == 21:
            print("You won!")
        elif sumOfTotal > 21:
            print("You lost!")
        elif sumOfTotal < 21:
            #Round 3
            hit = input("Do you want to hit and take another card? \nEnter yes to hit and anything else for no:\n")
            print("You selected: " + hit)

            number4 = random.randint(0,10)
            print("You recieved a: \n")
            print(number4)

            userHand.append(number4)

            print("Your current hand is: \n")
            print(userHand)
        
            #Decision Structure
            sumOfTotal = userHand[0] + userHand[1] + userHand[2] + userHand[3]
            print( "Your current total is: \n")
            print(sumOfTotal)
            if sumOfTotal == 21:
                print("You won!")
            elif sumOfTotal > 21:
                print("You lost!")
            elif sumOfTotal < 21:
                #Round 4
                hit = input("Do you want to hit and take another card?\nEnter yes to hit and anything else for no:")
                print("You selected: " + hit)

                number5 = random.randint(0,10)
                print("You recieved a: \n")
                print(number5)

                userHand.append(number5)

                print("Your current hand is: \n")
                print(userHand)
                
                #Decision Structure
                sumOfTotal = userHand[0] + userHand[1] + userHand[2] + userHand[3]  + userHand[4]
                print( "Your current total is: \n")
                print(sumOfTotal)
                if sumOfTotal == 21:
                    print("You won!")
                    
                    print( "The dealer's hand was: \n")
                    print(dealerHand)
                    print( "The dealer's total was: \n")
                    print(dealerTotalSum)
                    
                elif sumOfTotal > dealerTotalSum and sumOfTotal < 21:
                    print( "You won! The dealer's hand was: \n")
                    print(dealerHand)
                    print( "The dealer's total was: \n")
                    print(dealerTotalSum)
                    
                elif sumOfTotal < dealerTotalSum:
                    print( "Sorry. You have lost. The dealer's hand was: \n")
                    print(dealerHand)
                    print( "The dealer's total was: \n")
                    print(dealerTotalSum)
                    
                else:
                    print("You lost!")
                    
                    print( "The dealer's hand was: \n")
                    print(dealerHand)
                    print( "The dealer's total was: \n")
                    print(dealerTotalSum)

    #OPEN WRITE AND READ FILE
    openFile= open("openFile.txt", "w")
    openFile.write("Congratulations! You just played my first Python game! TY :) I hope you had as much fun playing the game, as I did creating it!")
    openFile.close()

    openFile= open("openFile.txt", "r")
    print(openFile.read())
    
main()

