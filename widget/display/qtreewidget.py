from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # WIDGETS
        widget = QtWidgets.QTreeWidget()
        widget.setHeaderLabels(["Name", "Description"])
        root1 = QtWidgets.QTreeWidgetItem(widget, ["Root 1", "Root item description"])
        root2 = QtWidgets.QTreeWidgetItem(widget, ["Root 2", "Root item description"])
        child1 = QtWidgets.QTreeWidgetItem(root1, ["Child 1", "Child item description"])
        child2 = QtWidgets.QTreeWidgetItem(root1, ["Child 2", "Another child item description"])
        child3 = QtWidgets.QTreeWidgetItem(root2, ["Child 3", "Child item under second root"])

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
