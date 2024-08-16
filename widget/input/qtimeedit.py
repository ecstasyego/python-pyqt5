from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # WIDGETS: Declaration
        self.widgets = dict()
        self.widgets['widget1'] = QtWidgets.QTimeEdit(self)
        self.widgets['widget2'] = QtWidgets.QStatusBar()

        # WIDGETS: Properties
        self.widgets['widget1'].setTime(QtCore.QTime.currentTime())
        self.widgets['widget1'].setTimeRange(QtCore.QTime(3, 00, 00), QtCore.QTime(23, 30, 00))
        self.widgets['widget1'].setDisplayFormat('hh:mm:ss')
        self.widgets['widget1'].timeChanged.connect(self.callback)

        # LAYOUTS
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.widgets['widget1'])
        layout.addStretch(1)
        layout.addWidget(self.widgets['widget2'])
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

    def callback(self):
        time = self.widgets['widget1'].time().toString('HH:mm:ss')
        self.widgets['widget2'].showMessage(f"Current Time: {time}", 1000)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
