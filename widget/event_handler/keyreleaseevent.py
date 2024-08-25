from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QtWidgets.QVBoxLayout()) # LAYOUT
        self.setGeometry(300, 300, 300, 200)

    def keyReleaseEvent(self, event: QtGui.QKeyEvent):
        key = event.key()
        text = event.text()
        print(f"Key released: {key} ({text})")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
