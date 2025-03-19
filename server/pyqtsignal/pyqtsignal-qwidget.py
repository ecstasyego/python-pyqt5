from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    signal = QtCore.pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.setLayout(QtWidgets.QVBoxLayout()) # LAYOUT
        self.setGeometry(300, 300, 300, 200)

        receive_signal = lambda *values: print(values)
        self.signal.connect(receive_signal)
        self.signal.emit(42)
        self.signal.disconnect(receive_signal)
        self.signal.emit(42)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
