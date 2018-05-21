from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QSizePolicy
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import text
import networkx as nx
from settings import *
import numpy
from utils import rgb


class GraphCanvas(FigureCanvas):
    def __init__(self, parent=None, title=''):
        fig = Figure()
        fig.set_facecolor("none")
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.ax = self.figure.add_subplot(111)
        self.title = title
        self.ax.set_title(self.title)
        fig.tight_layout()
        self.G = nx.Graph()
        self.ax.patch.set_alpha(0)
        self.pos = nx.random_layout(self.G)
        self.txt = self.ax.text(0.5, 0.9, '', transform=self.ax.transAxes, bbox=dict(facecolor='green', alpha=0.5),
                                horizontalalignment='center')

    def set_nodes(self, nodes=[]):
        self.G.add_path(nodes)
        pos = dict()
        for node in nodes:
            pos.update({node: POSITIONS[node]})
        self.pos = pos

    def get_nodes(self):
        return self.G.nodes()

    def plot(self, edges=[], length=None):
        self.ax.clear()
        self.G.add_edges_from(edges)
        if length:
            length = ' (' + str(round(length, 2)) + ')'
        else:
            length = ''
        self.ax.set_title(self.title + length)

        if edges:
            ordered_nodes = [e[0] for e in edges] + [edges[-1][1]]
            positions = [ordered_nodes.index(c) for c in CITIES]
            colors = [COLORS[p] for p in positions]
        else:
            colors = ['red'] * 10
        nx.draw_networkx_nodes(self.G, self.pos, cmap=plt.get_cmap('jet'), node_size=300, ax=self.ax, node_color=colors)
        nx.draw_networkx_labels(self.G, self.pos, ax=self.ax)
        nx.draw_networkx_edges(self.G, self.pos, cmap=plt.get_cmap('jet'), edgelist=edges, arrows=False, ax=self.ax,
                               edge_color='b')
        self.ax.patch.set_alpha(0)
        self.draw()


class HistoryCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure()
        fig.set_facecolor("none")
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.ax = self.figure.add_subplot(111)
        # fig.tight_layout()
        self.txt = self.ax.text(0.5, 0.9, '', transform=self.ax.transAxes, bbox=dict(facecolor='green', alpha=0.5),
                                horizontalalignment='center')
        self.ax.patch.set_alpha(0)
        self.y_lim = ()

    def plot(self, max_hist, avg_hist, min_hist):
        # self.ax.cla()
        try:
            x = range(len(max_hist))
            self.ax.lines[0].set_data(x, max_hist)
            self.ax.lines[1].set_data(x, avg_hist)
            self.ax.lines[2].set_data(x, min_hist)
        except IndexError:
            print('był index error')
            self.ax.plot(max_hist, 'o-', markersize=2, label='Maximum')  # Lots of overhead. Do once.
            self.ax.plot(avg_hist, 'o-', markersize=2, label='Average')  # Lots of overhead. Do once.
            self.ax.plot(min_hist, 'o-', markersize=2, label='Minimum')  # Lots of overhead. Do once.

        # self.y_lim = self.ax.get_ylim()
        if min_hist and max_hist:
            self.ax.set_ylim([0.9 * min(min_hist), 1.1 * max(max_hist)])
            self.txt.set_text(
                'Maximum = {}, Minimum = {}, Average = {}'.format(round(max_hist[-1], 2), round(min_hist[-1], 2),
                                                                  round(avg_hist[-1], 2)))
        self.ax.relim()
        self.ax.legend(loc=3, bbox_to_anchor=(0., 1.0, 1., .102), mode='expand', ncol=3)
        self.ax.autoscale_view(True, True, True)
        self.draw()
        # self.ax.plot(max_history, style + 'go', linewidth=6, markeredgecolor='yellow', markeredgewidth=1)
        # self.ax.plot(avg_history, style + 'co', linewidth=3, markeredgecolor='black', markeredgewidth=1)
        # self.ax.plot(min_history, style + 'ro', linewidth=0.8, markeredgecolor='black', markeredgewidth=1)
