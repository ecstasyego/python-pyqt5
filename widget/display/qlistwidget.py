from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # WIDGETS
        widget = QtWidgets.QListWidget()
        widget.addItem("Item 1.1")
        widget.addItem("Item 1.2")
        widget.addItem("Item 1.3")
        widget.addItem("Item 1.4")
        widget.addItem("Item 1.5")

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
                                                                                                                                                     65,25         Bot 
