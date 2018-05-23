# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 595)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 901, 551))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.map_widget = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.map_widget.setObjectName("map_widget")
        self.horizontalLayout.addWidget(self.map_widget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.size_input = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.size_input.setObjectName("size_input")
        self.verticalLayout.addWidget(self.size_input)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.iterations_input = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.iterations_input.setObjectName("iterations_input")
        self.verticalLayout.addWidget(self.iterations_input)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.mutation_input = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        self.mutation_input.setObjectName("mutation_input")
        self.verticalLayout.addWidget(self.mutation_input)
        self.start_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.start_button.setMinimumSize(QtCore.QSize(0, 40))
        self.start_button.setObjectName("start_button")
        self.verticalLayout.addWidget(self.start_button)
        self.stop_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.stop_button.setMinimumSize(QtCore.QSize(0, 40))
        self.stop_button.setObjectName("stop_button")
        self.verticalLayout.addWidget(self.stop_button)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 22))
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
        self.label.setText(_translate("MainWindow", "Population size:"))
        self.label_2.setText(_translate("MainWindow", "Iterations number:"))
        self.label_3.setText(_translate("MainWindow", "Mutation probablilty:"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.stop_button.setText(_translate("MainWindow", "Reset"))

