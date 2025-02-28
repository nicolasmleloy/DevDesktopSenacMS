import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QAction, QWidget
from somaNumeros import Ui_MainWindow 

class somaNumeros(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.botao.clicked.connect(self.ExibirSoma)

    def ExibirSoma(self):
        num = self.ui.numero.value()
        soma = sum(range(1, num + 1))
        self.ui.resultado.setText(f"A soma de 1 a {num} é: {soma}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = somaNumeros()
    mainWindow.show()
    sys.exit(app.exec_())