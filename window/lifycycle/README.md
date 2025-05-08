# lifecycle

```python
from PyQt5 import QtCore, QtGui, QtWidgets


class Widget(QtWidgets.QWidget):
    signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setLayout(QtWidgets.QVBoxLayout())
        QtCore.QTimer.singleShot(0, self.signal.emit)


class CentralWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(Widget())
        self.setLayout(layout)

        self.layout().itemAt(0).widget().signal.connect(lambda: print("ACTIVITY"))


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        centralwidget = CentralWidget()
        self.setCentralWidget(centralwidget)
        self.setMenuBar(QtWidgets.QMenuBar(self))
        self.setStatusBar(QtWidgets.QStatusBar(self))
        self.setGeometry(300, 300, 300, 200)
        QtCore.QMetaObject.connectSlotsByName(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
```
