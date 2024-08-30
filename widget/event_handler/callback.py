from PyQt5 import QtCore, QtGui, QtWidgets

class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.callback = None

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.callback()
        elif event.key() == QtCore.Qt.Key_Escape:
            self.close()
        elif event.key() == QtCore.Qt.Key_F:
            self.showFullScreen()
        elif event.key() == QtCore.Qt.Key_N:
            self.showNormal()

    def set_callback(self, callback):
        self.callback = callback

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        widget = Widget()
        widget.set_callback(self.callback)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget)

        self.setLayout(layout) # LAYOUT
        self.setGeometry(300, 300, 300, 200)

    def callback(self):
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
~                                                                                                                                                                      
