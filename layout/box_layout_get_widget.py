from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(QtWidgets.QWidget())
        layout.addWidget(QtWidgets.QWidget())
        layout.addWidget(QtWidgets.QWidget())
      
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

        # widget = layout.itemAt(index).widget()
        widget0 = layout.itemAt(0).widget()
        widget1 = layout.itemAt(1).widget()
        widget2 = layout.itemAt(2).widget()

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
