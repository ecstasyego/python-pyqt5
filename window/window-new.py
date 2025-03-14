from PyQt5 import QtCore, QtGui, QtWidgets

class NewWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Support Window Title')
        self.setGeometry(300, 300, 300, 200)

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window Title')
        self.setGeometry(300, 300, 300, 200)

        button = QtWidgets.QPushButton("Open Support Window", self)
        button.clicked.connect(self.callback)
        self.setCentralWidget(button)

    def callback(self):
        self.new_window = NewWindow()
        self.new_window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
