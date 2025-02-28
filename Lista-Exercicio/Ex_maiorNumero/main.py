import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QAction, QWidget
from maiorNumero import Ui_MainWindow 

class maiorNumero(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.botao.clicked.connect(self.exibirMaior)

    def exibirMaior(self):
        n1 = self.ui.n1.value()
        n2 = self.ui.n2.value()
        n3 = self.ui.n3.value()

        maior = n1
        if(n2 > maior):
            maior = n2
        
        if(n3 > maior):
            maior = n3

        self.ui.resultado.setText(f"Maior número é: {maior}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = maiorNumero()
    mainWindow.show()
    sys.exit(app.exec_())