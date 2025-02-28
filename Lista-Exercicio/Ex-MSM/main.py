import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QAction, QWidget
from MSM import Ui_MainWindow 

class MSM(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.botao.clicked.connect(self.ExibirResultado)

    def ExibirResultado(self):
        n1 = float(self.ui.n1.text())
        n2 = float(self.ui.n2.text())
        n3 = float(self.ui.n3.text())
        n4 = float(self.ui.n4.text())
        n5 = float(self.ui.n5.text())
        listNum = []

        listNum.append(n1)
        listNum.append(n2)
        listNum.append(n3)
        listNum.append(n4)
        listNum.append(n5)

        media = sum(listNum) / len(listNum)
        text = f"Maior: {max(listNum)}\n Soma: {sum(listNum)}\n Média: {media}"
        self.ui.resultado.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MSM()
    mainWindow.show()
    sys.exit(app.exec_())