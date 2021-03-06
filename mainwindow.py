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
        MainWindow.resize(1043, 667)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1031, 611))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
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
        self.size_input.setMinimum(2)
        self.size_input.setMaximum(10000)
        self.size_input.setObjectName("size_input")
        self.verticalLayout.addWidget(self.size_input)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.iterations_input = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.iterations_input.setMinimum(1)
        self.iterations_input.setMaximum(10000)
        self.iterations_input.setObjectName("iterations_input")
        self.verticalLayout.addWidget(self.iterations_input)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.mutation_input = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        self.mutation_input.setDecimals(4)
        self.mutation_input.setMaximum(1.0)
        self.mutation_input.setSingleStep(0.0001)
        self.mutation_input.setObjectName("mutation_input")
        self.verticalLayout.addWidget(self.mutation_input)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.processes_input = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.processes_input.setMinimum(1)
        self.processes_input.setMaximum(10)
        self.processes_input.setProperty("value", 4)
        self.processes_input.setObjectName("processes_input")
        self.verticalLayout.addWidget(self.processes_input)
        self.multiply_population = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.multiply_population.setChecked(True)
        self.multiply_population.setObjectName("multiply_population")
        self.verticalLayout.addWidget(self.multiply_population)
        self.divide_population = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.divide_population.setObjectName("divide_population")
        self.verticalLayout.addWidget(self.divide_population)
        self.start_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.start_button.setMinimumSize(QtCore.QSize(0, 40))
        self.start_button.setObjectName("start_button")
        self.verticalLayout.addWidget(self.start_button)
        self.reset_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.reset_button.setMinimumSize(QtCore.QSize(0, 40))
        self.reset_button.setObjectName("reset_button")
        self.verticalLayout.addWidget(self.reset_button)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.info_list = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.info_list.setObjectName("info_list")
        self.verticalLayout.addWidget(self.info_list)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 620, 241, 21))
        self.label_7.setObjectName("label_7")
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(250, 620, 131, 21))
        self.time_label.setText("")
        self.time_label.setObjectName("time_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1043, 22))
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
        self.label_6.setText(_translate("MainWindow", "Num. of processes"))
        self.multiply_population.setText(_translate("MainWindow", "Multiply population on processes"))
        self.divide_population.setText(_translate("MainWindow", "Divide population between processes"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.reset_button.setText(_translate("MainWindow", "Reset"))
        self.label_4.setText(_translate("MainWindow", "Info: "))
        self.label_7.setText(_translate("MainWindow", "Genetic algorithm execution time: "))

