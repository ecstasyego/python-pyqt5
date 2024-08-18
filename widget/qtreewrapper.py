from abc import *

class OTreeWrapper(metaclass=ABCMeta):
    def __init__(self, node=None, note=None):
        self.node = node
        self.note = note
        self.generation = 0
        self.ascendants = list([''])
        self.name = 'ROOT'
        
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
        - PARENT: {self.__parent.name if hasattr(self, 'parent') else None}
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
        self.tree = list([self.name])
        children = cls.posterity(self)
        while children:
            _children = list()
            for child in children:
                self.tree.append('.'.join(child.ascendants + [child.name]))
                _children.extend(cls.posterity(child))
            children = _children
            
    @classmethod
    def posterity(cls, self):
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
        
    @abstractmethod
    def connection(self, child):
        pass
        
class QTreeWrapper(OTreeWrapper):
    def connection(self, child):
        pass
        
qtree = QTreeWrapper()
qtree.a = QTreeWrapper()
qtree.a.a = QTreeWrapper()
qtree.a.b = QTreeWrapper()
qtree.a.b.a = QTreeWrapper()
qtree.a.b.b = QTreeWrapper()
qtree.a.b.b.a = QTreeWrapper()
qtree.a.c = QTreeWrapper()
qtree.a.d = QTreeWrapper()
qtree.b = QTreeWrapper()
qtree.b.a = QTreeWrapper()
qtree.b.b = QTreeWrapper()
qtree.b.c = QTreeWrapper()
QTreeWrapper.progeny(qtree)

print(qtree.a.b.b.a)
print(qtree)
print(qtree.tree)
