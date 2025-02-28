import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QAction, QWidget
from vetorInteiros import Ui_MainWindow 

class vetorInteiros(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.botao.clicked.connect(self.Resultado)

    def Resultado(self):
        vetor = self.ui.vetor.text()
        v = []