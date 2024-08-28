from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # ITEM MODEL
        model = QtGui.QStandardItemModel()
        model.appendRow(QtGui.QStandardItem('Item 1.1'))
        model.appendRow(QtGui.QStandardItem('Item 1.2'))
        model.appendRow(QtGui.QStandardItem('Item 1.3'))
        model.appendRow(QtGui.QStandardItem('Item 1.4'))
        model.appendRow(QtGui.QStandardItem('Item 1.5'))

        # WIDGETS
        widget = QtWidgets.QListView()
        widget.setModel(model)
        widget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

        # LAYOUTS
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget)
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
