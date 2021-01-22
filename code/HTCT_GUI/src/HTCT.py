# -*- coding: utf-8 -*-
"""
@File  : HTCT.py
@Author: Peng
@email: peng.song@bjtu.edu.cn
@Date  : 2020/3/22 20:51
@Desc  :  cd import/invoke
"""

import sys
import pandas as pd
import webbrowser

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets

import gui.design.images_ui
from gui.design.homepage_ui import *
from gui.design.ht_ui import *
from gui.design.plot_ui import *
from gui.design.cd_ui import *
from gui.design.roc_ui import *
from gui.design.tss_ui import *
from gui.design.cc_ui import *
from gui.design.aar_ui import *
from gui.design.art_ui import *
from gui.design.dr_ui import *
from gui.design.kappa_ui import *
from gui.design.rmse_ui import *
from gui.design.contact_ui import *
from gui.design.knn_ui import *
from gui.design.wait_ui import *
from gui.showContent import *

import hypothesisTesting.twoClassifiers.statisticsMethod2 as Sm2
import hypothesisTesting.multiClassifiers.statisticsMethodMulti as Smm

# import plot.cd as cd
import plot.roc as roc
import plot.texasSharpShooter as tss_fun
import plot.classifierComparePairwise as Ccp
import plot.avgAccuRate as Aar_fun
import plot.avgRunningTimings as Art_fun
import plot.kappa as kappa_fun
import plot.rmse as rmse_fun

import dimensionalityReduction.AutoEncoder as Ae
import dimensionalityReduction.LDA as LDA
import dimensionalityReduction.LE as LE
import dimensionalityReduction.LPP as LPP
import dimensionalityReduction.MDS as MDS
import dimensionalityReduction.PCA as PCA
import dimensionalityReduction.TSNE as TSNE

import classifier.kNN as Knn_fun



class Homepage(QMainWindow, Ui_HomepageWindow):
    def __init__(self):
        """

        """
        super(Homepage, self).__init__()
        self.setupUi(self)
        self.temp_view = QTableView()
        self.temp_view.setWindowTitle('data quick view')

        self.init_ui()

    def init_ui(self):
        """

        :return:
        """
        self.textEdit_notice.setReadOnly(True)
        introduction = 'Thanks for using this visualization tool.' + \
                       ' It is my graduation project, and it will be continuously updated in the future. ' + \
                       'My effort mainly includes the above four parts' + \
                       ' - Hypothesis Testing, General Evaluation Models, Data Dimensionality Reduction' + \
                       ' and kNN classifier.'

        introduction += '\n\n1. Hypothesis Testing section contains eight common testing methods that compare' + \
                        ' the performance of paired and multiple classifiers ' + \
                        'to find out if there are significant differences between them.'

        introduction += '\n\n2. General Evaluation Models section contains data visualizations of some commonly used' + \
                        ' performance metrics to help users explicitly observe classifier performance.'

        introduction += '\n\n3. Data Dimensionality Reduction section includes seven dimensionality' + \
                        ' reduction methods. They are all set to reduce dimensions by 2 as default, ' + \
                        'so the effect may be not ideal for data having large dimensions.'

        introduction += '\n\n4. kNN section provides a KNN classifier based on different distances for time series.' + \
                        ' Users can get the performance differences caused by different' + \
                        ' distance algorithms on the same data sets.'

        introduction += '\n\n\nSong\n25 March, 2020'

        self.textEdit_notice.setText(introduction)

        # qrc file - py file
        pix = QPixmap(':/icon/uu_.png')

        # relative path
        # pix = QPixmap('./gui/design/icon/uu_.png')
        self.label_image.setPixmap(pix)

        # menu file action
        self.actionopen.triggered.connect(self.open_file)
        self.actionexit.triggered.connect(self.closeEvent)
        self.actionkNN.triggered.connect(self.pbt_knn_on_clicked)

        # menu visualization action
        self.actionaccuracy_rate.triggered.connect(self.menu_aar_on_clicked)
        self.actionrunning_time.triggered.connect(self.menu_art_on_clicked)
        self.actioncritical_distance.triggered.connect(self.menu_cd_on_clicked)
        self.actionROC.triggered.connect(self.menu_roc_on_clicked)
        self.actionclassifiers_comparison.triggered.connect(self.menu_cc_on_clicked)
        self.actionTexas_sharpshooter.triggered.connect(self.menu_tss_on_clicked)

        self.actionAutoencoder.triggered.connect(self.pbt_dr_on_clicked)
        self.actionLDA.triggered.connect(self.pbt_dr_on_clicked)
        self.actionLE.triggered.connect(self.pbt_dr_on_clicked)
        self.actionLPP.triggered.connect(self.pbt_dr_on_clicked)
        self.actionMDS.triggered.connect(self.pbt_dr_on_clicked)
        self.actionPCA.triggered.connect(self.pbt_dr_on_clicked)
        self.actiont_SNE.triggered.connect(self.pbt_dr_on_clicked)

        # menu help action
        self.actioncontact.triggered.connect(self.menu_contact_on_clicked)
        self.actiondataset_resource.triggered.connect(self.menu_dataset_on_clicked)
        self.actionalgorithm_reference.triggered.connect(self.menu_reference_on_clicked)
        self.actionHTC_homepage.triggered.connect(self.menu_htc_on_clicked)
        self.actionsave.triggered.connect(self.menu_wait_on_clicked)
        self.actioncheck_update.triggered.connect(self.menu_wait_on_clicked)

        # button signal
        self.pbt_ht.clicked.connect(self.pbt_ht_on_clicked)

        self.pbt_plot.clicked.connect(self.pbt_plot_on_clicked)
        self.pbt_dr.clicked.connect(self.pbt_dr_on_clicked)
        self.pbt_knn.clicked.connect(self.pbt_knn_on_clicked)
        self.pbt_ex.clicked.connect(self.menu_wait_on_clicked)

    def pbt_ht_on_clicked(self):
        """

        :return:
        """
        self.sub_window = Ht()
        self.sub_window.show()

    def pbt_plot_on_clicked(self):
        """

        :return:
        """
        self.sub_window = Plot()
        self.sub_window.show()

    def pbt_dr_on_clicked(self):
        """

        :return:
        """
        self.sub_window = DimensionalityReduction()
        self.sub_window.show()

    def pbt_knn_on_clicked(self):
        """

        :return:
        """
        self.sub_window = Knn()
        self.sub_window.show()

    def menu_aar_on_clicked(self):
        """

        :return:
        """
        self.sub_window = Aar()
        self.sub_window.show()

    def menu_art_on_clicked(self):
        """

        :return:
        """
        self.sub_window = Art()
        self.sub_window.show()

    def menu_cd_on_clicked(self):
        """

        :return:
        """
        self.sub_window = Cd()
        self.sub_window.show()

    def menu_roc_on_clicked(self):
        """

        :return:
        """
        self.sub_window = Roc()
        self.sub_window.show()

    def menu_cc_on_clicked(self):
        """

        :return:
        """
        self.sub_window = Cc()
        self.sub_window.show()

    def menu_tss_on_clicked(self):
        """

        :return:
        """
        self.sub_window = Tss()
        self.sub_window.show()

    def menu_contact_on_clicked(self):
        """

        :return:
        """
        self.sub_window = Contact()
        self.sub_window.show()

    def menu_wait_on_clicked(self):
        """

        :return:
        """
        self.sub_window = Wait()
        self.sub_window.show()

    def closeEvent(self, event):
        """
        Overriding this method is mainly to solve the problem that when a child window is opened,
        if the main window is closed but the child window is still displayed.
        Sys.exit(0) closes the main window and all associated child Windows
        :param event:
        :return:
        """
        sys.exit(0)

    @staticmethod
    def menu_htc_on_clicked():
        """

        :return:
        """
        webbrowser.open('http://127.0.0.1:5000/ ', new=0, autoraise=True)

    @staticmethod
    def menu_dataset_on_clicked():
        """

        :return:
        """
        webbrowser.open('http://www.timeseriesclassification.com/dataset.php', new=0, autoraise=True)

    @staticmethod
    def menu_reference_on_clicked():
        """

        :return:
        """
        webbrowser.open('http://www.timeseriesclassification.com/index.php', new=0, autoraise=True)

    def open_file(self):
        """

        :return:
        """
        self.statusbar.showMessage('opening file...', 1000)
        file_name, _ = QFileDialog.getOpenFileName(self, 'open file', './', 'CSV Files(*.csv)')
        if file_name:
            try:
                df = pd.read_csv(file_name)
                model = pandasModel(df)
                self.temp_view.setModel(model)
                self.temp_view.resize(800, 600)
                self.temp_view.show()
            except:
                self.dialog_select_data()

    def dialog_select_data(self):
        """

        :return:
        """
        self.box = QMessageBox(QMessageBox.Question, 'Warning', 'Please select the correct data file!')
        self.box.setGeometry(500, 500, 0, 0)
        self.box.show()


class Knn(QMainWindow, Ui_KNNWindow):
    def __init__(self):
        """

        """
        super(Knn, self).__init__()
        self.setupUi(self)
        self.temp_view = QTableView()

        self.init_ui()

    def init_ui(self):
        """

        :return:
        """
        self.temp_view.setWindowTitle('data quick view')
        self.textEdit_des.setReadOnly(True)
        self.textEdit_result.setReadOnly(True)
        des = 'Provide kNN classifier based on different distance algorithm.'
        des += '\n\nTry using different K value and distance algorithm to observe the classification performance.'
        self.textEdit_des.setText(des)

        # menu action
        self.actiontrain_dataset.triggered.connect(self.open_train)
        self.actiontest_dataset.triggered.connect(self.open_test)
        self.actionexit.triggered.connect(self.close)
        self.actionHTC_Homepage.triggered.connect(self.menu_htc_on_clicked)

        # button signal
        self.pbt_train.clicked.connect(self.open_train)
        self.pbt_test.clicked.connect(self.open_test)

        self.pbt_clear.clicked.connect(self.pbt_clear_on_clicked)

        self.pbt_start.clicked.connect(self.pbt_start_on_clicked)

    def pbt_start_on_clicked(self):
        """

        :return:
        """
        try:
            train_path, test_path, distance, k = self.get_infor()
            if train_path and test_path and distance and k:
                self.statusbar.showMessage('kNN is working...', 5000)
                result = Knn_fun.utilize_knn(train_path, test_path, distance, int(k))
                self.textEdit_result.setText(result)
            else:
                self.dialog_file()

        except:
            self.dialog_error()

    def get_infor(self):
        """

        :return:
        """
        train_path = self.lineEdit_train.text()
        test_path = self.lineEdit_test.text()
        distance = self.comboBox_dt.currentText()
        k = self.comboBox_k.currentText()
        return train_path, test_path, distance, k

    def pbt_clear_on_clicked(self):
        """

        :return:
        """
        self.statusbar.showMessage('clearing...', 1000)
        self.lineEdit_test.setText('')
        self.lineEdit_train.setText('')
        self.textEdit_result.setText('')

    def open_train(self):
        """

        :return:
        """
        self.statusbar.showMessage('opening file...', 1000)
        file_name, _ = QFileDialog.getOpenFileName(self, 'open file', './', 'CSV Files(*.csv)')
        if file_name:
            try:
                df = pd.read_csv(file_name)
                model = pandasModel(df)
                self.temp_view.setModel(model)
                self.temp_view.resize(800, 600)
                self.temp_view.show()
                self.lineEdit_train.setText(file_name)
            except:
                self.dialog_file()

    def open_test(self):
        """

        :return:
        """
        self.statusbar.showMessage('opening file...', 1000)
        file_name, _ = QFileDialog.getOpenFileName(self, 'open file', './', 'CSV Files(*.csv)')
        if file_name:
            try:
                df = pd.read_csv(file_name)
                model = pandasModel(df)
                self.temp_view.setModel(model)
                self.temp_view.resize(800, 600)
                self.temp_view.show()
                self.lineEdit_test.setText(file_name)
            except:
                self.dialog_file()

    def dialog_error(self):
        """

        :return:
        """
        self.box1 = QMessageBox(QMessageBox.Information, 'Warning', 'error, please check file format!')
        self.box1.setGeometry(500, 500, 0, 0)
        self.box1.show()

    def dialog_file(self):
        """

        :return:
        """
        self.box2 = QMessageBox(QMessageBox.Information, 'Warning', 'Please select the correct data file!')
        self.box2.setGeometry(500, 500, 0, 0)
        self.box2.show()

    @staticmethod
    def menu_htc_on_clicked():
        """

        :return:
        """
        webbrowser.open('http://127.0.0.1:5000/ ', new=0, autoraise=True)


class Contact(QMainWindow, Ui_ContactWindow):
    def __init__(self):
        """

        """
        super(Contact, self).__init__()
        self.setupUi(self)

        self.init_ui()

    def init_ui(self):
        """

        :return:
        """
        # pix = QPixmap('./gui/design/icon/qr.jpg')
        pix = QPixmap(':/icon/qr.jpg')
        self.label_image.setPixmap(pix)


class DimensionalityReduction(QMainWindow, Ui_DrWindow):
    def __init__(self):
        """

        """
        super(DimensionalityReduction, self).__init__()
        self.setupUi(self)
        self.temp_view = QTableView()

        self.init_ui()

    def init_ui(self):
        """

        :return:
        """
        self.temp_view.setWindowTitle('data quick view')

        self.textEdit_des.setReadOnly(True)
        des = 'Provide the above seven dimension reduction methods.\n\n'
        des += 'Their full name is \nAuto Encoder (AE), \n\nLinear discriminant Analysis (LDA),' + \
               ' \n\nLaplacian Eigenmaps (LE), \n\nLocality Preserving Projections (LPP), ' + \
               '\n\nMultiple Dimensional Scaling (MDS), \n\nPrincipal Component Analysis (PCA), ' + \
               '\n\nt-distributed Stochastic neighbour Embedding (t-SNE)'
        self.textEdit_des.setText(des)

        # menu action
        self.actionopen.triggered.connect(self.open_file)
        self.actionexit.triggered.connect(self.close)
        self.actionHTC_Homepage.triggered.connect(self.menu_htc_on_clicked)

        # button signal
        self.pbt_clear.clicked.connect(self.pbt_clear_on_clicked)
        self.pbt_input.clicked.connect(self.open_file)
        self.pbt_output.clicked.connect(self.choose_path)

        self.pbt_ae.clicked.connect(self.pbt_method_on_clicked)
        self.pbt_lda.clicked.connect(self.pbt_method_on_clicked)
        self.pbt_le.clicked.connect(self.pbt_method_on_clicked)
        self.pbt_lpp.clicked.connect(self.pbt_method_on_clicked)
        self.pbt_mds.clicked.connect(self.pbt_method_on_clicked)
        self.pbt_pca.clicked.connect(self.pbt_method_on_clicked)
        self.pbt_tsne.clicked.connect(self.pbt_method_on_clicked)

    def pbt_method_on_clicked(self):
        """

        :return:
        """
        try:
            pbt = self.sender()
            name = pbt.text()
            input_file, output_file = self.get_infor()

            if input_file and output_file:
                self.statusbar.showMessage('reducing data dimensionality...', 3000)
                if name == 'Auto Encoder':
                    Ae.auto_encoder_fun(input_file, output_file)
                elif name == 'LE':
                    LE.le_fun(input_file, output_file)
                elif name == 'LPP':
                    LPP.lpp_fun(input_file, output_file)
                elif name == 'MDS':
                    MDS.mds_fun(input_file, output_file)
                elif name == 'PCA':
                    PCA.pca_fun(input_file, output_file)
                elif name == 'LDA':
                    LDA.lda_fun(input_file, output_file)
                elif name == 't-SNE':
                    TSNE.tsne_fun(input_file, output_file)
                else:
                    self.dialog_error()
            else:
                self.dialog_file()
        except:
            self.dialog_error()

    def get_infor(self):
        """

        :return:
        """
        input_path = self.lineEdit_input.text()
        output_path = self.lineEdit_output.text()
        return input_path, output_path

    def pbt_clear_on_clicked(self):
        """

        :return:
        """
        self.statusbar.showMessage('clearing...', 1000)
        self.lineEdit_input.setText('')
        self.lineEdit_output.setText('')

    def choose_path(self):
        """

        :return:
        """
        self.statusbar.showMessage('choosing dir...', 1000)
        try:
            self.statusbar.showMessage('choosing dir...', 1000)
            dir_choose = QFileDialog.getExistingDirectory(self, 'Select saving path', './')
            if dir_choose:
                self.lineEdit_output.setText(dir_choose)
        except:
            self.dialog_error()

    def open_file(self):
        """

        :return:
        """
        self.statusbar.showMessage('opening file...', 1000)
        file_name, _ = QFileDialog.getOpenFileName(self, 'open file', './', 'CSV Files(*.csv)')
        if file_name:
            try:
                df = pd.read_csv(file_name)
                model = pandasModel(df)
                self.temp_view.setModel(model)
                self.temp_view.resize(800, 600)
                self.temp_view.show()
                self.lineEdit_input.setText(file_name)
            except:
                self.dialog_file()

    def dialog_error(self):
        """

        :return:
        """
        self.box1 = QMessageBox(QMessageBox.Information, 'Warning', 'error, please check file format!')
        self.box1.setGeometry(500, 500, 0, 0)
        self.box1.show()

    def dialog_file(self):
        """

        :return:
        """
        self.box2 = QMessageBox(QMessageBox.Information, 'Warning', 'Please select the correct data file!')
        self.box2.setGeometry(500, 500, 0, 0)
        self.box2.show()

    @staticmethod
    def menu_htc_on_clicked():
        """

        :return:
        """
        webbrowser.open('http://127.0.0.1:5000/ ', new=0, autoraise=True)


class Plot(QMainWindow, Ui_PlotWindow):
    def __init__(self):
        """

        """
        super(Plot, self).__init__()
        self.setupUi(self)

        self.init_ui()

    def init_ui(self):
        """

        :return:
        """
        self.textEdit_note.setReadOnly(True)
        self.textEdit_note.setText(
            'Note:\nPlease select a data file that conforms to the format requirements, otherwise an error may occur.' +
            '\n--------------------------\n\nPlease check <Helps> to know the doc requirements!')

        # button signal
        self.pbt_cd.clicked.connect(self.pbt_cd_on_clicked)
        self.pbt_roc.clicked.connect(self.pbt_roc_on_clicked)
        self.pbt_tss.clicked.connect(self.pbt_tss_on_clicked)
        self.pbt_cc.clicked.connect(self.pbt_cc_on_clicked)
        self.pbt_aar.clicked.connect(self.pbt_aar_on_clicked)
        self.pbt_art.clicked.connect(self.pbt_art_on_clicked)
        self.pbt_kappa.clicked.connect(self.pbt_kappa_on_clicked)
        self.pbt_rmse.clicked.connect(self.pbt_rmse_on_clicked)

        # menu
        self.actionopen.triggered.connect(self.open_file)
        self.actionexit.triggered.connect(self.close)

    def pbt_cc_on_clicked(self):
        """

        :return:
        """
        self.sub_window = Cc()
        self.sub_window.show()

    def pbt_tss_on_clicked(self):
        """

        :return:
        """
        self.sub_window = Tss()
        self.sub_window.show()

    def pbt_cd_on_clicked(self):
        """

        :return:
        """
        self.sub_window = Cd()
        self.sub_window.show()

    def pbt_kappa_on_clicked(self):
        """
        :return:
        """
        self.sub_window = Kappa()
        self.sub_window.show()

    def pbt_rmse_on_clicked(self):
        """

        :return:
        """
        self.sub_window = Rmse()
        self.sub_window.show()

    def pbt_roc_on_clicked(self):
        """

        :return:
        """
        self.sub_window = Roc()
        self.sub_window.show()

    def pbt_aar_on_clicked(self):
        """

        :return:
        """
        self.sub_window = Aar()
        self.sub_window.show()

    def pbt_art_on_clicked(self):
        """

        :return:
        """
        self.sub_window = Art()
        self.sub_window.show()

    def open_file(self):
        """

        :return:
        """
        self.statusbar.showMessage('opening file...', 1000)
        file_name, _ = QFileDialog.getOpenFileName(self, 'open file', './', 'CSV Files(*.csv)')
        if file_name:
            try:
                df = pd.read_csv(file_name)
                model = pandasModel(df)
                self.temp_view.setModel(model)
                self.temp_view.resize(800, 600)
                self.temp_view.show()
                self.lineEdit_input.setText(file_name)
            except:
                self.dialog_file()

    def dialog_error(self):
        """

        :return:
        """
        self.box1 = QMessageBox(QMessageBox.Information, 'Warning', 'error, please check file format!')
        self.box1.setGeometry(500, 500, 0, 0)
        self.box1.show()

    def dialog_file(self):
        """

        :return:
        """
        self.box2 = QMessageBox(QMessageBox.Information, 'Warning', 'Please select the correct data file!')
        self.box2.setGeometry(500, 500, 0, 0)
        self.box2.show()


class Rmse(QMainWindow, Ui_RmseWindow):
    def __init__(self):
        """

        """
        super(Rmse, self).__init__()
        self.setupUi(self)
        self.temp_view = QTableView()
        self.temp_view.setWindowTitle('data quick view')

        self.init_ui()

    def init_ui(self):
        """

        :return:
        """
        self.textEdit_result.setReadOnly(True)
        self.textEdit_result.setText('The result will be here.\n')

        # menu action
        self.actionopen.triggered.connect(self.open_file)
        self.actionexit.triggered.connect(self.close)

        # button signal
        self.pbt_clear_2.clicked.connect(self.pbt_clear_on_clicked)
        self.pbt_rmse.clicked.connect(self.pbt_rmse_on_clicked)

    def pbt_rmse_on_clicked(self):

        self.statusbar.showMessage('performing...', 1000)
        try:
            input_path = self.get_infor()
            if input_path:
                rmse = rmse_fun.rmse_fun(input_path)
                result = 'RMSE = ' + str(rmse)
                self.textEdit_result.setText(result)
            else:
                self.dialog_file()
        except:
            self.dialog_error()

    def get_infor(self):
        """

        :return:
        """
        input_path = self.lineEdit.text()
        return input_path

    def pbt_clear_on_clicked(self):
        """

        :return:
        """
        self.statusbar.showMessage('clearing...', 1000)
        self.lineEdit.setText('')
        self.textEdit_result.setText('The result will be here.\n')

    def open_file(self):
        """

        :return:
        """
        self.statusbar.showMessage('opening file...', 1000)
        file_name, _ = QFileDialog.getOpenFileName(self, 'open file', './', 'CSV Files(*.csv)')
        if file_name:
            try:
                df = pd.read_csv(file_name)
                model = pandasModel(df)
                self.temp_view.setModel(model)
                self.temp_view.resize(800, 600)
                self.temp_view.show()
                self.lineEdit.setText(file_name)
            except:
                self.dialog_file()

    def dialog_error(self):
        """

        :return:
        """
        self.box1 = QMessageBox(QMessageBox.Information, 'Warning', 'error, please check file format!')
        self.box1.setGeometry(500, 500, 0, 0)
        self.box1.show()

    def dialog_file(self):
        """

        :return:
        """
        self.box2 = QMessageBox(QMessageBox.Information, 'Warning', 'Please select the correct data file!')
        self.box2.setGeometry(500, 500, 0, 0)
        self.box2.show()


class Kappa(QMainWindow, Ui_KappaWindow):
    def __init__(self):
        """

        """
        super(Kappa, self).__init__()
        self.setupUi(self)
        self.temp_view = QTableView()
        self.temp_view.setWindowTitle('data quick view')

        self.init_ui()

    def init_ui(self):
        """

        :return:
        """
        self.textEdit_result.setReadOnly(True)
        self.textEdit_result.setText('The result will be here.\n')

        # menu action
        self.actionopen.triggered.connect(self.open_file)
        self.actionexit.triggered.connect(self.close)

        # button signal
        self.pbt_clear_2.clicked.connect(self.pbt_clear_on_clicked)
        self.pbt_kappa.clicked.connect(self.pbt_kappa_on_clicked)

    def pbt_kappa_on_clicked(self):

        self.statusbar.showMessage('performing...', 1000)
        try:
            input_path = self.get_infor()
            if input_path:
                accuracy, pec, kappa = kappa_fun.kappa_fun(input_path)
                result = 'Accuracy = ' + str(int(accuracy * 1000) / 1000) + '\nPec = ' + str(
                    int(pec * 1000) / 1000) + '\nCohen’s Kappa = ' + str(int(kappa * 1000) / 1000)
                self.textEdit_result.setText(result)
            else:
                self.dialog_file()
        except:
            self.dialog_error()

    def get_infor(self):
        """

        :return:
        """
        input_path = self.lineEdit.text()
        return input_path

    def pbt_clear_on_clicked(self):
        """

        :return:
        """
        self.statusbar.showMessage('clearing...', 1000)
        self.lineEdit.setText('')
        self.textEdit_result.setText('The result will be here.\n')

    def open_file(self):
        """

        :return:
        """
        self.statusbar.showMessage('opening file...', 1000)
        file_name, _ = QFileDialog.getOpenFileName(self, 'open file', './', 'CSV Files(*.csv)')
        if file_name:
            try:
                df = pd.read_csv(file_name)
                model = pandasModel(df)
                self.temp_view.setModel(model)
                self.temp_view.resize(800, 600)
                self.temp_view.show()
                self.lineEdit.setText(file_name)
            except:
                self.dialog_file()

    def dialog_error(self):
        """

        :return:
        """
        self.box1 = QMessageBox(QMessageBox.Information, 'Warning', 'error, please check file format!')
        self.box1.setGeometry(500, 500, 0, 0)
        self.box1.show()

    def dialog_file(self):
        """

        :return:
        """
        self.box2 = QMessageBox(QMessageBox.Information, 'Warning', 'Please select the correct data file!')
        self.box2.setGeometry(500, 500, 0, 0)
        self.box2.show()


class Art(QMainWindow, Ui_ArtWindow):
    def __init__(self):
        """

        """
        super(Art, self).__init__()
        self.setupUi(self)
        self.temp_view = QTableView()
        self.temp_view.setWindowTitle('data quick view')

        self.init_ui()

    def init_ui(self):
        """

        :return:
        """
        self.textEdit_des.setReadOnly(True)
        self.textEdit_des.setText('An overall view for classifiers performance.')

        # menu action
        self.actionopen.triggered.connect(self.open_file)
        self.actionexit.triggered.connect(self.close)

        # button signal
        self.pbt_clear.clicked.connect(self.pbt_clear_on_clicked)
        self.pbt_input.clicked.connect(self.open_file)
        self.pbt_output.clicked.connect(self.choose_path)
        self.pbt_plot.clicked.connect(self.pbt_plot_on_clicked)

    def pbt_plot_on_clicked(self):
        """

        :return:
        """
        self.statusbar.showMessage('plotting...', 3000)
        try:
            input_path, output_path = self.get_infor()
            if input_path and output_path:
                Art_fun.plot_average_timings(input_path, output_path)

            else:
                self.dialog_file()
        except:
            self.dialog_error()

    def get_infor(self):
        """

        :return:
        """
        input_path = self.lineEdit_input.text()
        output_path = self.lineEdit_output.text()
        return input_path, output_path

    def pbt_clear_on_clicked(self):
        """

        :return:
        """
        self.statusbar.showMessage('clearing...', 1000)
        self.lineEdit_input.setText('')
        self.lineEdit_output.setText('')

    def choose_path(self):
        """

        :return:
        """
        self.statusbar.showMessage('choosing dir...', 1000)
        try:
            self.statusbar.showMessage('choosing dir...', 1000)
            dir_choose = QFileDialog.getExistingDirectory(self, 'Select saving path', './')
            if dir_choose:
                self.lineEdit_output.setText(dir_choose)
        except:
            self.dialog_error()

    def open_file(self):
        """

        :return:
        """
        self.statusbar.showMessage('opening file...', 1000)
        file_name, _ = QFileDialog.getOpenFileName(self, 'open file', './', 'CSV Files(*.csv)')
        if file_name:
            try:
                df = pd.read_csv(file_name)
                model = pandasModel(df)
                self.temp_view.setModel(model)
                self.temp_view.resize(800, 600)
                self.temp_view.show()
                self.lineEdit_input.setText(file_name)
            except:
                self.dialog_file()

    def dialog_error(self):
        """

        :return:
        """
        self.box1 = QMessageBox(QMessageBox.Information, 'Warning', 'error, please check file format!')
        self.box1.setGeometry(500, 500, 0, 0)
        self.box1.show()

    def dialog_file(self):
        """

        :return:
        """
        self.box2 = QMessageBox(QMessageBox.Information, 'Warning', 'Please select the correct data file!')
        self.box2.setGeometry(500, 500, 0, 0)
        self.box2.show()


class Aar(QMainWindow, Ui_AarWindow):
    def __init__(self):
        """

        """
        super(Aar, self).__init__()
        self.setupUi(self)
        self.temp_view = QTableView()
        self.temp_view.setWindowTitle('data quick view')

        self.init_ui()

    def init_ui(self):
        """

        :return:
        """
        self.rbt_ar.setChecked(True)
        self.textEdit_des.setReadOnly(True)
        self.textEdit_des.setText('An overall view for classifiers performance.')

        # menu action
        self.actionopen.triggered.connect(self.open_file)
        self.actionexit.triggered.connect(self.close)

        # button signal
        self.pbt_clear.clicked.connect(self.pbt_clear_on_clicked)
        self.pbt_input.clicked.connect(self.open_file)
        self.pbt_output.clicked.connect(self.choose_path)
        self.pbt_plot.clicked.connect(self.pbt_plot_on_clicked)

    def pbt_plot_on_clicked(self):
        """

        :return:
        """
        self.statusbar.showMessage('plotting...', 3000)
        try:
            input_path, output_path, is_error_rate = self.get_infor()
            if input_path and output_path:
                Aar_fun.plot_average_accuracy_rate(input_path, output_path, is_error_rate)

            else:
                self.dialog_file()
        except:
            self.dialog_error()

    def get_infor(self):
        """

        :return:
        """
        input_path = self.lineEdit_input.text()
        output_path = self.lineEdit_output.text()
        is_error_rate = True if self.rbt_er.isChecked() else False
        return input_path, output_path, is_error_rate

    def pbt_clear_on_clicked(self):
        """

        :return:
        """
        self.statusbar.showMessage('clearing...', 1000)
        self.lineEdit_input.setText('')
        self.lineEdit_output.setText('')

    def choose_path(self):
        """

        :return:
        """
        self.statusbar.showMessage('choosing dir...', 1000)
        try:
            self.statusbar.showMessage('choosing dir...', 1000)
            dir_choose = QFileDialog.getExistingDirectory(self, 'Select saving path', './')
            if dir_choose:
                self.lineEdit_output.setText(dir_choose)
        except:
            self.dialog_error()

    def open_file(self):
        """

        :return:
        """
        self.statusbar.showMessage('opening file...', 1000)
        file_name, _ = QFileDialog.getOpenFileName(self, 'open file', './', 'CSV Files(*.csv)')
        if file_name:
            try:
                df = pd.read_csv(file_name)
                model = pandasModel(df)
                self.temp_view.setModel(model)
                self.temp_view.resize(800, 600)
                self.temp_view.show()
                self.lineEdit_input.setText(file_name)
            except:
                self.dialog_file()

    def dialog_error(self):
        """

        :return:
        """
        self.box1 = QMessageBox(QMessageBox.Information, 'Warning', 'error, please check file format!')
        self.box1.setGeometry(500, 500, 0, 0)
        self.box1.show()

    def dialog_file(self):
        """

        :return:
        """
        self.box2 = QMessageBox(QMessageBox.Information, 'Warning', 'Please select the correct data file!')
        self.box2.setGeometry(500, 500, 0, 0)
        self.box2.show()


class Cc(QMainWindow, Ui_CcWindow):
    def __init__(self):
        """

        """
        super(Cc, self).__init__()
        self.setupUi(self)
        self.temp_view = QTableView()
        self.temp_view.setWindowTitle('data quick view')

        self.init_ui()

    def init_ui(self):
        """

        :return:
        """
        self.rbt_ar.setChecked(True)
        self.textEdit_des.setReadOnly(True)
        self.textEdit_des.setText(
            'Compare the average accuracy of two or more classifiers.' +
            'This graph is a scatter graph and shadows the winning region for each classifier.')

        # menu action
        self.actionopen.triggered.connect(self.open_file)
        self.actionexit.triggered.connect(self.close)

        # button signal
        self.pbt_clear.clicked.connect(self.pbt_clear_on_clicked)
        self.pbt_input.clicked.connect(self.open_file)
        self.pbt_output.clicked.connect(self.choose_path)
        self.pbt_plot.clicked.connect(self.pbt_plot_on_clicked)

    def pbt_plot_on_clicked(self):
        """

        :return:
        """
        try:
            input_path, output_path, classifier, is_error_rate = self.get_infor()
            if input_path and output_path and classifier:
                self.statusbar.showMessage('plotting...', 2000)
                Ccp.plot_compare_pairs(input_path, classifier, output_path, is_error_rate)
            else:
                self.dialog_file()
        except:
            self.dialog_error()

    def get_infor(self):
        """

        :return:
        """
        input_path = self.lineEdit_input.text()
        output_path = self.lineEdit_output.text()
        classifier = self.lineEdit_classifier.text()
        is_error_rate = True if self.rbt_er.isChecked() else False

        return input_path, output_path, classifier, is_error_rate

    def choose_path(self):
        """

        :return:
        """
        self.statusbar.showMessage('choosing dir...', 1000)
        try:
            self.statusbar.showMessage('choosing dir...', 1000)
            dir_choose = QFileDialog.getExistingDirectory(self, 'Select saving path', './')
            if dir_choose:
                self.lineEdit_output.setText(dir_choose)
        except:
            self.dialog_error()

    def pbt_clear_on_clicked(self):
        """

        :return:
        """
        self.statusbar.showMessage('clearing...', 1000)
        self.lineEdit_input.setText('')
        self.lineEdit_output.setText('')
        self.lineEdit_classifier.setText('')

    def open_file(self):
        """

        :return:
        """
        self.statusbar.showMessage('opening file...', 1000)
        file_name, _ = QFileDialog.getOpenFileName(self, 'open file', './', 'CSV Files(*.csv)')
        if file_name:
            try:
                df = pd.read_csv(file_name)
                model = pandasModel(df)
                self.temp_view.setModel(model)
                self.temp_view.resize(800, 600)
                self.temp_view.show()
                self.lineEdit_input.setText(file_name)
            except:
                self.dialog_file()

    def dialog_error(self):
        """

        :return:
        """
        self.box1 = QMessageBox(QMessageBox.Information, 'Warning', 'error, please check file format!')
        self.box1.setGeometry(500, 500, 0, 0)
        self.box1.show()

    def dialog_file(self):
        """

        :return:
        """
        self.box2 = QMessageBox(QMessageBox.Information, 'Warning', 'Please provide sufficient parameters!')
        self.box2.setGeometry(500, 500, 0, 0)
        self.box2.show()


class Tss(QMainWindow, Ui_TssWindow):
    """

    """

    def __init__(self):
        super(Tss, self).__init__()
        self.setupUi(self)
        self.temp_view = QTableView()
        self.temp_view.setWindowTitle('data quick view')

        self.init_ui()

    def init_ui(self):
        """

        :return:
        """
        self.rbt_ar.setChecked(True)
        self.textEdit_des.setReadOnly(True)
        self.textEdit_des.setText(
            'Texas Sharpshooter diagram.')

        # menu action
        self.actionopen.triggered.connect(self.open_file)
        self.actionexit.triggered.connect(self.close)

        # button signal
        self.pbt_clear.clicked.connect(self.pbt_clear_on_clicked)
        self.pbt_input.clicked.connect(self.open_file)
        self.pbt_output.clicked.connect(self.choose_path)
        self.pbt_plot.clicked.connect(self.pbt_plot_on_clicked)

    def pbt_plot_on_clicked(self):
        """

        :return:
        """
        try:
            input_path, output_path, classifier_a, classifier_b, is_error_rate = self.get_infor()
            if input_path and output_path and classifier_a and classifier_b:
                self.statusbar.showMessage('plotting...', 2000)
                tss_fun.texas_sharp_shooter(classifier_a, classifier_b, is_error_rate, input_path, output_path)
            else:
                self.dialog_file()
        except:
            self.dialog_error()

    def get_infor(self):
        """

        :return:
        """
        input_path = self.lineEdit_input.text()
        output_path = self.lineEdit_output.text()

        classifier_a = self.lineEdit_ca.text()
        classifier_b = self.lineEdit_cb.text()
        is_error_rate = True if self.rbt_er.isChecked() else False
        return input_path, output_path, classifier_a, classifier_b, is_error_rate

    def choose_path(self):
        """

        :return:
        """
        self.statusbar.showMessage('choosing dir...', 1000)
        try:
            self.statusbar.showMessage('choosing dir...', 1000)
            dir_choose = QFileDialog.getExistingDirectory(self, 'Select saving path', './')
            if dir_choose:
                self.lineEdit_output.setText(dir_choose)
        except:
            self.dialog_error()

    def pbt_clear_on_clicked(self):
        """

        :return:
        """
        self.statusbar.showMessage('clearing...', 1000)
        self.lineEdit_input.setText('')
        self.lineEdit_output.setText('')
        self.lineEdit_ca.setText('')
        self.lineEdit_cb.setText('')

    def open_file(self):
        """

        :return:
        """
        self.statusbar.showMessage('opening file...', 1000)
        file_name, _ = QFileDialog.getOpenFileName(self, 'open file', './', 'CSV Files(*.csv)')
        if file_name:
            try:
                df = pd.read_csv(file_name)
                model = pandasModel(df)
                self.temp_view.setModel(model)
                self.temp_view.resize(800, 600)
                self.temp_view.show()
                self.lineEdit_input.setText(file_name)
            except:
                self.dialog_file()

    def dialog_error(self):
        """

        :return:
        """
        self.box1 = QMessageBox(QMessageBox.Information, 'Warning', 'error, please check file format!')
        self.box1.setGeometry(500, 500, 0, 0)
        self.box1.show()

    def dialog_file(self):
        """

        :return:
        """
        self.box2 = QMessageBox(QMessageBox.Information, 'Warning', 'Please provide sufficient parameters!')
        self.box2.setGeometry(500, 500, 0, 0)
        self.box2.show()


class Roc(QMainWindow, Ui_RocWindow):
    def __init__(self):
        """

        """
        super(Roc, self).__init__()
        self.setupUi(self)
        self.temp_view = QTableView()
        self.temp_view.setWindowTitle('data quick view')

        self.init_ui()

    def init_ui(self):
        """

        :return:
        """
        self.textEdit_des.setReadOnly(True)
        self.textEdit_des.setText(
            'A Receiver Operating Characteristic (ROC) Curve is a way to compare diagnostic tests.' +
            ' It is a plot of the true positive rate against the false positive rate.')

        # menu action
        self.actionopen.triggered.connect(self.open_file)
        self.actionexit.triggered.connect(self.close)

        # button signal
        self.pbt_clear.clicked.connect(self.pbt_clear_on_clicked)
        self.pbt_input.clicked.connect(self.open_file)
        self.pbt_output.clicked.connect(self.choose_path)
        self.pbt_plot.clicked.connect(self.pbt_plot_on_clicked)

    def pbt_plot_on_clicked(self):
        """

        :return:
        """
        try:
            input_path, output_path, pos_label = self.get_infor()
            if input_path and output_path and pos_label:
                self.statusbar.showMessage('plotting...', 2000)
                roc.roc(input_path, output_path, pos_label)
            else:
                self.dialog_file()
        except:
            self.dialog_error()

    def get_infor(self):
        """

        :return:
        """
        input_path = self.lineEdit_input.text()
        output_path = self.lineEdit_output.text()
        pos_label = int(self.lineEdit_pl.text())
        return input_path, output_path, pos_label

    def choose_path(self):
        """

        :return:
        """
        self.statusbar.showMessage('choosing dir...', 1000)
        try:
            self.statusbar.showMessage('choosing dir...', 1000)
            dir_choose = QFileDialog.getExistingDirectory(self, 'Select saving path', './')
            if dir_choose:
                self.lineEdit_output.setText(dir_choose)
        except:
            self.dialog_error()

    def pbt_clear_on_clicked(self):
        """

        :return:
        """
        self.statusbar.showMessage('clearing...', 1000)
        self.lineEdit_input.setText('')
        self.lineEdit_output.setText('')
        self.lineEdit_pl.setText('')

    def open_file(self):
        """

        :return:
        """
        self.statusbar.showMessage('opening file...', 1000)
        file_name, _ = QFileDialog.getOpenFileName(self, 'open file', './', 'CSV Files(*.csv)')
        if file_name:
            try:
                df = pd.read_csv(file_name)
                model = pandasModel(df)
                self.temp_view.setModel(model)
                self.temp_view.resize(800, 600)
                self.temp_view.show()
                self.lineEdit_input.setText(file_name)
            except:
                self.dialog_file()

    def dialog_error(self):
        """

        :return:
        """
        self.box1 = QMessageBox(QMessageBox.Information, 'Warning', 'error, please check file format!')
        self.box1.setGeometry(500, 500, 0, 0)
        self.box1.show()

    def dialog_file(self):
        """

        :return:
        """
        self.box2 = QMessageBox(QMessageBox.Information, 'Warning', 'Please provide sufficient parameters!!')
        self.box2.setGeometry(500, 500, 0, 0)
        self.box2.show()


class Cd(QMainWindow, Ui_CdWindow):
    """

    """

    def __init__(self):
        super(Cd, self).__init__()
        self.setupUi(self)
        self.temp_view = QTableView()
        self.temp_view.setWindowTitle('data quick view')

        self.init_ui()

    def init_ui(self):
        """

        :return:
        """
        self.rbt_ar.setChecked(True)
        self.textEdit_des.setReadOnly(True)
        self.textEdit_des.setText(
            'The critical distance is used ' +
            'to view the performance differences of multiple classifiers over multiple data sets.')

        # menu action
        self.actionopen.triggered.connect(self.open_file)
        self.actionexit.triggered.connect(self.close)

        # button signal
        self.pbt_clear.clicked.connect(self.pbt_clear_on_clicked)
        self.pbt_input.clicked.connect(self.open_file)
        self.pbt_output.clicked.connect(self.choose_path)
        self.pbt_plot.clicked.connect(self.pbt_plot_on_clicked)

    def pbt_plot_on_clicked(self):
        """

        :return:
        """
        self.statusbar.showMessage('plotting...', 5000)
        try:
            input_path, output_path, is_error_rate = self.get_infor()
            if input_path and output_path:
                self.subwindow = Wait()
                self.subwindow.show()
                # cd.plot_cd(input_path, output_path, is_error_rate)
            else:
                self.dialog_file()
        except:
            self.dialog_error()

    def get_infor(self):
        """

        :return:
        """
        input_path = self.lineEdit_input.text()
        output_path = self.lineEdit_output.text()
        is_error_rate = True if self.rbt_er.isChecked() else False
        return input_path, output_path, is_error_rate

    def pbt_clear_on_clicked(self):
        """

        :return:
        """
        self.statusbar.showMessage('clearing...', 1000)
        self.lineEdit_input.setText('')
        self.lineEdit_output.setText('')

    def choose_path(self):
        """

        :return:
        """
        self.statusbar.showMessage('choosing dir...', 1000)
        try:
            self.statusbar.showMessage('choosing dir...', 1000)
            dir_choose = QFileDialog.getExistingDirectory(self, 'Select saving path', './')
            if dir_choose:
                self.lineEdit_output.setText(dir_choose)
        except:
            self.dialog_error()

    def open_file(self):
        """

        :return:
        """
        self.statusbar.showMessage('opening file...', 1000)
        file_name, _ = QFileDialog.getOpenFileName(self, 'open file', './', 'CSV Files(*.csv)')
        if file_name:
            try:
                df = pd.read_csv(file_name)
                model = pandasModel(df)
                self.temp_view.setModel(model)
                self.temp_view.resize(800, 600)
                self.temp_view.show()
                self.lineEdit_input.setText(file_name)
            except:
                self.dialog_file()

    def dialog_error(self):
        """

        :return:
        """
        self.box1 = QMessageBox(QMessageBox.Information, 'Warning', 'error, please check file format!')
        self.box1.setGeometry(500, 500, 0, 0)
        self.box1.show()

    def dialog_file(self):
        """

        :return:
        """
        self.box2 = QMessageBox(QMessageBox.Information, 'Warning', 'Please select the correct data file!')
        self.box2.setGeometry(500, 500, 0, 0)
        self.box2.show()


class Wait(QMainWindow, Ui_WaitWindow):
    def __init__(self):
        super(Wait, self).__init__()
        self.setupUi(self)

        self.textEdit_notice.setReadOnly(True)
        self.textEdit_notice.setText('The function is still improving, please stay tuned.')


class Ht(QMainWindow, Ui_HtWindow):
    def __init__(self):
        """

        """
        super(Ht, self).__init__()
        self.setupUi(self)
        self.temp_view = QTableView()
        self.temp_view.setWindowTitle('data quick view')

        self.init_ui()

    def init_ui(self):
        """

        :return:
        """
        self.rbt_er.setChecked(True)
        self.rbt_005.setChecked(True)

        self.textEdit_result.setReadOnly(True)
        self.textEdit_result.setText(
            'Note:\nPlease select a data file that conforms to the format requirements, otherwise an error may occur.' +
            '\n------------------------------------\n\nPlease check <Helps> to know the doc requirements!')

        # menu action
        self.actionopen.triggered.connect(self.open_file)
        self.actionexit.triggered.connect(self.close)

        # button signal
        self.pbt_clear.clicked.connect(self.pbt_clear_on_clicked)

        self.pbt_pt.clicked.connect(self.pbt_ht_on_clicked)
        self.pbt_w.clicked.connect(self.pbt_ht_on_clicked)
        self.pbt_mn.clicked.connect(self.pbt_ht_on_clicked)
        self.pbt_mw.clicked.connect(self.pbt_ht_on_clicked)
        self.pbt_rs.clicked.connect(self.pbt_ht_on_clicked)
        self.pbt_fr.clicked.connect(self.pbt_ht_on_clicked)
        self.pbt_kr.clicked.connect(self.pbt_ht_on_clicked)
        self.pbt_va.clicked.connect(self.pbt_ht_on_clicked)

    def pbt_ht_on_clicked(self):
        """

        :return:
        """
        try:
            pbt = self.sender()
            name = pbt.text()
            file_path, is_error_rate, confidence = self.get_infor()
            if file_path:
                self.statusbar.showMessage('analyzing data ...', 1000)
                if name == 'Paired T':
                    result = Sm2.ttest(file_path, is_error_rate, confidence)
                elif name == 'McNemar':
                    result = Sm2.mc_nemar(file_path, confidence)
                elif name == 'Wilcox Signed-Ranks':
                    result = Sm2.mannwhitneyu(file_path, is_error_rate, confidence)
                elif name == 'Sign':
                    result = Sm2.rank_sums(file_path, is_error_rate, confidence)
                elif name == 'Wilcox Rank-Sum':
                    result = Sm2.wilcoxon(file_path, is_error_rate, confidence)
                elif name == 'Kruskal–Wallis':
                    result = Smm.kruskal(file_path, is_error_rate, confidence)
                elif name == 'Friedman':
                    result = Smm.friedman(file_path, is_error_rate, confidence)
                elif name == 'ANOVA':
                    result = Smm.one_way_variance(file_path, is_error_rate)
                else:
                    result = 'error, please check file format!'

                self.textEdit_result.setText(result)
            else:
                self.dialog_select_data()
        except:
            self.dialog_select_data()

    def get_infor(self):
        """

        :return:
        """
        file_path = self.lineEdit.text()
        is_error_rate = True if self.rbt_er.isChecked() else False
        confidence = 0.05 if self.rbt_005.isChecked() else 0.1
        return file_path, is_error_rate, confidence

    def dialog_select_data(self):
        """

        :return:
        """
        self.box = QMessageBox(QMessageBox.Information, 'Warning', 'Please select the correct data file!')
        self.box.setGeometry(500, 500, 0, 0)
        self.box.show()

    def pbt_clear_on_clicked(self):
        """

        :return:
        """
        self.statusbar.showMessage('clearing...', 1000)
        self.lineEdit.setText('')
        self.textEdit_result.setText(
            'Note:\nPlease select a data file that conforms to the format requirements, otherwise an error may occur.' +
            '\n------------------------------------\n\nPlease check <Helps> to know the doc requirements!')

    def open_file(self):
        """

        :return:
        """
        self.statusbar.showMessage('opening file...', 1000)
        file_name, _ = QFileDialog.getOpenFileName(self, 'open file', './', 'CSV Files(*.csv)')
        if file_name:
            try:
                df = pd.read_csv(file_name)
                model = pandasModel(df)

                self.temp_view.setModel(model)
                self.temp_view.resize(800, 600)
                self.temp_view.show()
                self.lineEdit.setText(file_name)
            except:
                self.dialog_select_data()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # app.setWindowIcon(QIcon('./gui/design/icon/home.ico'))
    app.setWindowIcon(QIcon(':/icon/home.ico'))
    main_window = Homepage()
    main_window.show()
    sys.exit(app.exec_())
