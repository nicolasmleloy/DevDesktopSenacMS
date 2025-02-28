import sys
import random
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QAction, QWidget
from TelaInicial import Ui_MainWindow 

class TelaInicial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.cartas_blackjack = ['Ás de Copas', 'Ás de Ouros', 'Ás de Espadas', 'Ás de Paus', 
        '2 de Copas', '2 de Ouros', '2 de Espadas', '2 de Paus', 
        '3 de Copas', '3 de Ouros', '3 de Espadas', '3 de Paus', 
        '4 de Copas', '4 de Ouros', '4 de Espadas', '4 de Paus', 
        '5 de Copas', '5 de Ouros', '5 de Espadas', '5 de Paus', 
        '6 de Copas', '6 de Ouros', '6 de Espadas', '6 de Paus', 
        '7 de Copas', '7 de Ouros', '7 de Espadas', '7 de Paus', 
        '8 de Copas', '8 de Ouros', '8 de Espadas', '8 de Paus', 
        '9 de Copas', '9 de Ouros', '9 de Espadas', '9 de Paus', 
        '10 de Copas', '10 de Ouros', '10 de Espadas', '10 de Paus', 
        'Valete de Copas', 'Valete de Ouros', 'Valete de Espadas', 'Valete de Paus', 
        'Dama de Copas', 'Dama de Ouros', 'Dama de Espadas', 'Dama de Paus', 
        'Rei de Copas', 'Rei de Ouros', 'Rei de Espadas', 'Rei de Paus']

        self.ui.botao_continuar.clicked.connect(self.RandomCarta)

    def RandomCarta(self):
        carta = random.sample(self.cartas_blackjack)
        print(carta)
    
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    mainWindow = TelaInicial()
    mainWindow.show()
    sys.exit(app.exec_())