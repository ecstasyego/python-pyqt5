from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import numpy as np

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # WIDGETS
        widget = pg.PlotWidget(axisItems={'left':pg.AxisItem(orientation='left'), 'bottom':pg.AxisItem(orientation='bottom')})
        widget.setBackground('w')
        widget.setTitle("Title")
        widget.setLabel('bottom', 'X')
        widget.setLabel('left', 'Y')
        widget.addLegend()
        widget.showGrid(x=True, y=True)

        # PLOT
        x = np.arange(1000)
        y = np.random.normal(size=1000)
        widget.plot(x=x, y=2*y,
                    symbol=['o', 't', 't1', 's', 'x'][0], symbolSize=5, symbolBrush='r', symbolPen=None,
                    pen=pg.mkPen(width=2, color='r'), name="plot1")
        widget.plot(x=x, y=1*y,
                    symbol=['o', 't', 't1', 's', 'x'][0], symbolSize=5, symbolBrush='b', symbolPen=None,
                    pen=pg.mkPen(width=2, color='b'), name="plot2")
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
