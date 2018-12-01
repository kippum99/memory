import random
from string import ascii_lowercase

cardsDict = dict(zip(ascii_lowercase, range(0, 26)))
cards = list(cardsDict.keys())
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']
symbols += symbols
random.shuffle(symbols)

def showCards(cards):
    print('\n')
    counter = 0
    for i in range(0, 4):
        line = ''
        for j in range(0, 4):
            line += cards[counter] + ' '
            counter += 1
        print(line + '\n')

def playGame():
    global cards
    showCards(cards)
    flips = 0
    cardsLeft = 16
    while cardsLeft > 0:
        flips += 1
        currentCards = cards.copy()
        first = input()
        firstIndex = cardsDict[first]
        currentCards[firstIndex] = symbols[firstIndex]
        showCards(currentCards)
        second = input()
        secondIndex = cardsDict[second]
        currentCards[secondIndex] = symbols[secondIndex]
        showCards(currentCards)
        if symbols[firstIndex] == symbols[secondIndex]:
            cards[firstIndex] = ' '
            cards[secondIndex] = ' '
            cardsLeft -= 2
    print(f'Game finished with {flips} flips')

if __name__ == '__main__':
    playGame()
