from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMenuBar(QtWidgets.QMenuBar(self))
        self.menuBar().addMenu('&File')
        self.menuBar().addMenu('&Edit')
        self.menuBar().addMenu('&Settings')
        self.menuBar().addMenu('&Help')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
