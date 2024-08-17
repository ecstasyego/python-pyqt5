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
        self.node.appendRow(child.node)


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # ITEM MODEL
        treeview = OTreeWrapper(QtWidgets.QTreeView())
        treeview.model = OTreeWrapper(QtGui.QStandardItemModel())
        treeview.model.root_item = OTreeWrapper(treeview.model.node.invisibleRootItem())
        treeview.model.root_item.category1 = OTreeWrapper(QtGui.QStandardItem('Category 1'))
        treeview.model.root_item.category2 = OTreeWrapper(QtGui.QStandardItem('Category 2'))
        treeview.model.root_item.category1.item1 = OTreeWrapper(QtGui.QStandardItem('Item 1.1'))
        treeview.model.root_item.category1.item2 = OTreeWrapper(QtGui.QStandardItem('Item 1.2'))
        treeview.model.root_item.category2.item1 = OTreeWrapper(QtGui.QStandardItem('Item 2.1'))
        treeview.model.root_item.category2.item2 = OTreeWrapper(QtGui.QStandardItem('Item 2.2'))
        treeview.model.root_item.category2.item3 = OTreeWrapper(QtGui.QStandardItem('Item 2.3'))
        treeview.model.root_item.category2.category1 = OTreeWrapper(QtGui.QStandardItem('Category 2.1'))
        treeview.model.root_item.category2.category1.item1 = OTreeWrapper(QtGui.QStandardItem('Item 2.1.1'))
        treeview.model.root_item.category2.category1.item2 = OTreeWrapper(QtGui.QStandardItem('Item 2.1.2'))
        treeview.model.root_item.category2.category1.item3 = OTreeWrapper(QtGui.QStandardItem('Item 2.1.3'))
        OTreeWrapper.progeny(treeview.model.root_item)

        # WIDGETS
        model = treeview.model.node
        model.setHorizontalHeaderLabels(['NAME'])

        widget = treeview.node
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

