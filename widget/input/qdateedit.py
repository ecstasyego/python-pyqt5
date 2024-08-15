from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # WIDGETS: Declaration
        self.widgets = dict()
        self.widgets['widget1'] = QtWidgets.QDateEdit(self)
        self.widgets['widget2'] = QtWidgets.QStatusBar()

        # WIDGETS: Properties
        self.widgets['widget1'].setDate(QtCore.QDate.currentDate())
        self.widgets['widget1'].setMinimumDate(QtCore.QDate(1900, 1, 1))
        self.widgets['widget1'].setMaximumDate(QtCore.QDate(2100, 12, 31))
        self.widgets['widget1'].setDateRange(QtCore.QDate(1900, 1, 1), QtCore.QDate(2100, 12, 31))
        self.widgets['widget1'].dateChanged.connect(self.callback)

        # LAYOUT
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.widgets['widget1'])
        layout.addStretch(1)
        layout.addWidget(self.widgets['widget2'])
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

    def callback(self):
        date = self.widgets['widget1'].date().toString('yyyy-MM-dd')
        self.widgets['widget2'].showMessage(f"Current Date: {date}", 1000)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
