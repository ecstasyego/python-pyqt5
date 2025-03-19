from PyQt5 import QtCore, QtGui, QtWidgets

class Sender(QtCore.QObject):
    signal = QtCore.pyqtSignal(int)

    def __init__(self):
        super().__init__()

    def send_signal(self):
        self.signal.emit(42)

class Window(QtWidgets.QWidget):
    signal = QtCore.pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.setLayout(QtWidgets.QVBoxLayout()) # LAYOUT
        self.setGeometry(300, 300, 300, 200)

        self.sender = Sender()
        self.sender.signal.connect(lambda *values: print(values))
        self.sender.send_signal()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
