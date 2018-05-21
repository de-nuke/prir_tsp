from Algorithm import Population
from PyQt5.QtCore import QThread, pyqtSignal
import sys
import matplotlib.pyplot as plt


def av(x):
    """
    Average of values in X sequence.
    """
    return round(sum(x) / len(x), 2)


class Plotter(QThread):
    min5, max5, avg5, b5 = [], [], [], []
    counter = 1

    def __init__(self, app):
        QThread.__init__(self)
        self.app = app
        self.main = app.main
        self.population = app.population
        self.isRunning = False
        self.mode = 'ENDLESS'
        self.shortest_path = None
        self.shortest_path_length = sys.maxsize

    def activate(self, mode):
        self.isRunning = True
        self.mode = mode

    def stop(self):
        self.isRunning = False

    def run(self):
        while True:
            if self.isRunning and self.app.current_iteration <= self.app.iterations_limit:

                self.population.reproduce().cross().mutate()
                self.app.current_iteration += 1

                sp = self.population.shortest_path()
                lp = self.population.longest_path()
                self.app.max_hist.append(lp.length)
                self.app.avg_hist.append(self.population.average_path_length())
                self.app.min_hist.append(sp.length)

                if sp.length < self.shortest_path_length:
                    self.shortest_path_length = sp.length
                    self.shortest_path = sp
                    self.main.show_path_btn.setDisabled(False)
                    self.main.when_found.setText('(after {} iterations)'.format(str(len(self.app.max_hist))))

                self.main.graph_max_canvas.plot(lp.edges, length=lp.length)
                self.main.graph_min_canvas.plot(sp.edges, length=sp.length)
                self.main.history_canvas.plot(self.app.max_hist, self.app.avg_hist, self.app.min_hist)

                self.main.shortest_current.setText(str(round(sp.length, 4)))
                self.main.shortest_current_for.setText(
                    ' -> '.join(list(str(sp)))
                )
                self.main.shortest_ever.setText(str(round(self.shortest_path_length, 4)))
                self.main.shortest_ever_for.setText(
                    ' -> '.join(list(str(self.shortest_path)))
                )
                self.main.progress_bar_text.setText(
                    'Iteration: {}/{}'.format(len(self.app.max_hist), self.app.iterations_limit))

                # For reporting purposes. Prints table content for LaTeX document
                if self.app.current_iteration == self.app.iterations_limit:
                    print(self.counter, '&', round(self.app.min_hist[-1], 2), '&', round(self.app.max_hist[-1], 2), '&',
                          round(self.app.avg_hist[-1], 2), '&', round(sp.length, 2), '\\\\\\hline')
                    self.min5.append(self.app.min_hist[-1])
                    self.max5.append(self.app.max_hist[-1])
                    self.avg5.append(self.app.avg_hist[-1])
                    self.b5.append(sp.length)
                    if self.counter == 5:
                        print('&avg. min:&avg. max:&avg. mean:&avg. best:\\\\\\hline')
                        print('&', av(self.min5), '&', av(self.max5), '&', av(self.avg5), '&', av(self.b5),
                              '\\\\\\hline')
                        self.min5, self.max5, self.avg5, self.b5 = [], [], [], []
                        self.counter = 0
                    self.counter += 1

                if self.mode == 'SINGLE_STEP':
                    self.isRunning = False


class ApplicationLogic:
    def __init__(self, main_window):
        self.main = main_window
        self.population = Population()
        # self.population.set_progress_bar(self.main.progressBar, self.main.progress_bar_text)
        self.max_hist = []
        self.min_hist = []
        self.avg_hist = []
        self.is_running = False
        self.thread = Plotter(self)
        self.iterations_limit = self.main.iterations.value()
        self.current_iteration = 1
        self.main.stop_btn.clicked.connect(self.thread.stop)

        self.main.graph_max_canvas.set_nodes(self.population.cities)
        self.main.graph_min_canvas.set_nodes(self.population.cities)

    def apply_click(self):
        self.main.apply_btn.setText('Applying...')
        # self.main.progressBar.show()
        self.population.set_parameters(
            size=self.main.size.value(),
            iterations=self.main.iterations.value(),
            mutation_prob=self.main.mutation_prob.value()
        )

        self.iterations_limit = self.main.iterations.value()

        sp = self.population.shortest_path()
        lp = self.population.longest_path()

        self.main.graph_max_canvas.plot(sp.edges)
        self.main.graph_min_canvas.plot(lp.edges)

        self.max_hist.append(lp.length)
        self.avg_hist.append(self.population.average_path_length())
        self.min_hist.append(sp.length)
        self.main.history_canvas.plot(self.max_hist, self.avg_hist, self.min_hist)

        self.main.shortest_current.setText(str(round(sp.length, 4)))
        self.main.shortest_current_for.setText(
            ' -> '.join(list(str(sp)))
        )
        self.main.shortest_ever.setText(str(round(sp.length, 4)))
        self.main.shortest_ever_for.setText(
            ' -> '.join(list(str(sp)))
        )

        self.main.apply_btn.setText('Apply')
        # self.main.progressBar.hide()

        self.main.reset_btn.setDisabled(False)
        self.main.next_btn.setDisabled(False)
        self.main.start_btn.setDisabled(False)
        # self.main.stop_btn.setDisabled(False)
        self.main.apply_btn.setDisabled(True)

        self.main.size.setDisabled(True)
        # self.next_step_click()
        # self.main.mutation_prob.setDisabled(True)

    def start_auto_click(self):
        if not self.thread.isRunning:
            self.thread.start()
        self.thread.activate('ENDLESS')
        self.main.start_btn.setDisabled(True)
        self.main.next_btn.setDisabled(True)
        self.main.stop_btn.setDisabled(False)

    def next_step_click(self):
        if not self.thread.isRunning:
            self.thread.start()
        self.thread.activate('SINGLE_STEP')

    def reset_click(self):
        self.thread.stop()
        self.main.reset_btn.setDisabled(True)
        self.main.next_btn.setDisabled(True)
        self.main.start_btn.setDisabled(True)
        self.main.stop_btn.setDisabled(True)
        self.main.apply_btn.setDisabled(False)
        self.main.graph_max_canvas.plot()
        self.main.graph_min_canvas.plot()
        self.main.history_canvas.plot([], [], [])
        self.main.history_canvas.txt.set_text('')
        self.main.history_canvas.draw()
        # self.main.size.setValue(2)
        # self.main.iterations.setValue(100)
        # self.main.mutation_prob.setValue(0.0010)
        self.iterations_limit = 100
        self.current_iteration = 1
        self.avg_hist = []
        self.max_hist = []
        self.min_hist = []
        self.population = Population()
        self.main.size.setDisabled(False)
        # self.main.mutation_prob.setDisabled(False)
        # self.thread = Plotter(self)
        self.thread.population = self.population
        self.thread.isRunning = False
        self.thread.mode = 'ENDLESS'
        self.thread.shortest_path = None
        self.thread.shortest_path_length = sys.maxsize

        self.main.show_path_btn.setDisabled(True)
        self.main.shortest_current.setText('')
        self.main.shortest_current_for.setText('')
        self.main.shortest_ever.setText('')
        self.main.shortest_ever_for.setText('')

    def change_iterations(self, value):
        self.iterations_limit = value

    def change_mutation_prob(self, value):
        self.population.mutation_prob = value

    def pause(self):
        self.thread.stop()
        self.main.start_btn.setDisabled(False)
        self.main.next_btn.setDisabled(False)
        self.main.stop_btn.setDisabled(True)

    def show_path(self):
        pos = self.thread.shortest_path.positions
        nodes = self.thread.shortest_path.nodes
        labels, x, y = [], [], []

        for n in nodes:
            x.append(pos[n][0])
            y.append(pos[n][1])
            labels.append(n + ' ' + str(pos[n]))

        plt.plot(x, y, 'o-')
        for label, x, y in zip(labels, x, y):
            plt.annotate(label, xy=(x, y), xytext=(25, -4), textcoords='offset points', ha='right', va='top')
        plt.show()
