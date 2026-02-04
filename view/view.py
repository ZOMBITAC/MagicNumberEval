from common.iview import IView
from common.imodel import IModel
from common.icontroller import IController

class View(IView):
    __model: IModel
    __controller: IController

    def __init__(self):
        self.__model = None
        self.__controller = None

    def setModel(self, model: IModel) -> None:
        self.__model = model

    def setController(self, controller: IController) -> None:
        self.__controller = controller

    def showMessage(self, message: str) -> None:
        print(message)

    def askProposal(self) -> int:
        while True:
            try:
                self.showMessage("Entrez une proposition de nombre :")
                num = int(input())
                return num
            except ValueError:
                self.showMessage("Erreur : veuillez entrer un nombre entier valide.")
