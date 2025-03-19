from PyQt5 import QtCore

class Sender(QtCore.QObject):
    # [1] signal.connect: signal.connect(lambda *values: print(values))
    # [2] signal.emit
    signal = QtCore.pyqtSignal(int)

    def __init__(self):
        super().__init__()

    def send_signal(self):
        self.signal.emit(42)

sender = Sender()
sender.signal.connect(lambda *values: print(values))
sender.send_signal()
