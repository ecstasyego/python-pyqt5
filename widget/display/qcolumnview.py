from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # ITEM MODEL
        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(['NAME'])

        root_item = model.invisibleRootItem()
        category1 = QtGui.QStandardItem('Category 1')
        category2 = QtGui.QStandardItem('Category 2')
        category2_1 = QtGui.QStandardItem('Subcategory 2.1')

        root_item.appendRow(category1)
        root_item.appendRow(category2)
        category1.appendRow(QtGui.QStandardItem('Item 1.1'))
        category1.appendRow(QtGui.QStandardItem('Item 1.2'))
        category2.appendRow(QtGui.QStandardItem('Item 2.1'))
        category2.appendRow(QtGui.QStandardItem('Item 2.2'))
        category2.appendRow(QtGui.QStandardItem('Item 2.3'))
        category2.appendRow(category2_1)
        category2_1.appendRow(QtGui.QStandardItem('Item 2.1.1'))
        category2_1.appendRow(QtGui.QStandardItem('Item 2.1.2'))
        category2_1.appendRow(QtGui.QStandardItem('Item 2.1.3'))

        # WIDGETS
        widget = QtWidgets.QColumnView()
        widget.setModel(model)

        # LAYOUTS
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget)
        layout.addStretch(1)

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
