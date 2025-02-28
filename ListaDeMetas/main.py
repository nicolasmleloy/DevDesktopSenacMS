import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidgetItem, QFileDialog, QAction, QWidget
from listaDeMetas import Ui_MainWindow 

class ListaDeMetas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.adicionar.clicked.connect(self.adicionarMeta)
        self.ui.remover.clicked.connect(self.removerMeta)

        self.ui.actionNovo.triggered.connect(self.novo_arquivo)
        self.ui.actionAbrir.triggered.connect(self.abrir_arquivo)
        self.ui.actionSalvar.triggered.connect(self.salvar_arquivo)
        self.ui.actionSair.triggered.connect(self.close)

    def adicionarMeta(self):
        meta = self.ui.inputMeta.text()
        if(meta):
            item = QListWidgetItem(meta)

            self.ui.listaDeMetas.addItem(item)
            item.setCheckState(0)

            self.ui.inputMeta.clear()

    def removerMeta(self):
        itemSelecionado = self.ui.listaDeMetas.currentRow()
        if(itemSelecionado >= 0):
            self.ui.listaDeMetas.takeItem(itemSelecionado)

    def novo_arquivo(self):
        self.ui.listaDeMetas.clear()

    def abrir_arquivo(self):
        caminho = QFileDialog.getOpenFileName(self, "Abrir Arquivo", "", "Text Files (*.txt)")[0]
        if caminho:
            with open(caminho, 'r', encoding='utf-8') as f:
                metas = f.readlines()
                self.ui.listaDeMetas.clear()
                for meta in metas:
                    item = meta.strip()
                    item.setCheckState(0)
                    self.ui.listaDeMetas.addItem(item)
                    
    def salvar_arquivo(self):
        caminho = QFileDialog.getSaveFileName(self, "Salvar Arquivo", "", "Text Files (*.txt)")[0]
        if caminho:
            with open(caminho, 'w', encoding='utf-8') as f:
                for i in range(self.ui.listaDeMetas.count()):
                    item = self.ui.listaDeMetas.item(i)
                    f.write(item.text() + '\n')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = ListaDeMetas()
    mainWindow.show()
    sys.exit(app.exec_())