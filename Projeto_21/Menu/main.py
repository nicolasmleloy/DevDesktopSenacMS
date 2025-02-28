import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from Menu import Ui_MainWindow
from TelaInicial import TelaInicial  # Importando a tela inicial

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnStart.clicked.connect(self.Redirecionar)

    def Redirecionar(self):
        self.tela_inicial = TelaInicial()  # Criar instância da tela inicial
        self.tela_inicial.show()  # Mostrar a tela inicial
        self.close()  # Fechar o menu

class TelaInicial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = TelaInicial()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    mainWindow = Menu()  # Começa pelo menu
    mainWindow.show()
    sys.exit(app.exec_())
