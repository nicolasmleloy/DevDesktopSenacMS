import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QAction, QWidget
from tabuada import Ui_MainWindow 

class Tabuada(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.botao.clicked.connect(self.ExibirTabuada)

    def ExibirTabuada(self):
        num = self.ui.numero.value()
        textoTabuada = ""
        for i in range(1, 10 + 1):
            textoTabuada += f"{i} x {num} = {i * num}\n"

        self.ui.resultado.setText(textoTabuada)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Tabuada()
    mainWindow.show()
    sys.exit(app.exec_())