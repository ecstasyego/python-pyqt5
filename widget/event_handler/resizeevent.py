from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QtWidgets.QVBoxLayout()) # LAYOUT
        self.setGeometry(300, 300, 300, 200)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        new_size = event.size()
        print(f"Widget resized to {new_size.width()}x{new_size.height()}")

        if self.isMaximized():
            print(f"Maximized widget, resized to {new_size.width()}x{new_size.height()}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
