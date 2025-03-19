from PyQt5 import QtCore, QtGui, QtWidgets

class Worker(QtCore.QRunnable):
    def __init__(self):
        super().__init__()

    def run(self):
        QtCore.QThread.sleep(3)

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.worker = Worker()
        self.pool = QtCore.QThreadPool.globalInstance()
        self.pool.start(self.worker)
        self.pool.waitForDone()  # JOIN


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
