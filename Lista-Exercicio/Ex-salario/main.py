import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QAction, QWidget
from salario import Ui_MainWindow 

class salario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnCalcular.clicked.connect(self.CalcularSalario)

    def CalcularSalario(self):
        qtdHora = float(self.ui.qtdHora.text())
        horasTrabalhadas = float(self.ui.horasTrabalhadas.text())

        self.ui.salarioFinal.setText(f"Salario mensal = R${qtdHora * horasTrabalhadas:.2f}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = salario()
    mainWindow.show()
    sys.exit(app.exec_())