from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # TIMER
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.callback)
        self.timer.start(1000) # update time: 1000ms = 1s

        # WIDGETS
        self.widgets = dict()
        self.widgets['label'] = QtWidgets.QLabel(self)

        # LAYOUT
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.widgets['label'])
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

    def callback(self):
        time = QtCore.QTime.currentTime().toString('HH:mm:ss')
        self.widgets['label'].setText(f'Current Time: {time}')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
