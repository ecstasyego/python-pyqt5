from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # WIDGETS
        widget = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        widget.addWidget(QtWidgets.QWidget())
        widget.addWidget(QtWidgets.QWidget())
        widget.addWidget(QtWidgets.QSplitter(QtCore.Qt.Horizontal))
        widget.addWidget(QtWidgets.QFrame())
        widget.addWidget(QtWidgets.QFrame())

        # LAYOUTS
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget)
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
