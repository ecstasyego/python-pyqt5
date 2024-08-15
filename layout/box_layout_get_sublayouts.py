from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(QtWidgets.QHBoxLayout())
        layout.addLayout(QtWidgets.QHBoxLayout())
        layout.addLayout(QtWidgets.QHBoxLayout())
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)

        # sublayout = layout.itemAt(index).layout()
        sublayouts = list()
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if item is not None:
                sublayout = item.layout()
                if sublayout is not None:
                    sublayouts.append(sublayout)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
