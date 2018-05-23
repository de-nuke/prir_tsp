# -*- coding: utf-8 -*-
from PyQt5 import QtCore
from mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QVBoxLayout
import sys
import random
from utils import parse_input, qbytearray_to_str, parse_output
from plots import PlotCanvas


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.move(10, 10)
        self.statusbar.hide()

        #self.start_button.clicked.connect(self.fun)
        
        filename = sys.argv[1]
        with open(filename) as f:
            text = f.read()
            info = parse_input(text)
            self.info = info

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
        with open('x', 'w') as f:
            f.write(parse_output(self.info))
        self.start_button.enabled = True
        self.process.setProcessChannelMode(QtCore.QProcess.MergedChannels)
        self.process.readyReadStandardOutput.connect(self.readStdOutput)
        self.process.start("mpiexec", ["-n", "4", "/usr/bin/python3", "ga_engine.py", "x"])
        
    def readStdOutput(self):
        output = qbytearray_to_str(self.process.readAllStandardOutput())
        if output and 'BEST_PATH' in output and len(output.split()) == 3:
            path = output.split()[-1]
            value = output.split()[1]
            self.map_plot.draw_map(path, self.info['cities'])
            self.label_4.setText(value)
    

    def __del__(self):
        self.process.terminate()
        if not self.process.waitForFinished(10000):
            self.process.kill()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    x = MainWindow()
    x.show()

    sys.exit(app.exec_())
