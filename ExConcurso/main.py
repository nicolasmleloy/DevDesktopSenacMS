import sys
import json
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QAction, QWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from ExConcurso import Ui_MainWindow

class ExConcurso(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnCalcular.clicked.connect(self.Calcular)
        self.ui.btnSalvar.clicked.connect(self.Salvar)
        self.ui.btnLimparCampos.clicked.connect(self.LimparCampos)

    def Calcular(self):
        portugues = int(self.ui.notaPortugues.text()) * 2
        matematica = int(self.ui.notaMatematica.text()) * 2
        conGerais = int(self.ui.notaConGerais.text()) * 2
        conEspec = int(self.ui.notaConEspec.text()) * 2

        soma = (portugues + matematica + conGerais + conEspec)
        media = (portugues + matematica + conGerais + conEspec) / 2

        QtWidgets.QMessageBox.information(self, "Resultado", f"""CPF {self.ui.cpf.text()}:
        \nSoma: {soma}/200 pontos.
        \nMédia: {media} pontos.
        \nPortuguês: {portugues}/40 pontos
        \nMatemática: {matematica}/40 pontos
        \nConhecimentos Gerais: {conGerais}/20 pontos
        \nConhecimentos Específicos: {conEspec}/100 pontos""")


    def Salvar(self):
        dados_novos = {
            "cpf": self.ui.cpf.text(),
            "portugues": self.ui.notaPortugues.text(),
            "matematica": self.ui.notaMatematica.text(),
            "conGerais": self.ui.notaConGerais.text(),
            "conEspec": self.ui.notaConEspec.text()
        }

        filePath, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Salvar notas", "", "Arquivos JSON (*.json)")

        if filePath:
            try:
                if not filePath.endswith('.json'):
                    filePath += '.json'
                
                try:
                    with open(filePath, "r", encoding="utf-8") as file:
                        dados_existentes = json.load(file)
                    
                    if not isinstance(dados_existentes, list):
                        dados_existentes = [dados_existentes]
                except (FileNotFoundError, json.JSONDecodeError):
                    dados_existentes = []  
                
                dados_existentes.append(dados_novos)

                with open(filePath, "w", encoding="utf-8") as file:
                    json.dump(dados_existentes, file, ensure_ascii=False, indent=4)

                QtWidgets.QMessageBox.information(self, "Sucesso", "Notas salvas com sucesso!")
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao salvar as notas: {e}")
        else:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Nenhum arquivo foi selecionado!")


    def LimparCampos(self):
        self.ui.cpf.clear()
        self.ui.notaPortugues.clear()
        self.ui.notaMatematica.clear()
        self.ui.notaConGerais.clear()
        self.ui.notaConEspec.clear()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = ExConcurso()
    mainWindow.show()
    sys.exit(app.exec_())