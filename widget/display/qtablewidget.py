from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # WIDGETS
        self.widgets = dict()
        self.widgets['widget1'] = QtWidgets.QTableWidget()
        self.widgets['widget1'].setRowCount(20)
        self.widgets['widget1'].setColumnCount(4)
        for i in range(20):
            for j in range(4):
                self.widgets['widget1'].setItem(i, j, QtWidgets.QTableWidgetItem(str(i+j)))
        self.widgets['widget1'].horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # LAYOUTS
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.widgets['widget1'])
        layout.addStretch(1)

        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

    def callback(self):
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
