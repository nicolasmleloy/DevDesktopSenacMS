import sys
import os
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QAction, QWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from EscolherMusica import Ui_MainWindow


class EscolherMusica(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.player = QMediaPlayer(self)
        self.ui.btn_play.clicked.connect(self.Play)
        self.ui.btn_parar.clicked.connect(self.Parar)
        self.ui.btn_pause.clicked.connect(self.Pausar)
        self.ui.volume.sliderMoved.connect(self.controlarVolume)
        self.isPaused = False
    
    def Play(self):
        resposta = self.ui.input.text()
        musica = ""
        opcoes = ["1", "2", "3", "4", "5"]

        if(resposta in opcoes):
            self.ui.msg_erro.setText("")
            if(self.isPaused):
                self.player.play()
                self.isPaused = False
            else:
                if(resposta == "1"):
                    pathMusic = os.path.abspath("./Musicas/pelados_em_santos.mp3")
                    musica = "Pelados em Santos"
                elif(resposta == "2"):
                    pathMusic = os.path.abspath("./Musicas/roda_roda_vira.mp3")
                    musica = "Roda roda vira"
                elif(resposta == "3"):
                    pathMusic = os.path.abspath("./Musicas/jennifer.mp3")
                    musica = "Jennifer"
                elif(resposta == "4"):
                    pathMusic = os.path.abspath("./Musicas/descer_pra_bc.mp3")
                    musica = "Descer pra BC"
                elif(resposta == "5"):
                    pathMusic = os.path.abspath("./Musicas/descer_pra_cg.mp3")
                    musica = "Descer pra CG"
                else:
                    print("Valor inválido!")

                print("Local da musica", pathMusic)

                url = QUrl.fromLocalFile(pathMusic)

                if url.isValid():
                    self.player.setMedia(QMediaContent(url))
                    self.player.play()
                    print(f"Tocando música: {musica}🔊")
                else:
                    print("Erro: Caminho do arquivo inválido!")
        else:
            self.ui.msg_erro.setText("Opção inválida!")


    def Parar(self):
        self.player.stop()
        self.isPaused = False
        print("Musica parada!❌")

    def Pausar(self):
        self.player.pause()
        self.isPaused = True
        print("Musica pausada!▶")

    def controlarVolume(self):
        alturaSom = self.ui.volume.value()
        self.player.setVolume(alturaSom)
        print(f"Volume ajustado para: {alturaSom}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = EscolherMusica()
    mainWindow.show()
    sys.exit(app.exec_())