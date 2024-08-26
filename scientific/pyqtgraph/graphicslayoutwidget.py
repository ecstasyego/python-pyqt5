from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import numpy as np

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # WIDGETS
        widget = pg.GraphicsLayoutWidget()
        ax00 = widget.addPlot(row=1, col=1, colspan=2)
        ax10 = widget.addPlot(row=2, col=1, colspan=2)
        ax20 = widget.addPlot(row=3, col=1)
        ax21 = widget.addPlot(row=3, col=2)

        ax00.plot([1,4,2,4,3,5])
        ax10.plot([1,4,2,4,3,5])
        ax20.plot([1,4,2,4,3,5])
        ax21.plot([1,4,2,4,3,5])

        ax00.setLabel(axis='bottom', text='x')
        ax00.setLabel(axis='left', text='y')
        ax00.setTitle("plot-1")
        ax00.showGrid(x=True, y=True)

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
