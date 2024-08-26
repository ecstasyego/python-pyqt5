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

        # ANNOTATIONS
        arrow = pg.ArrowItem(pos=(999, y[999]), angle=-180, tipAngle=60, headLen=20, headWidth=10, pen=pg.mkPen('r', width=2), brush='r')
        text = pg.TextItem(text="Hello PyQtGraph", color='r', anchor=(0.5, 0.5)); text.setPos(500, y[500])
        label = pg.LabelItem("This is a <b>LabelItem</b><br>with <i>HTML</i> formatting", color='w', size='14pt', anchor=(0.5, 0.5)); label.setPos(0, y[0])
        widget.addItem(arrow)
        widget.addItem(text)
        widget.addItem(label)

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
