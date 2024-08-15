## Input Widgets

```python
from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # Widgets
        widget1 = QtWidgets.QWidget()
        widget2 = QtWidgets.QWidget()
        widget3 = QtWidgets.QWidget()

        # Layout
        layout = QtWidgets.QVBoxLayout()
        layout.addStretch(1)
        layout.addWidget(widget1)
        layout.addWidget(widget2)
        layout.addWidget(widget3)
        layout.addStretch(1)
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
```
