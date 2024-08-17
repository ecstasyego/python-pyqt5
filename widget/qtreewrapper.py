from abc import *

class OTreeWrapper(metaclass=ABCMeta):
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
        
    @abstractmethod
    def connection(self, child):
        pass
        
class QTreeWrapper(OTreeWrapper):
    def connection(self, child):
        pass
        
root = QTreeWrapper()
root.a = QTreeWrapper()
root.a.a = QTreeWrapper()
root.a.b = QTreeWrapper()
root.a.b.a = QTreeWrapper()
root.a.b.b = QTreeWrapper()
root.a.b.b.a = QTreeWrapper()
root.a.c = QTreeWrapper()
root.a.d = QTreeWrapper()
root.b = QTreeWrapper()
root.b.a = QTreeWrapper()
root.b.b = QTreeWrapper()
root.b.c = QTreeWrapper()
QTreeWrapper.progeny(root)

print(root.a.b.b.a)
