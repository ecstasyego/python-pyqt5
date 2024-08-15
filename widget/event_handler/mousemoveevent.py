from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)

        # WIDGETS
        self.widgets = dict()
        self.widgets['widget'] = QtWidgets.QStatusBar(self)

        # LAYOUT
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.widgets['widget'])
        layout.addStretch(1)
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

    def mouseMoveEvent(self, e):
        x = e.x(); y = e.y()
        self.widgets['widget'].showMessage(f'X: {x}, Y: {y}', 1000)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
