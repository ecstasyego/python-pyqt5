from PyQt5 import QtCore, QtGui, QtWidgets

class Worker(QtCore.QThread):
    signal = QtCore.pyqtSignal(int)

    def __init__(self):
        super().__init__()

    def run(self):
        self.signal.emit(42)

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.worker = Worker()
        self.worker.signal.connect(lambda *values: print(values))
        self.worker.start()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
