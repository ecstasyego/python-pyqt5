from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        widget = QtWidgets.QToolBox()
        widget.addItem(QtWidgets.QWidget(), "ITEM1")
        widget.addItem(QtWidgets.QWidget(), "ITEM2")
        
        layout.addWidget(widget)
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
