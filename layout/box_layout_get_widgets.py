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
        widgets = list()
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if item is not None:
                widgets.append(item.widget())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
