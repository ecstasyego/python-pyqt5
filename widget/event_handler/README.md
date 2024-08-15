## Event Handler

- Keyboard
  - keyPressEvent
  - keyReleaseEvent
- Mouse
  - mouseDoubleClickEvent
  - mouseMoveEvent
  - mousePressEvent
  - mouseReleaseEvent
- Window
  - moveEvent
  - resizeEvent	

```python
from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QtWidgets.QVBoxLayout()) # LAYOUT
        self.setGeometry(300, 300, 300, 200)

    def keyPressEvent(self, e):
        pass
    def keyReleaseEvent(self, e):
        pass
    def mouseDoubleClickEvent(self, e):
        pass
    def mousePressEvent(self, e):
        pass
    def mouseReleaseEvent(self, e):
        pass
    def mouseMoveEvent(self, e):
        pass
    def moveEvent(self, e):
        pass
    def resizeEvent(self, e):
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
```
