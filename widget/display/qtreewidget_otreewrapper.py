from PyQt5 import QtCore, QtGui, QtWidgets

class OTreeWrapper:
    def __init__(self, node=None):
        self.node = node

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, other):
        self.__parent = other

    @classmethod
    def progeny(cls, self):
        members = list(filter(lambda x: not x.startswith('_OTreeWrapper__') and x != 'parent' and x != 'name', dir(self)))
        self.children = dict(map(lambda x: (x, getattr(self, x)), filter(lambda x: isinstance(getattr(self, x), cls), members)))
        if len(self.children):
            for name, child in self.children.items():
                child.parent = self
                child.name = name
                return cls.progeny(child)
        else:
            return


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        root = OTreeWrapper(QtWidgets.QTreeWidget())
        root.a = OTreeWrapper(QtWidgets.QTreeWidgetItem(root.node, ["Root 1", "Root item description"]))
        root.b = OTreeWrapper(QtWidgets.QTreeWidgetItem(root.node, ["Root 2", "Root item description"]))
        root.a.a = OTreeWrapper(QtWidgets.QTreeWidgetItem(root.a.node, ["Child 1", "Child item description"]))
        root.a.b = OTreeWrapper(QtWidgets.QTreeWidgetItem(root.a.node, ["Child 2", "Another child item description"]))
        root.b.a = OTreeWrapper(QtWidgets.QTreeWidgetItem(root.b.node, ["Child 3", "Child item under second root"]))
        OTreeWrapper.progeny(root)

        # WIDGETS
        widget = root.node
        widget.setHeaderLabels(["Name", "Description"])

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
