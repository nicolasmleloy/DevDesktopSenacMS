import sys
import os
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QAction, QWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from ReprodutorMusica import Ui_MainWindow


class Reprodutor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.player = QMediaPlayer(self)
        self.ui.pushButton.clicked.connect(self.Play)
        self.ui.pushButton_2.clicked.connect(self.Parar)

    def Play(self):
        pathMusic = os.path.abspath("./Musicas/qui-fase-que-ta-o-curintia.mp3")
        print("Local da musica", pathMusic)

        url = QUrl.fromLocalFile(pathMusic)

        if url.isValid():
            self.player.setMedia(QMediaContent(url))
            self.player.play()
            print("Tocando música...💃")
        else:
            print("Erro: Caminho do arquivo inválido!")

    def Parar(self):
        self.player.stop()
        self.isPaused = False
        print("Musica parada!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Reprodutor()
    mainWindow.show()
    sys.exit(app.exec_())