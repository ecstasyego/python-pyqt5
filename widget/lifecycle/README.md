
## LifeCycle
```python
from PyQt5 import QtCore, QtGui, QtWidgets

class Widget(QtWidgets.QWidget):
    signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setLayout(QtWidgets.QVBoxLayout())
        QtCore.QTimer.singleShot(0, self.signal.emit)


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(Widget())
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

        self.layout().itemAt(0).widget().signal.connect(self.callback)

    def callback(self):
        layout = self.layout()
        widget = layout.itemAt(0).widget()

        layout.removeWidget(widget)
        widget.deleteLater()
        layout.addWidget(QtWidgets.QLabel("New Widget"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
```
