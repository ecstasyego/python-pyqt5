from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QtWidgets.QVBoxLayout()) # LAYOUT
        self.setGeometry(300, 300, 300, 200)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.callback()
        elif event.key() == QtCore.Qt.Key_Tab:
            self.callback()
        elif event.key() == QtCore.Qt.Key_Escape:
            self.close()
        elif event.key() == QtCore.Qt.Key_F:
            self.showFullScreen()
        elif event.key() == QtCore.Qt.Key_N:
            self.showNormal()
        elif event.modifiers() == QtCore.Qt.ShiftModifier:
            self.callback()
        elif event.modifiers() == QtCore.Qt.ControlModifier:
            self.callback()
        elif event.modifiers() == QtCore.Qt.AltModifier:
            self.callback()

    def callback(self):
        pass
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
