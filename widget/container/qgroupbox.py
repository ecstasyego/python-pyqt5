from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        widget = QtWidgets.QGroupBox()
        widget.setLayout(QtWidgets.QVBoxLayout())
        
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
