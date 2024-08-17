from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # WIDGETS
        widget = QtWidgets.QTableWidget()
        widget.setRowCount(20)
        widget.setColumnCount(4)
        for i in range(widget.rowCount()):
            for j in range(widget.columnCount()):
                widget.setItem(i, j, QtWidgets.QTableWidgetItem(str(i+j)))
        widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # LAYOUTS
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget)
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
