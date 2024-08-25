from PyQt5 import QtCore, QtGui, QtWidgets

class CustomTitleBar(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        widgets = dict()
        widgets['titlebar'] = QtWidgets.QLabel("Custom Title Bar")
        widgets['titlebar'].setFont(QtGui.QFont("Arial", 16, QtGui.QFont.Bold))
        widgets['titlebar'].setAlignment(QtCore.Qt.AlignCenter)
        widgets['closebutton'] = QtWidgets.QPushButton("X")
        widgets['closebutton'].clicked.connect(self.close_window)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(widgets['titlebar'])
        layout.addWidget(widgets['closebutton'])
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)
        self.setStyleSheet("background-color: #2E8B57; color: white;")

    def close_window(self):
        if self.parent():
            self.parent().close()


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setGeometry(100, 100, 800, 600)

        self.setCentralWidget(QtWidgets.QWidget(self))
        self.setMenuWidget(CustomTitleBar(self))

if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
