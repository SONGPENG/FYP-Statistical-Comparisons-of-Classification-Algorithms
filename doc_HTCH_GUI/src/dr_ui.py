# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dr.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DrWindow(object):
    def setupUi(self, DrWindow):
        DrWindow.setObjectName("DrWindow")
        DrWindow.resize(739, 438)
        self.centralwidget = QtWidgets.QWidget(DrWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_file = QtWidgets.QFrame(self.centralwidget)
        self.frame_file.setGeometry(QtCore.QRect(20, 20, 441, 151))
        self.frame_file.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_file.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_file.setObjectName("frame_file")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame_file)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 421, 71))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_file = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_file.setContentsMargins(0, 0, 0, 0)
        self.formLayout_file.setObjectName("formLayout_file")
        self.lineEdit_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_input.setObjectName("lineEdit_input")
        self.formLayout_file.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_input)
        self.lineEdit_output = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_output.setObjectName("lineEdit_output")
        self.formLayout_file.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_output)
        self.pbt_input = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pbt_input.setObjectName("pbt_input")
        self.formLayout_file.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pbt_input)
        self.pbt_output = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pbt_output.setObjectName("pbt_output")
        self.formLayout_file.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pbt_output)
        self.line_h1 = QtWidgets.QFrame(self.frame_file)
        self.line_h1.setGeometry(QtCore.QRect(0, 130, 441, 20))
        self.line_h1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_h1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_h1.setObjectName("line_h1")
        self.pbt_clear = QtWidgets.QPushButton(self.frame_file)
        self.pbt_clear.setGeometry(QtCore.QRect(340, 100, 93, 28))
        self.pbt_clear.setObjectName("pbt_clear")
        self.frame_choose_method = QtWidgets.QFrame(self.centralwidget)
        self.frame_choose_method.setGeometry(QtCore.QRect(20, 170, 441, 201))
        self.frame_choose_method.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_choose_method.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_choose_method.setObjectName("frame_choose_method")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame_choose_method)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 421, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_method = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_method.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_method.setObjectName("gridLayout_method")
        self.pbt_ae = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pbt_ae.setObjectName("pushButton")
        self.gridLayout_method.addWidget(self.pbt_ae, 0, 0, 1, 1)
        self.pbt_le = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pbt_le.setObjectName("pushButton_5")
        self.gridLayout_method.addWidget(self.pbt_le, 0, 2, 1, 1)
        self.pbt_lpp = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pbt_lpp.setObjectName("pushButton_3")
        self.gridLayout_method.addWidget(self.pbt_lpp, 1, 0, 1, 1)
        self.pbt_mds = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pbt_mds.setObjectName("pushButton_4")
        self.gridLayout_method.addWidget(self.pbt_mds, 1, 1, 1, 1)
        self.pbt_pca = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pbt_pca.setObjectName("pushButton_6")
        self.gridLayout_method.addWidget(self.pbt_pca, 1, 2, 1, 1)
        self.pbt_lda = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pbt_lda.setObjectName("pushButton_2")
        self.gridLayout_method.addWidget(self.pbt_lda, 0, 1, 1, 1)
        self.pbt_tsne = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pbt_tsne.setObjectName("pushButton_7")
        self.gridLayout_method.addWidget(self.pbt_tsne, 2, 0, 1, 1)
        self.label_method = QtWidgets.QLabel(self.frame_choose_method)
        self.label_method.setGeometry(QtCore.QRect(10, 10, 141, 16))
        self.label_method.setObjectName("label_method")
        self.label_des = QtWidgets.QLabel(self.centralwidget)
        self.label_des.setGeometry(QtCore.QRect(490, 30, 121, 21))
        self.label_des.setObjectName("label_des")
        self.textEdit_des = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_des.setGeometry(QtCore.QRect(490, 60, 211, 291))
        self.textEdit_des.setObjectName("textEdit_des")
        self.line_v1 = QtWidgets.QFrame(self.centralwidget)
        self.line_v1.setGeometry(QtCore.QRect(460, 20, 20, 341))
        self.line_v1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_v1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_v1.setObjectName("line_v1")
        DrWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DrWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 739, 26))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        DrWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DrWindow)
        self.statusbar.setObjectName("statusbar")
        DrWindow.setStatusBar(self.statusbar)
        self.actionopen = QtWidgets.QAction(DrWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionexit = QtWidgets.QAction(DrWindow)
        self.actionexit.setObjectName("actionexit")
        self.actionHTC_Homepage = QtWidgets.QAction(DrWindow)
        self.actionHTC_Homepage.setObjectName("actionHTC_Homepage")
        self.actionfile_format = QtWidgets.QAction(DrWindow)
        self.actionfile_format.setObjectName("actionfile_format")
        self.menufile.addAction(self.actionopen)
        self.menufile.addSeparator()
        self.menufile.addAction(self.actionexit)
        self.menuhelp.addAction(self.actionHTC_Homepage)
        self.menuhelp.addSeparator()
        self.menuhelp.addAction(self.actionfile_format)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(DrWindow)
        QtCore.QMetaObject.connectSlotsByName(DrWindow)

    def retranslateUi(self, DrWindow):
        _translate = QtCore.QCoreApplication.translate
        DrWindow.setWindowTitle(_translate("DrWindow", "MainWindow"))
        self.pbt_input.setText(_translate("DrWindow", "Input:"))
        self.pbt_output.setText(_translate("DrWindow", "Output:"))
        self.pbt_clear.setText(_translate("DrWindow", "clear"))
        self.pbt_ae.setText(_translate("DrWindow", "Auto Encoder"))
        self.pbt_le.setText(_translate("DrWindow", "LE"))
        self.pbt_lpp.setText(_translate("DrWindow", "LPP"))
        self.pbt_mds.setText(_translate("DrWindow", "MDS"))
        self.pbt_pca.setText(_translate("DrWindow", "PCA"))
        self.pbt_lda.setText(_translate("DrWindow", "LDA"))
        self.pbt_tsne.setText(_translate("DrWindow", "t-SNE"))
        self.label_method.setText(_translate("DrWindow", "Reduction Method:"))
        self.label_des.setText(_translate("DrWindow", "Descriptions"))
        self.menufile.setTitle(_translate("DrWindow", "File"))
        self.menuhelp.setTitle(_translate("DrWindow", "Help"))
        self.actionopen.setText(_translate("DrWindow", "open"))
        self.actionexit.setText(_translate("DrWindow", "exit"))
        self.actionHTC_Homepage.setText(_translate("DrWindow", "HTC Homepage"))
        self.actionfile_format.setText(_translate("DrWindow", "file format"))