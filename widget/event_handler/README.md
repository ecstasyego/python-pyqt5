## Event Handler
[QEvent](https://doc.qt.io/qt-5/qevent.html)  

- event
  - [QKeyEvent](https://doc.qt.io/qt-5/qkeyevent.html)
    - keyPressEvent
    - keyReleaseEvent
  - [QMouseEvent](https://doc.qt.io/qt-5/qmouseevent.html)
    - mouseDoubleClickEvent
    - mouseMoveEvent
    - mousePressEvent
    - mouseReleaseEvent
      - contextMenuEvent
    - wheelEvent 
  - Window
    - moveEvent
    - resizeEvent
    - closeEvent
    - showEvent
    - hideEvent
  - Widget
    - changeEvent
    - enterEvent
    - leaveEvent
    - paintEvent
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

```python
from PyQt5 import QtCore

class Communicate(QtCore.QObject):
    signal_int = QtCore.pyqtSignal(int)
    signal_str = QtCore.pyqtSignal(str)
    signal_composite = QtCore.pyqtSignal(int, str, float)
    signals = QtCore.pyqtSignal((int,), (str,))

    def __init__(self):
        super().__init__()

    def emit_signal(self):
        self.signal_int.emit(42)
        self.signal_str.emit("Hello")
        self.signal_composite.emit(100, "World", 3.14)
        self.signals[int].emit(99)
        self.signals[str].emit("Hello, World!")

def receive_slot(*values):
    print(f"SIGNAL: {values}")

com = Communicate()
com.signal_int.connect(receive_slot)
com.signal_str.connect(receive_slot)
com.signal_composite.connect(receive_slot)
com.signals[int].connect(receive_slot)
com.signals[str].connect(receive_slot)
com.emit_signal()

com.signal_int.disconnect(receive_slot)
com.signal_str.disconnect(receive_slot)
com.signal_composite.disconnect(receive_slot)
com.signals[int].disconnect(receive_slot)
com.signals[str].disconnect(receive_slot)
com.emit_signal()
```

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
