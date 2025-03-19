from PyQt5 import QtCore, QtGui, QtWidgets

class Sender(QtCore.QObject):
    signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def send_signal(self, message):
        self.signal.emit(message)

class Receiver(QtCore.QObject):
    def __init__(self):
        super().__init__()

    def receive_signal(self, message):
        print(f"Signal received with message: {message}")

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # SIGNAL
        self.sender = Sender()
        self.receiver = Receiver()
        self.sender.signal.connect(self.receiver.receive_signal)

        # WIDGET
        self.button = QtWidgets.QPushButton("Send Signal")
        self.button.clicked.connect(self.callback)

        # LAYOUT
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)
        self.setGeometry(300, 300, 300, 200)

    def callback(self):
        self.sender.send_signal("Hello from Sender!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
