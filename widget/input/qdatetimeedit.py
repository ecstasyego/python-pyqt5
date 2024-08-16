from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # WIDGETS: Declaration
        self.widgets = dict()
        self.widgets['widget1'] = QtWidgets.QDateTimeEdit(self)
        self.widgets['widget2'] = QtWidgets.QStatusBar()

        # WIDGETS: Properties
        self.widgets['widget1'].setDateTime(QtCore.QDateTime.currentDateTime())
        self.widgets['widget1'].setDateTimeRange(QtCore.QDateTime(1900, 1, 1, 00, 00, 00), QtCore.QDateTime(2100, 1, 1, 00, 00, 00))
        self.widgets['widget1'].setDisplayFormat('yyyy-MM-dd hh:mm:ss')
        self.widgets['widget1'].dateTimeChanged.connect(self.callback)

        # LAYOUTS
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.widgets['widget1'])
        layout.addStretch(1)
        layout.addWidget(self.widgets['widget2'])
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

    def callback(self):
        datetime = self.widgets['widget1'].dateTime().toString('yyyy-MM-dd HH:mm:ss')
        self.widgets['widget2'].showMessage(f"Current Time: {datetime}", 1000)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
