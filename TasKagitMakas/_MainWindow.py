# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_Mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(406, 456)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnpick = QtWidgets.QPushButton(self.centralwidget)
        self.btnpick.setGeometry(QtCore.QRect(120, 230, 111, 71))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(13)
        self.btnpick.setFont(font)
        self.btnpick.setObjectName("btnpick")
        self.lblmyscore = QtWidgets.QLabel(self.centralwidget)
        self.lblmyscore.setGeometry(QtCore.QRect(40, 80, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lblmyscore.setFont(font)
        self.lblmyscore.setText("")
        self.lblmyscore.setObjectName("lblmyscore")
        self.lblscore = QtWidgets.QLabel(self.centralwidget)
        self.lblscore.setGeometry(QtCore.QRect(130, 30, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lblscore.setFont(font)
        self.lblscore.setObjectName("lblscore")
        self.lblhimscore = QtWidgets.QLabel(self.centralwidget)
        self.lblhimscore.setGeometry(QtCore.QRect(260, 80, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lblhimscore.setFont(font)
        self.lblhimscore.setText("")
        self.lblhimscore.setObjectName("lblhimscore")
        self.txtmychoice = QtWidgets.QLineEdit(self.centralwidget)
        self.txtmychoice.setGeometry(QtCore.QRect(10, 120, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.txtmychoice.setFont(font)
        self.txtmychoice.setReadOnly(True)
        self.txtmychoice.setObjectName("txtmychoice")
        self.txthimchoice = QtWidgets.QLineEdit(self.centralwidget)
        self.txthimchoice.setGeometry(QtCore.QRect(230, 120, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.txthimchoice.setFont(font)
        self.txthimchoice.setReadOnly(True)
        self.txthimchoice.setObjectName("txthimchoice")
        self.cbpick = QtWidgets.QComboBox(self.centralwidget)
        self.cbpick.setGeometry(QtCore.QRect(120, 190, 111, 22))
        self.cbpick.setObjectName("cbpick")
        self.cbpick.addItem("")
        self.cbpick.addItem("")
        self.cbpick.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 406, 21))
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
        self.btnpick.setText(_translate("MainWindow", "SEÇ"))
        self.lblscore.setText(_translate("MainWindow", "SCOREBOARD"))
        self.cbpick.setItemText(0, _translate("MainWindow", "Taş"))
        self.cbpick.setItemText(1, _translate("MainWindow", "Kağıt"))
        self.cbpick.setItemText(2, _translate("MainWindow", "Makas"))
