## Timer

```python
from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # TIME
        time = QtCore.QTime.currentTime().toString('HH:mm:ss')

        # WIDGETS
        widget = QtWidgets.QLabel(self)
        widget.setText(f'Current Time: {time}')

        # LAYOUT
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget)
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
```
