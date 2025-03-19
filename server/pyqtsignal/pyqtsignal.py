from PyQt5 import QtCore

class Communicate(QtCore.QObject):
    signal_int = QtCore.pyqtSignal(int)
    signal_str = QtCore.pyqtSignal(str)
    signal_composite = QtCore.pyqtSignal(int, str, float)
    signals = QtCore.pyqtSignal((int,), (str,))

    def __init__(self):
        super().__init__()

    def emit_signal(self):
        self.signal_int.emit(42)
        self.signal_str.emit("Hello")
        self.signal_composite.emit(100, "World", 3.14)
        self.signals[int].emit(99)
        self.signals[str].emit("Hello, World!")

def receive_slot(*values):
    print(f"SIGNAL: {values}")

com = Communicate()
print("[Connection] Slot")
com.signal_int.connect(receive_slot)
com.signal_str.connect(receive_slot)
com.signal_composite.connect(receive_slot)
com.signals[int].connect(receive_slot)
com.signals[str].connect(receive_slot)
com.emit_signal()

print("[Disconnection]")
com.signal_int.disconnect(receive_slot)
com.signal_str.disconnect(receive_slot)
com.signal_composite.disconnect(receive_slot)
com.signals[int].disconnect(receive_slot)
com.signals[str].disconnect(receive_slot)
com.emit_signal()

print("[Connection] Lambda")
com.signal_int.connect(lambda *values: print(f"SIGNAL: {values}"))
com.signal_str.connect(lambda *values: print(f"SIGNAL: {values}"))
com.signal_composite.connect(lambda *values: print(f"SIGNAL: {values}"))
com.signals[int].connect(lambda *values: print(f"SIGNAL: {values}"))
com.signals[str].connect(lambda *values: print(f"SIGNAL: {values}"))
com.emit_signal()
