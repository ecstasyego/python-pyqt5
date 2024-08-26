from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import numpy as np

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.callback)
        self.timer.start(500)  # Update every 500 ms

        # WIDGETS
        widget = pg.PlotWidget()

        # PLOT
        x = np.arange(1000)
        y = np.random.normal(size=1000)        
        self.plotitem = widget.plot(x, y)

        # LAYOUTS
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget)
        layout.addStretch(1)

        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

    def callback(self):
        x = np.arange(1000)
        y = np.random.normal(size=1000)
        self.plotitem.setData(x, y)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
