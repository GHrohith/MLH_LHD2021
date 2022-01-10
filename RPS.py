import random

playerScore = 0
botScore = 0

maxScore = int(input("Enter maximum score : "))

while (playerScore<maxScore and botScore<maxScore) :

    while (True):
        inp = input("Choose your move (R,P,S, or E to exit) : ")

        inp = inp.lower()
        
        if (inp not in ['r','p','s','e']):
            print("Wrong Input. Try Again.")
        else :
            break

    if (inp=='e'):
        break

    botMove = random.choice(['r','p','s'])

    print("The bot chose " + botMove + ".")

    moveConc = inp + botMove

    if (moveConc in ['rs','pr','sp']):
        print("You got a point.")
        playerScore += 1
    elif (moveConc in ['sr','rp','ps']):
        print("The bot got a point.")
        botScore +=1
    else :
        print("Nobody gets a point.")

if botScore == maxScore :
    print("The bot won.")
else :
    print("You won!")


    
