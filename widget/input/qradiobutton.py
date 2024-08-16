from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # WIDGETS
        self.widgets = dict()
        self.widgets['widget1'] = QtWidgets.QRadioButton("Option1", self);
        self.widgets['widget2'] = QtWidgets.QRadioButton(self);
        self.widgets['widget3'] = QtWidgets.QStatusBar()

        self.widgets['widget1'].setChecked(True)
        self.widgets['widget2'].setText("Option2")

        # LAYOUTS
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.widgets['widget1'])
        layout.addWidget(self.widgets['widget2'])
        layout.addStretch(1)
        layout.addWidget(self.widgets['widget3'])
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

    def callback(self):
        self.widgets['widget3'].showMessage("CallBack", 1000)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
