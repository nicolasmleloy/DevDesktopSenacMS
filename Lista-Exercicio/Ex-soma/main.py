import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QAction, QWidget
from Soma import Ui_MainWindow 

class Soma(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.acaoBotao)

    def acaoBotao(self):
        n1 = int(self.ui.spinBox.text())
        n2 = int(self.ui.spinBox_2.text())
        soma = str(n1 + n2)
        self.ui.label_4.setText(soma)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Soma()
    mainWindow.show()
    sys.exit(app.exec_())