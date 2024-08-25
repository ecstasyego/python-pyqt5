from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QtWidgets.QVBoxLayout()) # LAYOUT
        self.setGeometry(300, 300, 300, 200)

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        pos = event.pos()
        button = event.button()

        if button == QtCore.Qt.LeftButton:
            button_name = 'Left'
        elif button == QtCore.Qt.RightButton:
            button_name = 'Right'
        elif button == QtCore.Qt.MiddleButton:
            button_name = 'Middle'
        else:
            button_name = 'Unknown'

        print(f"Mouse {button_name} button pressed at: ({pos.x()}, {pos.y()})")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
