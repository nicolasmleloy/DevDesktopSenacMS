import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QAction, QWidget
from decrescente import Ui_MainWindow 

class decrescente(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.botao.clicked.connect(self.ExibirDecrescente)

    def ExibirDecrescente(self):
        n1 = int(self.ui.n1.text())
        n2 = int(self.ui.n2.text())
        n3 = int(self.ui.n3.text())
        numeros = []

        numeros.append(n1)
        numeros.append(n2)
        numeros.append(n3)

        numeros.sort(reverse=True)
        text = ""

        for i in range(len(numeros)):
            if(i == len(numeros) - 1):
                text += f"{numeros[i]}"
            else:
                text += f"{numeros[i]}, "


        self.ui.resultado.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = decrescente()
    mainWindow.show()
    sys.exit(app.exec_())