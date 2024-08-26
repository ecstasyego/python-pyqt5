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
        widget.plot(x, y)

        arrow = pg.ArrowItem(angle=-180, tipAngle=60, headLen=10, pen=None, brush='r')
        arrow.setPos(999, y[999])
        widget.addItem(arrow)

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
