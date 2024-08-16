from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # ITEM MODEL
        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(['NAME1', 'NAME2', 'NAME3'])

        root_item = model.invisibleRootItem()
        root_item.appendRow([QtGui.QStandardItem('Item 1.1'), QtGui.QStandardItem('Item 1.2'), QtGui.QStandardItem('Item 1.3')])
        root_item.appendRow([QtGui.QStandardItem('Item 2.1'), QtGui.QStandardItem('Item 2.2'), QtGui.QStandardItem('Item 2.3')])
        root_item.appendRow([QtGui.QStandardItem('Item 3.1'), QtGui.QStandardItem('Item 3.2'), QtGui.QStandardItem('Item 3.3')])

        # WIDGETS
        widget = QtWidgets.QTreeView()
        widget.setUniformRowHeights(True)
        widget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        widget.setModel(model)

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
