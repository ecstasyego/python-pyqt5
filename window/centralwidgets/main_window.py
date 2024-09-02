from PyQt5 import QtCore, QtGui, QtWidgets

class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLayout(QtWidgets.QVBoxLayout())
        main_window = self.parent()

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        centralwidget = Widget(self)
        self.setCentralWidget(centralwidget)
        self.setMenuBar(QtWidgets.QMenuBar(self))
        self.setStatusBar(QtWidgets.QStatusBar(self))
        self.setGeometry(300, 300, 300, 200)
        QtCore.QMetaObject.connectSlotsByName(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
