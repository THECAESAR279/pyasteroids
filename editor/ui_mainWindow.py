# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainWindow.ui'
#
# Created: Thu Dec  4 16:37:07 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        from editor.opengl import GLController
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1046,637)
        MainWindow.setMinimumSize(QtCore.QSize(1046,637))
        MainWindow.setMaximumSize(QtCore.QSize(1046,637))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(10,0,171,191))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(53,31,107,23))
        self.lineEdit.setObjectName("lineEdit")
        self.spinBox_2 = QtGui.QSpinBox(self.groupBox)
        self.spinBox_2.setGeometry(QtCore.QRect(53,59,107,24))
        self.spinBox_2.setMaximum(10000)
        self.spinBox_2.setSingleStep(100)
        self.spinBox_2.setProperty("value",QtCore.QVariant(2000))
        self.spinBox_2.setObjectName("spinBox_2")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(11,31,38,21))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(11,59,30,21))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(113,120,47,26))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(62,90,47,26))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtGui.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(11,120,47,26))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtGui.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(62,150,47,26))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(62,120,47,26))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10,260,171,321))
        self.groupBox_2.setObjectName("groupBox_2")
        self.spinBox_8 = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_8.setGeometry(QtCore.QRect(87,175,81,26))
        self.spinBox_8.setSingleStep(10)
        self.spinBox_8.setObjectName("spinBox_8")
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(11,29,51,21))
        self.label_6.setObjectName("label_6")
        self.spinBox_3 = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_3.setGeometry(QtCore.QRect(87,29,81,26))
        self.spinBox_3.setMaximum(10000)
        self.spinBox_3.setSingleStep(10)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_4 = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_4.setGeometry(QtCore.QRect(87,58,81,26))
        self.spinBox_4.setMaximum(10000)
        self.spinBox_4.setSingleStep(10)
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_5 = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_5.setGeometry(QtCore.QRect(87,87,81,26))
        self.spinBox_5.setSingleStep(10)
        self.spinBox_5.setObjectName("spinBox_5")
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(11,116,71,21))
        self.label_7.setObjectName("label_7")
        self.spinBox_6 = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_6.setGeometry(QtCore.QRect(87,116,81,26))
        self.spinBox_6.setSingleStep(10)
        self.spinBox_6.setObjectName("spinBox_6")
        self.spinBox_7 = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_7.setGeometry(QtCore.QRect(87,145,81,27))
        self.spinBox_7.setSingleStep(10)
        self.spinBox_7.setObjectName("spinBox_7")
        self.spinBox_9 = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_9.setGeometry(QtCore.QRect(87,204,81,26))
        self.spinBox_9.setMaximum(10000)
        self.spinBox_9.setSingleStep(10)
        self.spinBox_9.setObjectName("spinBox_9")
        self.comboBox = QtGui.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(87,233,81,26))
        self.comboBox.setObjectName("comboBox")
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setEnabled(False)
        self.label_11.setGeometry(QtCore.QRect(11,291,71,21))
        self.label_11.setObjectName("label_11")
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setEnabled(False)
        self.label_10.setGeometry(QtCore.QRect(11,262,72,21))
        self.label_10.setObjectName("label_10")
        self.comboBox_2 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_2.setEnabled(False)
        self.comboBox_2.setGeometry(QtCore.QRect(87,262,81,26))
        self.comboBox_2.setObjectName("comboBox_2")
        self.spinBox_10 = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_10.setEnabled(False)
        self.spinBox_10.setGeometry(QtCore.QRect(87,291,81,27))
        self.spinBox_10.setObjectName("spinBox_10")
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(11,233,63,21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(11,204,36,21))
        self.label_9.setObjectName("label_9")
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setEnabled(True)
        self.groupBox_3.setGeometry(QtCore.QRect(870,0,171,191))
        self.groupBox_3.setObjectName("groupBox_3")
        self.listWidget = QtGui.QListWidget(self.groupBox_3)
        self.listWidget.setGeometry(QtCore.QRect(10,30,151,151))
        self.listWidget.setObjectName("listWidget")
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setEnabled(True)
        self.groupBox_4.setGeometry(QtCore.QRect(190,0,671,581))
        self.groupBox_4.setObjectName("groupBox_4")
        self.widget = GLController(self.groupBox_4)
        self.widget.setGeometry(QtCore.QRect(10,30,651,551))
        self.widget.setAutoFillBackground(False)
        self.widget.setObjectName("widget")
        self.groupBox_5 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_5.setEnabled(True)
        self.groupBox_5.setGeometry(QtCore.QRect(870,190,171,191))
        self.groupBox_5.setObjectName("groupBox_5")
        self.listWidget_2 = QtGui.QListWidget(self.groupBox_5)
        self.listWidget_2.setGeometry(QtCore.QRect(10,30,151,151))
        self.listWidget_2.setObjectName("listWidget_2")
        self.groupBox_6 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_6.setEnabled(True)
        self.groupBox_6.setGeometry(QtCore.QRect(870,380,171,191))
        self.groupBox_6.setObjectName("groupBox_6")
        self.listWidget_3 = QtGui.QListWidget(self.groupBox_6)
        self.listWidget_3.setGeometry(QtCore.QRect(10,30,151,151))
        self.listWidget_3.setObjectName("listWidget_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,1046,25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtGui.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Level Editor - PyAsteroids 3D", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Scene", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setText(QtGui.QApplication.translate("MainWindow", "Untitled", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Size:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Right", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "Up", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "Left", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("MainWindow", "Down", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Spin", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Object", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Position:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Rotation vel:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(QtGui.QApplication.translate("MainWindow", "static", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(QtGui.QApplication.translate("MainWindow", "orbit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Orbit radius:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Orbit center:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Movement:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Mass:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Models", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "Space", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("MainWindow", "Elements", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("MainWindow", "Objects", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setText(QtGui.QApplication.translate("MainWindow", "Save as", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
