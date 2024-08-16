from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.pbar_step = 0

        # TIMER
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.callback)
        self.timer.start(1000) # update time: 1000ms = 1s

        # WIDGETS
        self.widgets = dict()
        self.widgets['widget1'] = QtWidgets.QProgressBar(self)

        # LAYOUTS
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.widgets['widget1'])
        layout.addStretch(1)
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

    def callback(self):
        self.pbar_step += 20
        if self.pbar_step > 100:
            self.pbar_step = 0
        self.widgets['widget1'].setValue(self.pbar_step)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
