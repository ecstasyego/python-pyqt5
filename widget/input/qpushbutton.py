from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        widget1 = QtWidgets.QPushButton('&Button1', self)
        widget1.setCheckable(True)
        widget1.toggle()
        widget2 = QtWidgets.QPushButton(self)
        widget2.setText('Button&2')
        widget3 = QtWidgets.QPushButton('Button3', self)
        widget3.setEnabled(False)

        layout = QtWidgets.QVBoxLayout()
        layout.addStretch(1)
        layout.addWidget(widget1)
        layout.addWidget(widget2)
        layout.addWidget(widget3)
        layout.addStretch(1)
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
