from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setMinimumSize(100, 50) # width, height
        self.setMaximumSize(300, 100) # width, height
        
        width = self.size().width()
        height = self.size().height()
        size = QtCore.QSize(width, height)
        sizef = QtCore.QSizeF(width, height)
        self.setMinimumSize(size) # QtCore.QSize
        self.setMaximumSize(size) # QtCore.QSize
      
        self.setLayout(QtWidgets.QVBoxLayout())
        self.setGeometry(300, 300, 300, 200)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
