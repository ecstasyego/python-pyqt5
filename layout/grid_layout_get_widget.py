from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QGridLayout()
        layout.addWidget(QtWidgets.QWidget(), 0, 0)
        layout.addWidget(QtWidgets.QWidget(), 1, 0)
        layout.addWidget(QtWidgets.QWidget(), 2, 0)
        layout.addWidget(QtWidgets.QWidget(), 0, 1)
        layout.addWidget(QtWidgets.QWidget(), 1, 1)
        layout.addWidget(QtWidgets.QWidget(), 2, 1)

        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

        # widget = layout.itemAt(index).widget()
        widget0 = layout.itemAt(0).widget()
        widget1 = layout.itemAt(1).widget()
        widget2 = layout.itemAt(2).widget()
        widget3 = layout.itemAt(3).widget()
        widget4 = layout.itemAt(4).widget()
        widget5 = layout.itemAt(5).widget()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
