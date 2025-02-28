import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QAction, QWidget
from turno import Ui_MainWindow 

class turno(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.botao.clicked.connect(self.ExibirMensagem)

    def ExibirMensagem(self):
        turno = self.ui.turno.text()

        if(turno == "M" or turno == "m"):
            self.ui.resultado.setText("Bom dia!")
        elif(turno == "V" or turno == "v"):
            self.ui.resultado.setText("Boa tarde!")
        elif(turno == "N" or turno == "n"):
            self.ui.resultado.setText("Boa noite!")
        else:
            self.ui.resultado.setText("Valor inválido!")
            self.ui.resultado.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n""color: red;")
        
        self.ui.turno.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = turno()
    mainWindow.show()
    sys.exit(app.exec_())