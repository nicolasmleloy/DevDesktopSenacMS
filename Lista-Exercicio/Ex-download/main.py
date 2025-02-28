import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QAction, QWidget
from download import Ui_MainWindow 

class download(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnCalcular.clicked.connect(self.CalcularVelocidade)

    def CalcularVelocidade(self):
        tamArquivo = float(self.ui.tamArq.text())
        velocidadeInternet = float(self.ui.velocidadeInternet.text())

        velocidadeDownload = tamArquivo / velocidadeInternet
        self.ui.resultado.setText(f"Velocidade = {velocidadeDownload}Mbps")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = download()
    mainWindow.show()
    sys.exit(app.exec_())