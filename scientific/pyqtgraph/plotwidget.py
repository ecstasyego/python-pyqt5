from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import numpy as np

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # WIDGETS        
        x = np.arange(1000)
        y = np.random.normal(size=1000)
        
        widget = pg.PlotWidget()
        widget.plot(x, y)
        
        widget.setBackground('w')
        widget.setTitle("Title")
        widget.setLabel('bottom', 'X')
        widget.setLabel('left', 'Y')
        widget.addLegend()
        widget.showGrid(x=True, y=True)
        
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
