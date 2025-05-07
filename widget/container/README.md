## Widget and Layout
```python
from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(QtWidgets.QWidget()) # INDEX: 0
        layout.addLayout(QtWidgets.QVBoxLayout()) # INDEX: 1

        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

        widget = self.layout().itemAt(0).widget(); print(widget.__class__.__name__)
        layout = self.layout().itemAt(1).layout(); print(layout.__class__.__name__)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
```
