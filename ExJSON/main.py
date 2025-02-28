import sys
import json
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QAction, QWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from ExJSON import Ui_MainWindow

class ExJSON(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnSair.clicked.connect(self.close)
        self.ui.btnNovoJogo.clicked.connect(self.novoJogo)
        self.ui.btnSalvar.clicked.connect(self.salvarJogo)
        # self.ui.btnCarregar.clicked.connect(self.carregarJogo)

    def novoJogo(self): 
        self.ui.nome.clear()
        self.ui.idade.clear()
        self.ui.altura.clear()

        self.ui.masculino.setChecked(False)
        self.ui.feminino.setChecked(False)

        self.ui.dtNasc.setDate(QtCore.QDate.currentDate())

        QtWidgets.QMessageBox.information(self, "Novo Jogo", "Novo jogo iniciado!")
    
    def salvarJogo(self):
        data = {
            "nome": self.ui.nome.text(),
            "dataNascimento": self.ui.dtNasc.date().toString("yyyy-MM-dd"),
            "idade": self.ui.idade.text(),
            "altura": self.ui.altura.text(),
            "sexo": "Feminino" 
            if self.ui.feminino.isChecked()
            else "Masculino" if self.ui.masculino.isChecked()
            else "Não informado"
        }

        filePath = QtWidgets.QFileDialog.getSaveFileName(self, "Salvar Jogo", "", data, "Arquivos JSON (*json)")

        if(filePath):
            try:
                if not filePath.endswith('.json'):
                    filePath += '.json'
                
                with open(filePath, "w", encoding="utf-8") as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)

                QtWidgets.QMessageBox.information(self, "sucesso", "Jogo salvo com sucesso!")

            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao salvar o jogo: {e}")
        else:
            QtWidgets.QMessageBox.warning(self, "Erro", "Nenhum arquivo selecionado!")
                
    
    def carregarJogo(self):
        filePath = QtWidgets.QFileDialog.getSaveFileName(self, "Carregar Jogo", "", data, "Arquivos JSON (*json)")

        if filePath:
            try:
                with open(filePath, "r", encoding="utf-8") as file:
                    data = json.load(file)

                    self.ui.nome.setText(data.get("nome", ""))
                    self.ui.dtNasc.setDate(QtCore.QDate.fromString(data.get("dataNascimento", "2000-01-01"), "yyyy-MM-dd"))
                    self.ui.idade.setText(data.get("idade", ""))
                    self.ui.altura.setText(data.get("altura", ""))

                    if(data.get("sexo") == "Feminino"):
                        self.ui.feminino.setChecked(True)
                    elif(data.get("sexo") == "Masculino"):
                        self.ui.masculino.setChecked(True)
                    else:
                        self.ui.feminino.setChecked(False)
                        self.ui.masculino.setChecked(False)

                QtWidgets.QMessageBox.information(self, "Sucesso", "Jogo carregado com sucesso!")

            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Erro", f"Erro ao carregar o jogo: {e}")
        else:
            QtWidgets.QMessageBox.warning(self, "Erro", "Nenhum arquivo selecionado!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = ExJSON()
    mainWindow.show()
    sys.exit(app.exec_())