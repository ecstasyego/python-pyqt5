from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # WIDGETS
        self.widgets = dict()
        self.widgets['widget1'] = QtWidgets.QComboBox(self)
        self.widgets['widget2'] = QtWidgets.QStatusBar(self)

        self.widgets['widget1'].addItem('Option1')
        self.widgets['widget1'].addItem('Option2')
        self.widgets['widget1'].addItem('Option3')
        self.widgets['widget1'].addItem('Option4')

        # LAYOUTS
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.widgets['widget1'])
        layout.addStretch(1)
        layout.addWidget(self.widgets['widget2'])
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

    def callback(self):
        status_widget = self.get_widgets()[-1]
        status_widget.showMessage("CallBack", 1000)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
