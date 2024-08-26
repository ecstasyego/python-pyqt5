from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import numpy as np
import pandas as pd
import datetime

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # DATA
        x = pd.date_range(end='2022-12-31', periods=1000, freq='D').astype(int) // 10**9
        y = np.random.normal(size=1000)

        # WIDGETS
        widget = pg.PlotWidget(axisItems={'bottom': pg.DateAxisItem()})
        widget.plot(x, y)
        
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
