#!/usr/bin/python3
__author__ = "Vitaly Bibikov"
__version__ = "0.1"

from random import shuffle
from random import getrandbits


def __main__():
    game = Game(16)
    game.start()
    return


class Lotto(object):

    def __init__(self, number):
        self.number = number
        self.barrelList = self.getShuffledList()

    def getRandomBarrel(self):
        return self.barrelList.pop()

    def getBarrelCount(self):
        return len(self.barrelList)

    def getShuffledList(self):
        arr = list(range(1, self.number + 1))
        shuffle(arr)
        return arr

    def createRandomCard(self):
        chunks = 5
        lines = 3
        slots = 9 - chunks
        arr = self.getShuffledList()[0:chunks * lines]
        stripes = [sorted(arr[i:i + chunks])
                   for i in range(0, len(arr), chunks)]
        i = 0
        while i < lines:
            stripes[i].extend([0] * slots)
            shuffle(stripes[i])
            i += 1
        return stripes


class Game(object):
    """docstring for  Game"""

    def __init__(self, number):
        self.lotto = Lotto(number)
        self.number = number
        self.compScore = 0
        self.playerScore = 0
        self.computerCard = self.lotto.createRandomCard()
        self.playerCard = self.lotto.createRandomCard()

    def make_move(self):
        if self.number > 0:
            number = self.getBarrel()
            self.displayCards()
            choiceToCross = self.askPlayerDescision()
            player = self.checkMove(self.__cross_number__(
                self.playerCard, number), choiceToCross)
            computer = self.checkMove(self.__cross_number__(
                self.computerCard, number, False), True) #getrandbits(1)
        return self.__validateNextMove__(player, computer)

# gameContinues =

    def checkMove(self, isItemPresented, choiceToCross):
        result = True if choiceToCross and isItemPresented or not choiceToCross and not isItemPresented else False
        return result

    def askPlayerDescision(self):
        makeMove = False
        while True:
            descision = input("Cross the number? (y/n) \n")
            if descision.lower() == 'n':
                break
            elif descision.lower() == 'y':
                makeMove = True
                break
            else:
                print("Wrong input. Please try again.")
        return makeMove

    def getBarrel(self):
        barrel = self.lotto.getRandomBarrel()
        self.number = self.lotto.getBarrelCount()
        print("New number: {} (left {})".format(barrel, self.number))
        return barrel

    def displayCards(self):
        print('------ Your card -----')
        [print(i) for i in self.playerCard]
        print('--------------------------')
        print('-- Computer\'s card ---')
        [print(i) for i in self.computerCard]
        print('--------------------------')
        return

    def __cross_number__(self, arr, searched, isPlayersMove = True):
        itemPresented = False
        v = ()
        try:
            v = [(i, row.index(searched))
                 for i, row in enumerate(arr) if searched in row]
            v = v[0]
        except Exception:
            pass
        else:
            if isPlayersMove:
                self.playerScore += 1
            else:
                self.compScore += 1

            arr[v[0]][v[1]] = '-'
            itemPresented = True
        return itemPresented

    def __validateNextMove__(self, player, computer):
        gameOver = False
        if player and computer:
            pass
        elif player and not computer:
            print("Player wins.")
            gameOver = True
        else:
            print("Computer wins.")
            gameOver = True

        if self.playerScore >= 15:
            gameOver = True
            print("Player wins crossing all his lines!")
        elif self.compScore >= 15:
            gameOver = True
            print("Computer wins crossing all it's lines first. Stupid human.")

        return not gameOver

    def start(self):
        while self.make_move():
            print("Another round!!!")
        print("Game over")


if __name__ == '__main__':
    __main__()
