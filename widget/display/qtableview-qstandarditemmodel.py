from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # ITEM MODEL
        model = QtGui.QStandardItemModel(5,3)
        model.setHorizontalHeaderLabels(['COLUMN1', 'COLUMN2', 'COLUMN3'])
        model.setVerticalHeaderLabels(['ROW1', 'ROW2', 'ROW3', 'ROW4', 'ROW5'])

        for row in range(model.rowCount()):
            for col in range(model.columnCount()):
                item = QtGui.QStandardItem(f'Item {row+1}.{col+1}')
                model.setItem(row, col, item)

        model.appendRow([QtGui.QStandardItem('Item 6.1'), QtGui.QStandardItem('Item 6.2'), QtGui.QStandardItem('Item 6.3')])
        model.appendRow([QtGui.QStandardItem('Item 7.1'), QtGui.QStandardItem('Item 7.2'), QtGui.QStandardItem('Item 7.3')])
        model.appendRow([QtGui.QStandardItem('Item 8.1'), QtGui.QStandardItem('Item 8.2'), QtGui.QStandardItem('Item 8.3')])
        model.appendRow([QtGui.QStandardItem('Item 9.1'), QtGui.QStandardItem('Item 9.2'), QtGui.QStandardItem('Item 9.3')])
        model.appendRow([QtGui.QStandardItem('Item 10.1'), QtGui.QStandardItem('Item 10.2'), QtGui.QStandardItem('Item 10.3')])

        # WIDGETS
        widget = QtWidgets.QTableView()
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
