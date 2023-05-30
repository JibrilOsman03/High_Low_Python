# you'll need the random module
import random

### Write your functions below ###
def getCardValue():
    return random.randint(2, 14)

def getCardStr(cardValue):
    if (cardValue >= 2 and cardValue <= 9):
        return str(cardValue)
    elif (cardValue == 10):
        return "T"
    elif (cardValue == 11):
        return "J"
    elif (cardValue == 12):
        return "Q"
    elif (cardValue == 13):
        return "K"
    else:
        return "A"

def getHLGuess():
    guess = ""
    while(guess != "H" and guess != "L"):
        guess = input("High or Low (H/L): ")
        guess = guess.upper()
    if guess == "H":
        return "HIGH"
    if guess == "L":
        return "LOW"

def getBetAmount(maximum):
    amount = -69
    while (amount <= 0 or amount > maximum):
        amount = int(input("Input bet amount: "))
    return amount

def playerGuessCorrect(card1, card2, betType):
    if betType == "HIGH":
        if card1 < card2:
            return True
        else:
            return False
    elif betType == "LOW":
        if card1 > card2:
            return True
        else:
            return False

### Write your main program below ####
msg = """--- Welcome to High-Low ---
Start with 100 points.  Each round a card will be drawn and shown.
Select whether you think the 2nd card will be Higher or Lower than the 1st card.
Then enter the amount you want to bet.
If you are right, you win the amount you bet, otherwise you lose. 
Try to make it to 500 points within 10 tries."""

print(msg)
pts = 100
turns = 1
while (pts > 0 and pts < 500 and turns !=11):
    print("\n-------------------------------------")
    print("OVERALL POINTS: %d ROUND %d/10" %(pts, turns))
    cardA = getCardValue()
    stringA = getCardStr(cardA)
    print("First card is a [%s]" % (stringA))
    stringBet = getHLGuess()
    betAmount = getBetAmount(pts)
    cardB = getCardValue()
    stringB = getCardStr(cardB)
    guessCheck = playerGuessCorrect(cardA, cardB, stringBet)
    print("Second card is a [%s]" % (stringB))
    if guessCheck == True:
        pts += betAmount
        print("Card1 [%s] Card2 [%s] - You bet '%s' for %d - YOU WON" % (stringA, stringB, stringBet, betAmount))
    if guessCheck == False:
        pts -= betAmount
        print("Card1 [%s] Card2 [%s] - You bet '%s' for %d - YOU LOST" % (stringA, stringB, stringBet, betAmount))
    turns += 1

if pts >= 500:
   print("------------------WIN------------------")
   print("YOU MADE IT TO *%d* POINTS IN %d ROUNDS!" % (pts, turns))
else:
   print("------------------LOSE------------------")
   print("YOU HAVE *%d* POINTS AFTER %d ROUNDS!" % (pts, turns))
print("---------------------------------------")

endVariable = input("Press enter to exit: ")