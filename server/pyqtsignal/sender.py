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

com = Sender()
print("[Connection] Slot")
com.signal_int.connect(receive_signal)
com.signal_str.connect(receive_signal)
com.signal_composite.connect(receive_signal)
com.signals[int].connect(receive_signal)
com.signals[str].connect(receive_signal)
com.send_signal()

print("[Disconnection]")
com.signal_int.disconnect(receive_signal)
com.signal_str.disconnect(receive_signal)
com.signal_composite.disconnect(receive_signal)
com.signals[int].disconnect(receive_signal)
com.signals[str].disconnect(receive_signal)
com.send_signal()

print("[Connection] Lambda")
com.signal_int.connect(lambda *values: print(f"SIGNAL: {values}"))
com.signal_str.connect(lambda *values: print(f"SIGNAL: {values}"))
com.signal_composite.connect(lambda *values: print(f"SIGNAL: {values}"))
com.signals[int].connect(lambda *values: print(f"SIGNAL: {values}"))
com.signals[str].connect(lambda *values: print(f"SIGNAL: {values}"))
com.send_signal()
