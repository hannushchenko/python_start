import random

numbers = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
colors = ['♠','♥','♦','♣']
cards = []
myCards = []
work = True
has_ace = 0


def createCards():
    for c in colors:
        for n in numbers:
            match n:
                case 'J':
                    v = 2
                case 'Q':
                    v = 3
                case 'K':
                    v = 4
                case 'A':
                    v = 11
                case 'a':
                    v = 1
                case _:
                    v = int(n)
            cards.append((n, c, v))
        # print('')
        return cards

def pickRandom():
    global has_ace
    randIndex = random.randint(0, len(cards)-1)
    delCard = cards.pop(randIndex)
    (n, c, v)= delCard
    if n=="A":
        has_ace +=1
    return delCard

def startCards():
    for n in range(2):
        x = pickRandom()
        myCards.append(x)
    print(myCards)

def calculateResult():
    global work
    global has_ace
    res = 0

    for card in myCards:
        (n, c, v) = card
        res += v
    if res < 21:
        print(f"РЕЗУЛЬТАТ: {res}")


    if res == 21:
        print("WIN!")
        work = False
    elif res > 21:
        if has_ace > 0:
            for card in myCards:
                    (n, c, v) = card
                    if n == "A":
                        index_card = myCards.index(card)
                        n = "a"
                        v = 1
                        res = res - 10
                        has_ace = has_ace - 1
                        myCards[index_card] = (n, c, v)

            print(f"РЕЗУЛЬТАТ: {res}")

        else:
            print(f"LOSE {res}")
            work = False
    else:
        getCard()


    return res

def getCard():
    global work
    while work:
        q = input("Do You Need One Card More? Press +: ")
        if q == '+':
            new = pickRandom()
            myCards.append(new)
            print(myCards)
            calculateResult()
        else:
            work = False

createCards()
startCards()
calculateResult()