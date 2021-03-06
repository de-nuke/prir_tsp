# -*- coding: utf-8 -*-
from PyQt5 import QtCore
from mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QVBoxLayout, QLabel
import sys
import random
from utils import parse_input, qbytearray_to_str, parse_output
from plots import PlotCanvas
from functools import partial
import pprint
import copy
import time

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.move(10, 10)
        self.statusbar.hide()

        filename = sys.argv[1]
        with open(filename) as f:
            text = f.read()
            info = parse_input(text)
            self.info = info
            self.initial_info = copy.deepcopy(info)

        self.plot_layout = QVBoxLayout(self.map_widget)
        self.map_plot = PlotCanvas(title="Map of cities")
        self.plot_layout.addWidget(self.map_plot)
        self.map_plot.draw_map(''.join(info['cities'].keys()), info['cities'], only_cities=True)
        #self.label_5.setText(pprint.pformat(self.info, indent=2))
        self.updateInfoSection(self.info)
        self.start_time = 0
        self.end_time = 0
        self.size_input.setValue(info['size'])
        self.iterations_input.setValue(info['iterations'])
        self.mutation_input.setValue(info['mutation_probability'])

        self.process = QtCore.QProcess()
        self.start_button.clicked.connect(self.start_click)
        self.size_input.valueChanged.connect(partial(self.updateInfo, 'size'))
        self.iterations_input.valueChanged.connect(partial(self.updateInfo, 'iterations'))
        self.mutation_input.valueChanged.connect(partial(self.updateInfo, 'mutation_probability'))
        self.processes_input.valueChanged.connect(partial(self.updateInfo, 'processes'))
        self.reset_button.clicked.connect(self.reset)

    def start_click(self):
        with open('x', 'w') as f:
            f.write(parse_output(self.info))
        self.start_button.setEnabled(False)
        self.process.setProcessChannelMode(QtCore.QProcess.MergedChannels)
        self.process.readyReadStandardOutput.connect(self.readStdOutput)
        n = str(self.info['processes']) if 'processes' in self.info else "4"
        divide = self.divide_population.isChecked()
        self.process.start("mpiexec", ["-n", n, "/usr/bin/python3", "ga_engine.py", "x", str(divide)])
        self.start_time = time.time()


    def updateInfo(self, key, value):
        self.info[key] = value if key == 'cities' else round(value, 4)
        #self.label_5.setText(pprint.pformat(self.info, indent=2))
        self.updateInfoSection(self.info)


    def readStdOutput(self):
        self.end_time = time.time()
        output = qbytearray_to_str(self.process.readAllStandardOutput())
        print(output)
        self.updateGUI(output)
        self.start_button.setEnabled(True)
    
    def updateGUI(self, output):
        if output and 'BEST_PATH' in output and len(output.split()) == 3:
            value = output.split()[1]
            path = output.split()[2]
            self.map_plot.draw_map(path, self.info['cities'], length=value)
        self.time_label.setText(str(round(self.end_time - self.start_time, 2)) + "sek.")

    def reset(self):
        self.start_time = 0
        self.end_time = 0
        self.time_label.setText("")
        self.reset_button.setEnabled(False)
        self.info = copy.deepcopy(self.initial_info)
        #self.label_5.setText(pprint.pformat(self.info, indent=2))
        self.updateInfoSection(self.info)
        self.size_input.setValue(int(self.info['size']))
        self.mutation_input.setValue(float(self.info['mutation_probability']))
        self.iterations_input.setValue(int(self.info['iterations']))
        self.processes_input.setValue(int(self.info['processes']))
        self.process.terminate()
        if not self.process.waitForFinished(2000):
            self.process.kill()
        self.map_plot.draw_map(''.join(self.info['cities'].keys()), self.info['cities'], only_cities=True)
        self.reset_button.setEnabled(True)
    

    def updateInfoSection(self, info):
        self.info_list.clear()
        for key in info:
            if key != 'cities':
                self.info_list.addItem("{}: {}".format(key, info[key]))
        
        self.info_list.addItem("Cities:")
        for city in info['cities']:
            self.info_list.addItem("{}: {}".format(city, info['cities'][city]))
            
    def __del__(self):
        self.process.terminate()
        if not self.process.waitForFinished(10000):
            self.process.kill()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    x = MainWindow()
    x.show()

    sys.exit(app.exec_())
