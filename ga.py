from PyQt5 import QtCore
from w2 import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QVBoxLayout
import sys
from Plots import GraphCanvas, HistoryCanvas
from ApplicationLogic import ApplicationLogic

appStyle = """
    QLabel {
        font-size: 14px;
    }
    
    QSpinBox {
        font-size: 14px;
    }
    
    QDoubleSpinBox {
        font-size: 14px;
    }
    
    QPushButton {
        padding-top: 10px;
        padding-bottom: 10px;
        font-size: 14px;
    }
"""


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.move(10, 10)
        self.setStyleSheet(appStyle)
        # self.progressBar.hide()
        self.statusbar.hide()

        self.right_plot_layout = QVBoxLayout(self.right_frame)
        self.graph_max_canvas = GraphCanvas(title='Longest path')
        self.right_plot_layout.addWidget(self.graph_max_canvas)

        self.left_plot_layout = QVBoxLayout(self.left_frame)
        self.graph_min_canvas = GraphCanvas(title='Shortest path')
        self.left_plot_layout.addWidget(self.graph_min_canvas)

        self.top_plot_layout = QVBoxLayout(self.top_frame)
        self.history_canvas = HistoryCanvas()
        self.top_plot_layout.addWidget(self.history_canvas)

        self.app = ApplicationLogic(self)
        self.apply_btn.clicked.connect(self.app.apply_click)
        self.start_btn.clicked.connect(self.app.start_auto_click)
        self.next_btn.clicked.connect(self.app.next_step_click)
        self.reset_btn.clicked.connect(self.app.reset_click)
        self.stop_btn.clicked.connect(self.app.pause)
        self.show_path_btn.clicked.connect(self.app.show_path)

        self.iterations.valueChanged.connect(self.app.change_iterations)
        self.mutation_prob.valueChanged.connect(self.app.change_mutation_prob)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    x = MainWindow()
    x.show()

    sys.exit(app.exec_())
