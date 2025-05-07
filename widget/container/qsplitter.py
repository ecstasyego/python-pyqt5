from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # WIDGETS
        widget = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        widget.addWidget(QtWidgets.QWidget())
        widget.addWidget(QtWidgets.QLabel("EEE"))
        widget.addWidget(QtWidgets.QWidget())
        widget.widget(2).setLayout(QtWidgets.QVBoxLayout())
        widget.widget(2).layout().addWidget(QtWidgets.QSplitter(QtCore.Qt.Horizontal))
        widget.widget(2).layout().itemAt(0).widget().addWidget(QtWidgets.QLabel("EEE0"))
        widget.widget(2).layout().itemAt(0).widget().addWidget(QtWidgets.QLabel("EEE1"))

        # LAYOUTS
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget)
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

        # INITIALS
        widget.setSizes([100]*widget.count())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
