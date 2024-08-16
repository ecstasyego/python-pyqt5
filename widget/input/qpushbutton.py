from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # WIDGETS
        self.widgets = dict()
        self.widgets['widget1'] = QtWidgets.QPushButton('&Button1', self)
        self.widgets['widget2'] = QtWidgets.QPushButton(self)
        self.widgets['widget3'] = QtWidgets.QPushButton('Button3', self)
        self.widgets['widget4'] = QtWidgets.QStatusBar(self)

        self.widgets['widget1'].setCheckable(True)
        self.widgets['widget1'].toggle()
        self.widgets['widget2'].setText('Button&2')
        self.widgets['widget3'].setEnabled(False)

        # LAYOUTS
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.widgets['widget1'])
        layout.addWidget(self.widgets['widget2'])
        layout.addWidget(self.widgets['widget3'])
        layout.addStretch(1)
        layout.addWidget(self.widgets['widget4'])
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

    def callback(self):
        self.widgets['widget4'].showMessage("CallBack", 1000)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
