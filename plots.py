from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.ticker import AutoMinorLocator, MultipleLocator


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, title=''):
        fig = Figure()
        #self.axes = fig.add_subplot(111)
        fig.set_facecolor("none")
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self.ax = self.figure.add_subplot(111)
        self.title = title
        self.ax.set_title(self.title)
        fig.tight_layout()
        self.mins = []
        self.maxes = []
        self.averages = []
        self.x_list = []
        self.y_list = []

    def clearData(self):
        self.ax.cla()
        self.mins = []
        self.maxes = []
        self.averages = []
        del self.x_list[:]
        del self.y_list[:]

        self.draw()

    def draw_map(self, path, cities, only_cities=False, length=None):
        self.x_list = []; self.y_list = []; labels = []
        for city in path:
            self.x_list.append(cities[city][0])
            self.y_list.append(cities[city][1])
        self.ax.cla()
        for i in range(len(path)):
            labels.append('{name}({x},{y})'.format(name=path[i], x = self.x_list[i], y = self.y_list[i]))
        self.ax.plot(self.x_list, self.y_list, 'bo')
        self.ax.plot(self.x_list, self.y_list, linestyle='-', linewidth = 0.8 if not only_cities else 0)
        for label, x, y in zip(labels, self.x_list, self.y_list):
            self.ax.annotate(label, xy=(x, y), xytext=(25,-4), textcoords='offset points', ha='right', va='top')
        if length:
            self.ax.set_title("Shortest path: {} ({})".format(path, round(float(length), 4)))
        else:
            self.ax.set_title(self.title)
        self.draw()

