# -*- utf-8 -*-
from PyQt5 import QtCore
from mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QVBoxLayout
import sys
import random
from utils import parse_input
from plots import PlotCanvas


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.move(10, 10)
        self.statusbar.hide()

        #self.start_button.clicked.connect(self.fun)
        
        filename = sys.argv[1]
        text = open(filename).read()
        info = parse_input(text)
        print(info)

        self.plot_layout = QVBoxLayout(self.map_widget)
        self.map_plot = PlotCanvas()
        self.plot_layout.addWidget(self.map_plot)
        self.map_plot.draw_map(''.join(info['cities'].keys()), info['cities'], only_cities=True)

        self.size_input.setValue(info['size'])
        self.iterations_input.setValue(info['iterations'])
        self.mutation_input.setValue(info['mutation_probability'])

        self.process = QtCore.QProcess()
        self.start_button.clicked.connect(self.start_click)

    def start_click(self):
        self.start_button.disabled = True
        self.process.setProcessChannelMode(QtCore.QProcess.MergedChannels)
        self.process.readyReadStandardOutput.connect(self.readStdOutput)
        self.process.start("df -h")
        
    def readStdOutput(self):
        print(self.process.readAllStandardOutput())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    x = MainWindow()
    x.show()

    sys.exit(app.exec_())
