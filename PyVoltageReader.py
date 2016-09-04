# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyVoltageReader.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 641)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mplLayout = QtWidgets.QVBoxLayout()
        self.mplLayout.setObjectName("mplLayout")
        self.verticalLayout.addLayout(self.mplLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setMaximumSize(QtCore.QSize(55, 23))
        self.startButton.setObjectName("startButton")
        self.horizontalLayout.addWidget(self.startButton)
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setMaximumSize(QtCore.QSize(54, 23))
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout.addWidget(self.stopButton)
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setMaximumSize(QtCore.QSize(55, 23))
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(27, 23))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.gpibBox = QtWidgets.QComboBox(self.centralwidget)
        self.gpibBox.setObjectName("gpibBox")
        self.horizontalLayout.addWidget(self.gpibBox)
        self.refreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshButton.setMaximumSize(QtCore.QSize(80, 23))
        self.refreshButton.setObjectName("refreshButton")
        self.horizontalLayout.addWidget(self.refreshButton)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(88, 16))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.rateBox = QtWidgets.QSpinBox(self.centralwidget)
        self.rateBox.setMaximumSize(QtCore.QSize(79, 20))
        self.rateBox.setMaximum(999999999)
        self.rateBox.setProperty("value", 10)
        self.rateBox.setObjectName("rateBox")
        self.horizontalLayout.addWidget(self.rateBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 21))
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
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.label.setText(_translate("MainWindow", "GPIB:"))
        self.refreshButton.setText(_translate("MainWindow", "Refresh List"))
        self.label_2.setText(_translate("MainWindow", "Refresh rate (Hz):"))

