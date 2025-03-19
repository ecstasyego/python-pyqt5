from PyQt5 import QtCore, QtGui, QtWidgets

class Worker(QtCore.QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        self.msleep(3000)

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.worker = Worker()
        self.worker.start()
        self.worker.wait() # JOIN

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
