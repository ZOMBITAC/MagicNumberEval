from random import randint
from common.imodel import IModel

class Model(IModel):

    __magicNumber: int
    __num: int
    __maxproposition: int
    __tentative: int

    def __init__(self, num: int):
        self.__num = num
        self.__maxproposition = 10
        self.__tentative = 0
        self.__magicNumber = randint(0, 100)

    def compareToMagicNumber(self, num: int) -> int:
        if self.__tentative >= self.__maxproposition:
            print("Tu as épuisé toutes tes tentatives !")
            return -2

        if num > self.__magicNumber:
            print("Trop grand !")
            self.__tentative += 1
            return 1
        elif num < self.__magicNumber:
            print("Trop petit !")
            self.__tentative += 1
            return -1
        else:
            print("Trouvé !!!")
            self.__tentative += 1
            return 0

    def getProposalCount(self) -> bool:
        remaining = self.__maxproposition - self.__tentative
        print(f"Il vous reste {remaining} tentatives.")
        if self.__tentative == self.__maxproposition:
            print("Tu as perdu")
            return True
        return False

    def getMaxNumberOfProposals(self) -> int:
        return self.__maxproposition
