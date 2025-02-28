import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QAction, QWidget
from fatorial import Ui_MainWindow 

class fatorial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.botao.clicked.connect(self.Resultado)

    def Resultado(self):
        numero = int(self.ui.numero.text())
        mult = 1
        res = ""
        for i in range(1, numero + 1):
            if(i == numero):
                mult *= i
                res += f"{i}"
            else:
                mult *= i
                res += f"{i}."


        self.ui.resultado.setText(f"!{numero} = {res} = {mult}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = fatorial()
    mainWindow.show()
    sys.exit(app.exec_())