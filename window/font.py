from PyQt5 import QtCore, QtGui, QtWidgets

class Widget(QtWidgets.QWidget):
    def __init__(self, other):
        super(Widget, self).__init__(other)
        widget = QtWidgets.QLabel('Hello, World!')
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget)
        self.setLayout(layout)

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        centralwidget = Widget(self)
        self.setCentralWidget(centralwidget)
        self.setMenuBar(QtWidgets.QMenuBar(self))
        self.setStatusBar(QtWidgets.QStatusBar(self))
        QtCore.QMetaObject.connectSlotsByName(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setFont(QtGui.QFont("Times New Roman", 12))

    window = Window()
    window.show()
    sys.exit(app.exec_())
