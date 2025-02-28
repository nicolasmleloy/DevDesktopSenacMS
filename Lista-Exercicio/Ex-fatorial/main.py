import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QAction, QWidget
from Fatorial import Ui_MainWindow 

class Fatorial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.botao.clicked.connect(self.exibirRes)

    def exibirRes(self):
        numero = self.ui.inputNumero.value()
        mult = 1
        for i in range(numero, 1, -1):
            mult *= i
        self.ui.resultado.setText(f"Fatorial de {numero} = {mult}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Fatorial()
    mainWindow.show()
    sys.exit(app.exec_())