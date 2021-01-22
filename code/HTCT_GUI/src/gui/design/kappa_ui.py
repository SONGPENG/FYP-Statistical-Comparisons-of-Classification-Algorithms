# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kappa.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KappaWindow(object):
    def setupUi(self, KappaWindow):
        KappaWindow.setObjectName("KappaWindow")
        KappaWindow.setFixedSize(490, 470)
        self.centralwidget = QtWidgets.QWidget(KappaWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_fp = QtWidgets.QLabel(self.centralwidget)
        self.label_fp.setGeometry(QtCore.QRect(37, 30, 81, 15))
        self.label_fp.setObjectName("label_fp")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 30, 311, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.line_h1_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_h1_2.setGeometry(QtCore.QRect(30, 100, 401, 16))
        self.line_h1_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_h1_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_h1_2.setObjectName("line_h1_2")
        self.frame_tr = QtWidgets.QFrame(self.centralwidget)
        self.frame_tr.setGeometry(QtCore.QRect(20, 120, 411, 281))
        self.frame_tr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_tr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_tr.setObjectName("frame_tr")
        self.label_tr = QtWidgets.QLabel(self.frame_tr)
        self.label_tr.setGeometry(QtCore.QRect(10, 10, 131, 21))
        self.label_tr.setObjectName("label_tr")
        self.textEdit_result = QtWidgets.QTextEdit(self.frame_tr)
        self.textEdit_result.setGeometry(QtCore.QRect(10, 30, 401, 241))
        self.textEdit_result.setObjectName("textEdit_result")
        self.pbt_clear = QtWidgets.QPushButton(self.frame_tr)
        self.pbt_clear.setGeometry(QtCore.QRect(220, 390, 93, 28))
        self.pbt_clear.setObjectName("pbt_clear")
        self.pbt_kappa = QtWidgets.QPushButton(self.centralwidget)
        self.pbt_kappa.setGeometry(QtCore.QRect(340, 70, 93, 28))
        self.pbt_kappa.setObjectName("pbt_kappa")
        self.pbt_clear_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pbt_clear_2.setGeometry(QtCore.QRect(230, 70, 93, 28))
        self.pbt_clear_2.setObjectName("pbt_clear_2")
        KappaWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(KappaWindow)
        self.statusbar.setObjectName("statusbar")
        KappaWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(KappaWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 491, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        KappaWindow.setMenuBar(self.menuBar)
        self.actionopen = QtWidgets.QAction(KappaWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionexit = QtWidgets.QAction(KappaWindow)
        self.actionexit.setObjectName("actionexit")
        self.menuFile.addAction(self.actionopen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionexit)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(KappaWindow)
        QtCore.QMetaObject.connectSlotsByName(KappaWindow)

    def retranslateUi(self, KappaWindow):
        _translate = QtCore.QCoreApplication.translate
        KappaWindow.setWindowTitle(_translate("KappaWindow", "Cohen’s kappa"))
        self.label_fp.setText(_translate("KappaWindow", "File Path:"))
        self.label_tr.setText(_translate("KappaWindow", "Result: "))
        self.pbt_clear.setText(_translate("KappaWindow", "clear"))
        self.pbt_kappa.setText(_translate("KappaWindow", "calculate"))
        self.pbt_clear_2.setText(_translate("KappaWindow", "clera"))
        self.menuFile.setTitle(_translate("KappaWindow", "File"))
        self.actionopen.setText(_translate("KappaWindow", "open"))
        self.actionexit.setText(_translate("KappaWindow", "exit"))
