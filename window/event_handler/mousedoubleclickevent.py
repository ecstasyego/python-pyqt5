from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Window Title')
        self.setGeometry(300, 300, 300, 200)
        self.maximized = False

    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent):
        if event.button() == QtCore.Qt.LeftButton:
            if not self.maximized:
                self.showMaximized()
            else:
                self.showNormal()
            self.maximized = not self.maximized
        super().mouseDoubleClickEvent(event)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
