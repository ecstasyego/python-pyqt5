from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # WIDGETS
        widget = QtWidgets.QPushButton('Button', self)
        widget.setFixedWidth(100) # W
        widget.setFixedHeight(30) # H
        widget.setFixedSize(100, 30) # W, H

        widget.size()
        widget.width()
        widget.height()
        widget.geometry()
        widget.geometry().x()
        widget.geometry().y()
        widget.geometry().width()
        widget.geometry().height()

        # LAYOUTS
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget)

        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200) # X, Y, W, H


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
