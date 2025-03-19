from PyQt5 import QtCore

class Sender(QtCore.QObject):
    # [1] signal.connect: signal.connect(lambda *values: print(values))
    # [2] signal.emit
    signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def send_signal(self):
        self.signal.emit("Hello, World!")

class Receiver(QtCore.QObject):
    def __init__(self):
        super().__init__()

    def receive_signal(self, *values):
        print(values)

receiver = Receiver()
sender = Sender()
sender.signal.connect(receiver.receive_signal)
sender.send_signal()
