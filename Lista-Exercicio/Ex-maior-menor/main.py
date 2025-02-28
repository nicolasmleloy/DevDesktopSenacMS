import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QAction, QWidget
from maiorMenor import Ui_MainWindow 

class maiorMenor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.botao.clicked.connect(self.MaiorEMenor)

    def MaiorEMenor(self):
        n1 = int(self.ui.n1.text())
        n2 = int(self.ui.n2.text())
        n3 = int(self.ui.n3.text())

        numeros = []
        numeros.append(n1)
        numeros.append(n2)
        numeros.append(n3)

        maior = max(numeros)
        menor = min(numeros)
        self.ui.resultado.setText(f"Maior: {maior}\n Menor: {menor}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = maiorMenor()
    mainWindow.show()
    sys.exit(app.exec_())