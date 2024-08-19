from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        widget = QtWidgets.QMdiArea(self)
        button = QtWidgets.QPushButton("PRESS")
        button.clicked.connect(self.callback)
        self.widget = widget

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget)
        layout.addWidget(button)
        self.setLayout(layout)

    def callback(self):
        sub_window = QtWidgets.QMdiSubWindow()
        sub_window.setWidget(QtWidgets.QLabel('LABEL'))
        sub_window.setWindowTitle(f"MDI")
        self.widget.addSubWindow(sub_window)

        sub_window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
