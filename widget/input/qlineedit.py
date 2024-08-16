from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # WIDGETS: Declaration
        self.widgets = dict()
        self.widgets['widget1'] = QtWidgets.QLineEdit(self)
        self.widgets['widget2'] = QtWidgets.QStatusBar()

        # WIDGETS: Properties
        self.widgets['widget1'].textChanged[str].connect(self.callback)

        # LAYOUTS
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.widgets['widget1'])
        layout.addStretch(1)
        layout.addWidget(self.widgets['widget2'])
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

    def callback(self):
        text = self.widgets['widget1'].text()
        self.widgets['widget2'].showMessage(f"Current Text: {text}", 1000)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
