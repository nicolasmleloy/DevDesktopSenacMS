# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lojaDeTinta.ui'
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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 20, 496, 39))
        self.label.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.metrosQuadrados = QtWidgets.QLineEdit(self.centralwidget)
        self.metrosQuadrados.setGeometry(QtCore.QRect(320, 70, 161, 51))
        self.metrosQuadrados.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"color: gray;")
        self.metrosQuadrados.setObjectName("metrosQuadrados")
        self.btnCalcular = QtWidgets.QPushButton(self.centralwidget)
        self.btnCalcular.setGeometry(QtCore.QRect(364, 140, 75, 23))
        self.btnCalcular.setObjectName("btnCalcular")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 200, 801, 141))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.resultado = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.resultado.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: green;")
        self.resultado.setText("")
        self.resultado.setObjectName("resultado")
        self.horizontalLayout.addWidget(self.resultado)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Informe quantos m2 deseja pintar:"))
        self.btnCalcular.setText(_translate("MainWindow", "Calcular"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
