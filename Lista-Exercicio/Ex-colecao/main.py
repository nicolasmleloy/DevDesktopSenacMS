import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from colecao import Ui_MainWindow 

class Colecao(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.botao.clicked.connect(self.Contar)
        self.qtd = self.ui.qtd.value()

        self.cont = 1
        self.ui.contagem.setText(f"Valor do {self.cont}° CD")
        self.valores = []

    def Contar(self):
        try:
            if(self.cont < self.qtd):
                self.cont += 1
                valor = float(self.ui.valor.text())

                self.valores.append(valor)
                self.ui.contagem.setText(f"Valor do {self.cont}° CD")

                print("Valores cadastrados:", self.valores)
            else:
                return
            
        except ValueError:
            print("Erro: Certifique-se de inserir números válidos.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Colecao()
    mainWindow.show()
    sys.exit(app.exec_())
