from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import numpy as np

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # WIDGETS
        widget = pg.PlotWidget()

        # PLOT
        x = np.arange(1000)
        y = np.random.normal(size=1000)

        # BAR GRAPH
        bar_x = np.arange(len(y))
        bar_y = np.abs(y)
        widget.addItem(pg.BarGraphItem(x=bar_x, height=bar_y, width=0.5, brush='g'))

        # LAYOUTS
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget)
        layout.addStretch(1)

        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
