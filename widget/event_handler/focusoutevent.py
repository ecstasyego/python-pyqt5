from PyQt5 import QtCore, QtGui, QtWidgets

class PushButtonA(QtWidgets.QPushButton):
    def __init__(self, text=None, parent=None):
        super().__init__(text, parent)

    def focusInEvent(self, event):
        print("A: FocusInEvent")
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        print("A: FocusOutEvent")
        super().focusOutEvent(event)


class PushButtonB(QtWidgets.QPushButton):
    def __init__(self, text=None, parent=None):
        super().__init__(text, parent)

    def focusInEvent(self, event):
        print("B: FocusInEvent")
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        print("B: FocusOutEvent")
        super().focusOutEvent(event)

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        widget1 = PushButtonA("Button A")
        widget2 = PushButtonB("Button B")
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget1)
        layout.addWidget(widget2)

        self.setLayout(layout) # LAYOUT
        self.setGeometry(300, 300, 300, 200)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
