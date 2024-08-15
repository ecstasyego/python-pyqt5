from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QGridLayout()
        layout.addWidget(QtWidgets.QWidget(), 0, 0)
        layout.addWidget(QtWidgets.QWidget(), 1, 0)
        layout.addWidget(QtWidgets.QWidget(), 2, 0)
        layout.addLayout(QtWidgets.QVBoxLayout(), 0, 1)
        layout.addLayout(QtWidgets.QVBoxLayout(), 1, 1)
        layout.addLayout(QtWidgets.QVBoxLayout(), 2, 1)

        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
