from PyQt5 import QtCore, QtGui, QtWidgets

class OTreeWrapper:
    def __init__(self, node=None):
        self.node = node
        self.generation = 0

    def __iter__(self):
        return self

    def __next__(self):
        return list(self.__sibling.values())[self.order+1]

    def __repr__(self):
        representation = f"""
        - NAME: {self.name}
        - ACCESS SPECIFIER: {'.'.join(self.ascendants)}.{self.name}
        - GENERATION: {self.generation} + 1
        - ASCENDANTS: {'.'.join(self.ascendants)}
        - PARENT: {self.parent.name}
        """
        return representation

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

    @property
    def sibling(self):
        return self.__sibling

    @sibling.setter
    def sibling(self, other):
        self.__sibling = other

    @classmethod
    def progeny(cls, self):
        children = cls.posterity(self)
        while children:
            _children = list()
            for child in children:
                _children.extend(cls.posterity(child))
            children = _children

    @classmethod
    def posterity(cls, self):
        if self.generation == 0:
            self.name = 'ROOT'

        members = list(filter(lambda x: not x.startswith('_OTreeWrapper__') and x != 'parent' and x != 'sibling' and x != 'name', dir(self)))
        self.children = dict(map(lambda x: (x, getattr(self, x)), filter(lambda x: isinstance(getattr(self, x), cls), members)))
        for order, (name, child) in enumerate(self.children.items()):
            child.parent = self
            child.generation = self.generation + 1
            child.ascendants = self.ascendants + [ self.name ] if self.generation else [ self.name ]
            child.name = name
            child.order = order
            child.sibling = self.children

            self.connection(child) # OTree Node Connection
        return self.children.values()

    def connection(self, child):
        self.node
        child.node


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
