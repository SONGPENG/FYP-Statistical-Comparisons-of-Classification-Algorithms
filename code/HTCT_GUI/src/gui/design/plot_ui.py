# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plot.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PlotWindow(object):
    def setupUi(self, PlotWindow):
        PlotWindow.setObjectName("PlotWindow")
        PlotWindow.setFixedSize(575, 450)
        self.centralwidget = QtWidgets.QWidget(PlotWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.framediagram = QtWidgets.QFrame(self.centralwidget)
        self.framediagram.setGeometry(QtCore.QRect(20, 20, 251, 371))
        self.framediagram.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framediagram.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framediagram.setObjectName("framediagram")
        self.label_cdt = QtWidgets.QLabel(self.framediagram)
        self.label_cdt.setGeometry(QtCore.QRect(0, 0, 171, 30))
        self.label_cdt.setObjectName("label_cdt")
        self.line_h1 = QtWidgets.QFrame(self.framediagram)
        self.line_h1.setGeometry(QtCore.QRect(0, 20, 161, 16))
        self.line_h1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_h1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_h1.setObjectName("line_h1")
        self.layoutWidget = QtWidgets.QWidget(self.framediagram)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 211, 311))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_dragram = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_dragram.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_dragram.setObjectName("gridLayout_dragram")
        self.pbt_tss = QtWidgets.QPushButton(self.layoutWidget)
        self.pbt_tss.setObjectName("pbt_tss")
        self.gridLayout_dragram.addWidget(self.pbt_tss, 5, 0, 1, 1)
        self.pbt_cd = QtWidgets.QPushButton(self.layoutWidget)
        self.pbt_cd.setObjectName("pbt_cd")
        self.gridLayout_dragram.addWidget(self.pbt_cd, 2, 0, 1, 1)
        self.pbt_roc = QtWidgets.QPushButton(self.layoutWidget)
        self.pbt_roc.setObjectName("pbt_roc")
        self.gridLayout_dragram.addWidget(self.pbt_roc, 3, 0, 1, 1)
        self.pbt_kappa = QtWidgets.QPushButton(self.layoutWidget)
        self.pbt_kappa.setObjectName("pbt_kappa")
        self.gridLayout_dragram.addWidget(self.pbt_kappa, 6, 0, 1, 1)
        self.pbt_aar = QtWidgets.QPushButton(self.layoutWidget)
        self.pbt_aar.setObjectName("pbt_aar")
        self.gridLayout_dragram.addWidget(self.pbt_aar, 0, 0, 1, 1)
        self.pbt_art = QtWidgets.QPushButton(self.layoutWidget)
        self.pbt_art.setObjectName("pbt_art")
        self.gridLayout_dragram.addWidget(self.pbt_art, 1, 0, 1, 1)
        self.pbt_cc = QtWidgets.QPushButton(self.layoutWidget)
        self.pbt_cc.setObjectName("pbt_cc")
        self.gridLayout_dragram.addWidget(self.pbt_cc, 4, 0, 1, 1)
        self.pbt_rmse = QtWidgets.QPushButton(self.layoutWidget)
        self.pbt_rmse.setObjectName("pbt_rmse")
        self.gridLayout_dragram.addWidget(self.pbt_rmse, 7, 0, 1, 1)
        self.frame_note = QtWidgets.QFrame(self.centralwidget)
        self.frame_note.setGeometry(QtCore.QRect(290, 20, 251, 371))
        self.frame_note.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_note.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_note.setObjectName("frame_note")
        self.textEdit_note = QtWidgets.QTextEdit(self.frame_note)
        self.textEdit_note.setGeometry(QtCore.QRect(10, 40, 221, 311))
        self.textEdit_note.setObjectName("textEdit_note")
        self.label_note = QtWidgets.QLabel(self.frame_note)
        self.label_note.setGeometry(QtCore.QRect(10, 10, 72, 15))
        self.label_note.setObjectName("label_note")
        self.line_h3 = QtWidgets.QFrame(self.frame_note)
        self.line_h3.setGeometry(QtCore.QRect(10, 20, 41, 16))
        self.line_h3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_h3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_h3.setObjectName("line_h3")
        self.line_v3 = QtWidgets.QFrame(self.centralwidget)
        self.line_v3.setGeometry(QtCore.QRect(263, 20, 20, 351))
        self.line_v3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_v3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_v3.setObjectName("line_v3")
        PlotWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PlotWindow)
        self.statusbar.setObjectName("statusbar")
        PlotWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(PlotWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 574, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        PlotWindow.setMenuBar(self.menuBar)
        self.actionopen = QtWidgets.QAction(PlotWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionexit = QtWidgets.QAction(PlotWindow)
        self.actionexit.setObjectName("actionexit")
        self.menuFile.addAction(self.actionopen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionexit)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(PlotWindow)
        QtCore.QMetaObject.connectSlotsByName(PlotWindow)

    def retranslateUi(self, PlotWindow):
        _translate = QtCore.QCoreApplication.translate
        PlotWindow.setWindowTitle(_translate("PlotWindow", "generic performance metrics"))
        self.label_cdt.setText(_translate("PlotWindow", "Select Diagram Type:"))
        self.pbt_tss.setText(_translate("PlotWindow", "Texas Sharpshooter"))
        self.pbt_cd.setText(_translate("PlotWindow", "Critical Distance"))
        self.pbt_roc.setText(_translate("PlotWindow", "ROC"))
        self.pbt_kappa.setText(_translate("PlotWindow", "Cohen Kappa"))
        self.pbt_aar.setText(_translate("PlotWindow", "Average Accuracy Rate"))
        self.pbt_art.setText(_translate("PlotWindow", "Average Running Time"))
        self.pbt_cc.setText(_translate("PlotWindow", "Classifiers Comparsion"))
        self.pbt_rmse.setText(_translate("PlotWindow", "RMSE"))
        self.label_note.setText(_translate("PlotWindow", "Note:"))
        self.menuFile.setTitle(_translate("PlotWindow", "File"))
        self.actionopen.setText(_translate("PlotWindow", "open"))
        self.actionexit.setText(_translate("PlotWindow", "exit"))
