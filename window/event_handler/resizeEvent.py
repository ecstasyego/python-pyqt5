from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Window Title')
        self.setGeometry(300, 300, 300, 200)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self.windowState() == QtCore.Qt.WindowMaximized:
            print("Window is maximized!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
