from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # WIDGETS: Declaration
        self.widgets = dict()
        self.widgets['widget1'] = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        self.widgets['widget2'] = QtWidgets.QStatusBar(self)
        # WIDGETS: Properties
        self.widgets['widget1'].setRange(0, 50)
        self.widgets['widget1'].setSingleStep(2)
        self.widgets['widget1'].valueChanged.connect(self.callback)

        # LAYOUT
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.widgets['widget1'])
        layout.addStretch(1)
        layout.addWidget(self.widgets['widget2'])
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

    def callback(self):
        value = self.widgets['widget1'].value()
        self.widgets['widget2'].showMessage(f"Current value: {value}", 1000)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
