# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listaDeMetas.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(170, 30, 491, 471))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.adicionar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.adicionar.setStyleSheet("background-color: rgb(49, 132, 13);\n"
"color: white;")
        self.adicionar.setObjectName("adicionar")
        self.gridLayout.addWidget(self.adicionar, 4, 0, 1, 1)
        self.remover = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.remover.setStyleSheet("background-color: rgb(255, 42, 42);\n"
"color: white;")
        self.remover.setObjectName("remover")
        self.gridLayout.addWidget(self.remover, 4, 1, 1, 1)
        self.listaDeMetas = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.listaDeMetas.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.listaDeMetas.setObjectName("listaDeMetas")
        item = QtWidgets.QListWidgetItem()
        self.listaDeMetas.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listaDeMetas.addItem(item)
        self.gridLayout.addWidget(self.listaDeMetas, 1, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)
        self.inputMeta = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.inputMeta.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inputMeta.setObjectName("inputMeta")
        self.gridLayout.addWidget(self.inputMeta, 3, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setObjectName("menuArquivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNovo = QtWidgets.QAction(MainWindow)
        self.actionNovo.setObjectName("actionNovo")
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionSalvar = QtWidgets.QAction(MainWindow)
        self.actionSalvar.setObjectName("actionSalvar")
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.menuArquivo.addAction(self.actionNovo)
        self.menuArquivo.addAction(self.actionAbrir)
        self.menuArquivo.addAction(self.actionSalvar)
        self.menuArquivo.addAction(self.actionSair)
        self.menubar.addAction(self.menuArquivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.adicionar.setText(_translate("MainWindow", "Adicionar"))
        self.remover.setText(_translate("MainWindow", "Remover"))
        __sortingEnabled = self.listaDeMetas.isSortingEnabled()
        self.listaDeMetas.setSortingEnabled(False)
        item = self.listaDeMetas.item(0)
        item.setText(_translate("MainWindow", "Estudar"))
        item = self.listaDeMetas.item(1)
        item.setText(_translate("MainWindow", "Ler livros"))
        self.listaDeMetas.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("MainWindow", "Digite uma nova meta:"))
        self.label.setText(_translate("MainWindow", "Lista de Metas para 2025"))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))
        self.actionNovo.setText(_translate("MainWindow", "Novo"))
        self.actionNovo.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir"))
        self.actionAbrir.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionSalvar.setText(_translate("MainWindow", "Salvar"))
        self.actionSalvar.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))
        self.actionSair.setShortcut(_translate("MainWindow", "Esc"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
