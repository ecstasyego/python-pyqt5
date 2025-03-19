from PyQt5 import QtCore

class Sender(QtCore.QObject):
    signal_int = QtCore.pyqtSignal(int)
    signal_str = QtCore.pyqtSignal(str)
    signal_composite = QtCore.pyqtSignal(int, str, float)
    signals = QtCore.pyqtSignal((int,), (str,))

    def __init__(self):
        super().__init__()

    def send_signal(self):
        self.signal_int.emit(42)
        self.signal_str.emit("Hello")
        self.signal_composite.emit(100, "World", 3.14)
        self.signals[int].emit(99)
        self.signals[str].emit("Hello, World!")

def receive_signal(*values):
    print(f"SIGNAL: {values}")

sender = Sender()
print("[Connection] Slot")
sender.signal_int.connect(receive_signal)
sender.signal_str.connect(receive_signal)
sender.signal_composite.connect(receive_signal)
sender.signals[int].connect(receive_signal)
sender.signals[str].connect(receive_signal)
sender.send_signal()

print("[Disconnection]")
sender.signal_int.disconnect(receive_signal)
sender.signal_str.disconnect(receive_signal)
sender.signal_composite.disconnect(receive_signal)
sender.signals[int].disconnect(receive_signal)
sender.signals[str].disconnect(receive_signal)
sender.send_signal()

print("[Connection] Lambda")
sender.signal_int.connect(lambda *values: print(f"SIGNAL: {values}"))
sender.signal_str.connect(lambda *values: print(f"SIGNAL: {values}"))
sender.signal_composite.connect(lambda *values: print(f"SIGNAL: {values}"))
sender.signals[int].connect(lambda *values: print(f"SIGNAL: {values}"))
sender.signals[str].connect(lambda *values: print(f"SIGNAL: {values}"))
sender.send_signal()
