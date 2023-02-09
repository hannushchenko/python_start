import random

numbers = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
colors = ['♠','♥','♦','♣']
cards = []
myCards = []
res = 0
work = True
has_a = False

def createCards():
    for c in colors:
        for n in numbers:
            # print(n, c, end='  ')
            cards.append((n,c))
        # print('')
        return cards

def pickRandom():
    rand = random.randint(0,len(cards)-1)
    delCard = cards.pop(rand)
    return delCard

def startCards():
    for n in range(2):
        x = pickRandom()
        myCards.append(x)
    print(myCards)

def calculateResult():
    global work
    global has_a
    res = 0
    another_res=0

    for c in myCards:
        (a, b) = c
        match a:
            case 'J':
                a = 2
            case 'Q':
                a = 3
            case 'K':
                a = 4
            case 'A':
                if res < 11:
                    a = 11
                    has_a = True
                else:
                    a = 1
            case _:
                a = int(a)
        res += a
    if(res>21):
        if not has_a:
            print("LOSE")
            work = False
        else:
            res-=10
    elif(res==21):
        print("Win")
        work = False
    print(res)
    return res

def getCard():
    global work
    while work:
        q = input("Do You Need One Card More? Press +: ")
        if q == '+':
            new = pickRandom()
            myCards.append(new)
            print(new)
            calculateResult()
        else:
            work = False

createCards()
startCards()
calculateResult()
getCard()