from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # WIDGETS: Declaration
        self.widgets = dict()
        self.widgets['widget1'] = QtWidgets.QStatusBar(self)
        self.widgets['widget2'] = QtWidgets.QStatusBar(self)
        self.widgets['widget3'] = QtWidgets.QStatusBar(self)

        # WIDGETS: Properties
        self.widgets['widget1'].showMessage("status1", 1000) # milliseconds
        self.widgets['widget2'].showMessage("status2", 2000) # milliseconds
        self.widgets['widget3'].showMessage("status3", 3000) # milliseconds

        # LAYOUTS
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.widgets['widget1'])
        layout.addWidget(self.widgets['widget2'])
        layout.addWidget(self.widgets['widget3'])
        layout.addStretch(1)
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
