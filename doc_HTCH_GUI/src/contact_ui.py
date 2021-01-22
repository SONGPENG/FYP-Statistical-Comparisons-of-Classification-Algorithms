# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contact.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ContactWindow(object):
    def setupUi(self, ContactWindow):
        ContactWindow.setObjectName("ContactWindow")
        ContactWindow.setFixedSize(400, 510)
        self.centralwidget = QtWidgets.QWidget(ContactWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 330, 391, 141))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_infor5 = QtWidgets.QLabel(self.frame)
        self.label_infor5.setGeometry(QtCore.QRect(10, 110, 121, 16))
        self.label_infor5.setObjectName("label_infor5")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_infor1 = QtWidgets.QLabel(self.layoutWidget)
        self.label_infor1.setObjectName("label_infor1")
        self.verticalLayout.addWidget(self.label_infor1)
        self.label_infor2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_infor2.setObjectName("label_infor2")
        self.verticalLayout.addWidget(self.label_infor2)
        self.label_infor3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_infor3.setObjectName("label_infor3")
        self.verticalLayout.addWidget(self.label_infor3)
        self.label_infor4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_infor4.setObjectName("label_infor4")
        self.verticalLayout.addWidget(self.label_infor4)
        self.frame_image = QtWidgets.QFrame(self.centralwidget)
        self.frame_image.setGeometry(QtCore.QRect(20, 20, 391, 311))
        self.frame_image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_image.setObjectName("frame_image")
        self.label_image = QtWidgets.QLabel(self.frame_image)
        self.label_image.setGeometry(QtCore.QRect(10, 40, 361, 261))
        self.label_image.setObjectName("label_image")
        self.label_wechat = QtWidgets.QLabel(self.frame_image)
        self.label_wechat.setGeometry(QtCore.QRect(10, 10, 72, 15))
        self.label_wechat.setObjectName("label_wechat")
        ContactWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ContactWindow)
        self.statusbar.setObjectName("statusbar")
        ContactWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ContactWindow)
        QtCore.QMetaObject.connectSlotsByName(ContactWindow)

    def retranslateUi(self, ContactWindow):
        _translate = QtCore.QCoreApplication.translate
        ContactWindow.setWindowTitle(_translate("ContactWindow", "contact"))
        self.label_infor5.setText(_translate("ContactWindow", "Mr. Song"))
        self.label_infor1.setText(_translate("ContactWindow", "E-mail: peng.song@bjtu.edu.cn"))
        self.label_infor2.setText(_translate("ContactWindow", "Addr: Xiandai Road No.69, Weihai, China.P.R."))
        self.label_infor3.setText(_translate("ContactWindow", "org: Computer Science Department"))
        self.label_infor4.setText(_translate("ContactWindow", "     Beijing Jiaotong University"))
        self.label_image.setText(_translate("ContactWindow", "image"))
        self.label_wechat.setText(_translate("ContactWindow", "Wechat QR"))
