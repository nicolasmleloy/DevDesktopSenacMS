import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QAction, QWidget
from nome import Ui_MainWindow 

class Nome(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.acaoBotao)

    def acaoBotao(self):
        self.ui.label_4.setText(self.ui.lineEdit.text())


if __name__ == "__main__":
    app = QApplication(sys.argv) 
    mainWindow = Nome()
    mainWindow.show()
    sys.exit(app.exec_())