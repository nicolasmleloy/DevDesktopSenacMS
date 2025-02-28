import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QAction, QWidget
from lojaDeTinta import Ui_MainWindow 

class lojaDeTinta(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnCalcular.clicked.connect(self.CalcularResultado)

    def CalcularResultado(self):
        metroLata = 18 * 3
        valorLata = 80.00

        qtdLatasComprar = float(self.ui.metrosQuadrados.text()) / metroLata
        
        if(float(self.ui.metrosQuadrados.text()) < 54):
            qtdLatasComprar = 1

        precoTotal = qtdLatasComprar * valorLata
        self.ui.resultado.setText(f"Qtd latas a comprar: {round(qtdLatasComprar, 0)}\n Preço total R${precoTotal:.2f}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = lojaDeTinta()
    mainWindow.show()
    sys.exit(app.exec_())