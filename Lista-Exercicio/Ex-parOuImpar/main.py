import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QAction, QWidget
from ParOuImpar import Ui_MainWindow 

class ParOuImpar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.botao.clicked.connect(self.exibirRes)

    def exibirRes(self):
        numero = int(self.ui.inputNumero.text())
        if(numero % 2 == 0):
            self.ui.resultado.setText(f"{numero} é par!")
        else:
            self.ui.resultado.setText(f"{numero} é ímpar!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = ParOuImpar()
    mainWindow.show()
    sys.exit(app.exec_())