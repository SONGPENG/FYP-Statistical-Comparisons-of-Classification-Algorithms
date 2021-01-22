# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aar_t.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AarWindow(object):
    def setupUi(self, Aar_tWindow):
        """

        :param Aar_tWindow:
        :return:
        """
        Aar_tWindow.setObjectName("Aar_tWindow")
        Aar_tWindow.setFixedSize(485, 435)
        self.centralwidget = QtWidgets.QWidget(Aar_tWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_file = QtWidgets.QFrame(self.centralwidget)
        self.frame_file.setGeometry(QtCore.QRect(20, 10, 441, 111))
        self.frame_file.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_file.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_file.setObjectName("frame_file")

        self.formLayoutWidget = QtWidgets.QWidget(self.frame_file)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 421, 80))
        self.formLayoutWidget.setObjectName("formLayoutWidget")

        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.lineEdit_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_input.setObjectName("lineEdit_input")

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_input)
        self.lineEdit_output = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_output.setObjectName("lineEdit_output")

        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_output)
        self.pbt_input = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pbt_input.setObjectName("pbt_input")

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pbt_input)
        self.pbt_output = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pbt_output.setObjectName("pbt_output")

        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pbt_output)
        self.frame_dt = QtWidgets.QFrame(self.centralwidget)
        self.frame_dt.setGeometry(QtCore.QRect(20, 120, 211, 80))
        self.frame_dt.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_dt.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dt.setObjectName("frame_dt")

        self.layoutWidget = QtWidgets.QWidget(self.frame_dt)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 133, 69))
        self.layoutWidget.setObjectName("layoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_dt = QtWidgets.QLabel(self.layoutWidget)

        self.label_dt.setObjectName("label_dt")
        self.verticalLayout.addWidget(self.label_dt)

        self.rbt_ar = QtWidgets.QRadioButton(self.layoutWidget)
        self.rbt_ar.setObjectName("rbt_ar")
        self.verticalLayout.addWidget(self.rbt_ar)

        self.rbt_er = QtWidgets.QRadioButton(self.layoutWidget)
        self.rbt_er.setObjectName("rbt_er")

        self.verticalLayout.addWidget(self.rbt_er)

        self.frame_plot = QtWidgets.QFrame(self.centralwidget)
        self.frame_plot.setGeometry(QtCore.QRect(230, 120, 231, 81))
        self.frame_plot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_plot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_plot.setObjectName("frame_plot")

        self.pbt_plot = QtWidgets.QPushButton(self.frame_plot)
        self.pbt_plot.setGeometry(QtCore.QRect(130, 50, 93, 28))
        self.pbt_plot.setObjectName("pbt_plot")

        self.pbt_clear = QtWidgets.QPushButton(self.frame_plot)
        self.pbt_clear.setGeometry(QtCore.QRect(10, 50, 93, 28))
        self.pbt_clear.setObjectName("pbt_clear")

        self.line_h1 = QtWidgets.QFrame(self.centralwidget)
        self.line_h1.setGeometry(QtCore.QRect(20, 203, 441, 20))
        self.line_h1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_h1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_h1.setObjectName("line_h1")

        self.label_des = QtWidgets.QLabel(self.centralwidget)
        self.label_des.setGeometry(QtCore.QRect(30, 220, 121, 21))
        self.label_des.setObjectName("label_des")

        self.textEdit_des = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_des.setGeometry(QtCore.QRect(20, 250, 441, 111))
        self.textEdit_des.setObjectName("textEdit_des")

        Aar_tWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Aar_tWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 484, 26))
        self.menubar.setObjectName("menubar")

        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")

        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        Aar_tWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(Aar_tWindow)
        self.statusbar.setObjectName("statusbar")

        Aar_tWindow.setStatusBar(self.statusbar)
        self.actionopen = QtWidgets.QAction(Aar_tWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionexit = QtWidgets.QAction(Aar_tWindow)
        self.actionexit.setObjectName("actionexit")

        self.actionHTC_Homepage = QtWidgets.QAction(Aar_tWindow)
        self.actionHTC_Homepage.setObjectName("actionHTC_Homepage")
        self.actionstyle_requirement = QtWidgets.QAction(Aar_tWindow)
        self.actionstyle_requirement.setObjectName("actionstyle_requirement")

        self.menufile.addAction(self.actionopen)
        self.menufile.addSeparator()
        self.menufile.addAction(self.actionexit)

        self.menuhelp.addAction(self.actionHTC_Homepage)
        self.menuhelp.addSeparator()
        self.menuhelp.addAction(self.actionstyle_requirement)

        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(Aar_tWindow)
        QtCore.QMetaObject.connectSlotsByName(Aar_tWindow)

    def retranslateUi(self, Aar_tWindow):
        """

        :param Aar_tWindow:
        :return:
        """
        _translate = QtCore.QCoreApplication.translate
        Aar_tWindow.setWindowTitle(_translate("Aar_tWindow", "plot: average accuracy rate "))
        self.pbt_input.setText(_translate("Aar_tWindow", "Input:"))
        self.pbt_output.setText(_translate("Aar_tWindow", "Output:"))
        self.label_dt.setText(_translate("Aar_tWindow", "Data Type:"))
        self.rbt_ar.setText(_translate("Aar_tWindow", "accuracy rate"))
        self.rbt_er.setText(_translate("Aar_tWindow", "error rate"))
        self.pbt_plot.setText(_translate("Aar_tWindow", "plot"))
        self.pbt_clear.setText(_translate("Aar_tWindow", "clear"))
        self.label_des.setText(_translate("Aar_tWindow", "Descriptions:"))
        self.menufile.setTitle(_translate("Aar_tWindow", "File"))
        self.menuhelp.setTitle(_translate("Aar_tWindow", "Help"))
        self.actionopen.setText(_translate("Aar_tWindow", "open"))
        self.actionexit.setText(_translate("Aar_tWindow", "exit"))
        self.actionHTC_Homepage.setText(_translate("Aar_tWindow", "HTC Homepage"))
        self.actionstyle_requirement.setText(_translate("Aar_tWindow", "style requirements"))
