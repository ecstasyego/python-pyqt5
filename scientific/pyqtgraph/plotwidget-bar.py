from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import numpy as np
import pandas as pd
import datetime

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # WIDGETS
        x = np.arange(20)
        y = np.random.randint(low=0, high=100, size=20)

        widget = pg.PlotWidget()
        widget.addItem(pg.BarGraphItem(x=x, height=y, width=0.3, pen=None, brush='b'))

        widget.setBackground('w')
        widget.setTitle("Title")
        widget.setLabel('bottom', 'X')
        widget.setLabel('left', 'Y')

        # LAYOUTS
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget)
        layout.addStretch(1)

        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

    def callback(self):
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
