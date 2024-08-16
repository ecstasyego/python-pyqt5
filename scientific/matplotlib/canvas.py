from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.fig = plt.Figure()

        # WIDGETS: Declaration
        self.widgets = dict()
        self.widgets['widget1'] = FigureCanvas(self.fig)
        self.widgets['widget2'] = QtWidgets.QLineEdit(self)
        self.widgets['widget3'] = QtWidgets.QPushButton('Draw', self)

        # WIDGETS: Properties
        self.widgets['widget3'].clicked.connect(self.callback)


        # LAYOUT: Declaration
        self.layouts = dict()
        self.layouts['layout0'] = QtWidgets.QHBoxLayout()
        self.layouts['layout1'] = QtWidgets.QVBoxLayout()
        self.layouts['layout2'] = QtWidgets.QVBoxLayout()

        # LAYOUT: Construction
        self.layouts['layout0'].addLayout(self.layouts['layout1'])
        self.layouts['layout0'].addLayout(self.layouts['layout2'])
        self.layouts['layout0'].setStretchFactor(self.layouts['layout1'], 1)
        self.layouts['layout0'].setStretchFactor(self.layouts['layout2'], 0)

        self.layouts['layout1'].addWidget(self.widgets['widget1'])
        self.layouts['layout2'].addWidget(self.widgets['widget2'])
        self.layouts['layout2'].addWidget(self.widgets['widget3'])
        self.layouts['layout2'].addStretch(1)

        layout = self.layouts['layout0']
        self.setLayout(layout)
        self.setGeometry(600, 200, 1200, 600)
        self.setWindowTitle("PyChart Viewer v0.1")

    def callback(self):
        self.fig.clf()
        ax = self.fig.add_subplot(111)
        ax.plot(np.random.normal(size=100).cumsum())
        ax.legend(loc='upper right')
        ax.grid()

        canvas = self.widgets['widget1']
        canvas.draw()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
