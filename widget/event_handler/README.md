## Event Handler
[QEvent](https://doc.qt.io/qt-5/qevent.html)  

- [QKeyEvent](https://doc.qt.io/qt-5/qkeyevent.html)
  - keyPressEvent
  - keyReleaseEvent
- [QMouseEvent](https://doc.qt.io/qt-5/qmouseevent.html)
  - mouseDoubleClickEvent
  - mouseMoveEvent
  - mousePressEvent
  - mouseReleaseEvent
- Window
  - moveEvent
  - resizeEvent
  - closeEvent
  - showEvent
  - hideEvent
- Focus
  - focusInEvent
  - focusOutEvent
- Drag
  - dragEnterEvent
  - dragMoveEvent
  - dragLeaveEvent
  - dropEvent
- Timer
  - timerEvent
- File
  - dropEvent
- ETC
  - contextMenuEvent
  - wheelEvent
  - enterEvent
  - leaveEvent


```python
from PyQt5 import QtCore, QtGui, QtWidgets

class Communicate(QtCore.QObject):
    signal = QtCore.pyqtSignal()

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.c = Communicate()
        self.c.signal.connect

        self.setLayout(QtWidgets.QVBoxLayout()) # LAYOUT
        self.setGeometry(300, 300, 300, 200)

    def keyPressEvent(self, e):
        self.c.signal.emit

    def keyReleaseEvent(self, e):
        self.c.signal.emit

    def mouseDoubleClickEvent(self, e):
        self.c.signal.emit

    def mousePressEvent(self, e):
        self.c.signal.emit

    def mouseReleaseEvent(self, e):
        self.c.signal.emit

    def mouseMoveEvent(self, e):
        self.c.signal.emit

    def moveEvent(self, e):
        self.c.signal.emit

    def resizeEvent(self, e):
        self.c.signal.emit

    def closeEvent(self, e):
        self.c.signal.emit

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
```
