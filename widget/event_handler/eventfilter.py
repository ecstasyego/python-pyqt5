from PyQt5 import QtCore, QtGui, QtWidgets

class CustomEventFilter(QtCore.QObject):
    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            print(f"Mouse button pressed on: {obj.objectName()}")
        return super().eventFilter(obj, event)

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.installEventFilter(CustomEventFilter(self))
        self.setLayout(QtWidgets.QVBoxLayout()) # LAYOUT
        self.setGeometry(300, 300, 300, 200)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
