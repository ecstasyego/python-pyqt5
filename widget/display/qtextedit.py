from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        widget = QtWidgets.QTextEdit()
        widget.setReadOnly(True)
      
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget)

        self.setLayout(layout) # LAYOUT
        self.setGeometry(300, 300, 300, 200)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
