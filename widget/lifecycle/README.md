
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

### QStackedWidget

```python
from PyQt5 import QtCore, QtGui, QtWidgets


class Widget0(QtWidgets.QWidget):
    signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        widget0 = QtWidgets.QLabel("PAGE0")
        widget1 = QtWidgets.QPushButton("PAGE0")
        widget1.clicked.connect(self.signal.emit)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget0)
        layout.addWidget(widget1)
        self.setLayout(layout)


class Widget1(QtWidgets.QWidget):
    signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        widget0 = QtWidgets.QLabel("PAGE1")
        widget1 = QtWidgets.QPushButton("PAGE1")
        widget1.clicked.connect(self.signal.emit)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget0)
        layout.addWidget(widget1)
        self.setLayout(layout)


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        widget0 = Widget0()
        widget1 = Widget1()
        widget0.signal.connect(self.callback0)
        widget1.signal.connect(self.callback1)

        self.widgets = QtWidgets.QStackedWidget()
        self.widgets.addWidget(widget0)
        self.widgets.addWidget(widget1)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.widgets)
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

    def callback0(self):
        self.widgets.setCurrentIndex(1)

    def callback1(self):
        self.widgets.setCurrentIndex(0)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
```
