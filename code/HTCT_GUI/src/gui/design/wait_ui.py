# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wait.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WaitWindow(object):
    def setupUi(self, WaitWindow):
        WaitWindow.setObjectName("WaitWindow")
        WaitWindow.setFixedSize(435, 410)
        self.centralwidget = QtWidgets.QWidget(WaitWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit_notice = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_notice.setGeometry(QtCore.QRect(30, 40, 371, 281))
        self.textEdit_notice.setObjectName("textEdit_notice")
        WaitWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WaitWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 433, 26))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        WaitWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WaitWindow)
        self.statusbar.setObjectName("statusbar")
        WaitWindow.setStatusBar(self.statusbar)
        self.actionHTC_homepage = QtWidgets.QAction(WaitWindow)
        self.actionHTC_homepage.setObjectName("actionHTC_homepage")
        self.actioncontact = QtWidgets.QAction(WaitWindow)
        self.actioncontact.setObjectName("actioncontact")
        self.actionexit = QtWidgets.QAction(WaitWindow)
        self.actionexit.setObjectName("actionexit")
        self.menuHelp.addAction(self.actionHTC_homepage)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actioncontact)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionexit)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(WaitWindow)
        QtCore.QMetaObject.connectSlotsByName(WaitWindow)

    def retranslateUi(self, WaitWindow):
        _translate = QtCore.QCoreApplication.translate
        WaitWindow.setWindowTitle(_translate("WaitWindow", "notice"))
        self.menuHelp.setTitle(_translate("WaitWindow", "Help"))
        self.actionHTC_homepage.setText(_translate("WaitWindow", "HTC homepage"))
        self.actioncontact.setText(_translate("WaitWindow", "contact"))
        self.actionexit.setText(_translate("WaitWindow", "exit"))
