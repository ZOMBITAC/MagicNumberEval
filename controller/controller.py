from common.icontroller import IController
from common.iview import IView
from common.imodel import IModel

class Controller(IController):
    __view: IView
    __model: IModel

    def __init__(self):
        self.__view = None
        self.__model = None

    def setView(self, view: IView) -> None:
        self.__view = view

    def setModel(self, model: IModel) -> None:
        self.__model = model

    def performProposeNumber(self, num: int) -> None:
        if self.__model is not None:
            result = self.__model.compareToMagicNumber(num)
            if result == 0:
                self.__view.showMessage("Félicitations, vous avez trouvé le nombre magique !")
            self.__model.getProposalCount()

    def start(self) -> None:
        pass