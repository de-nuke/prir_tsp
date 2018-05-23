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
        self.map_plot.draw_map('ADBEFC', info['cities'])
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    x = MainWindow()
    x.show()

    sys.exit(app.exec_())
