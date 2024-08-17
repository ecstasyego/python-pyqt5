class OTree:
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
        members = list(filter(lambda x: not x.startswith('_OTree__') and x != 'parent' and x != 'name', dir(self)))
        self.children = dict(map(lambda x: (x, getattr(self, x)), filter(lambda x: isinstance(getattr(self, x), cls), members)))
        if len(self.children):
            for name, child in self.children.items():
                child.parent = self
                child.name = name
                return cls.progeny(child)
        else:
            return

root = OTree()
root.a = OTree()
root.a.a = OTree()
root.a.b = OTree()
root.a.b.a = OTree()
root.a.b.b = OTree()
root.a.b.b.a = OTree()
root.a.c = OTree()
root.a.d = OTree()
OTree.progeny(root)

print(root.a.parent)
print(root.a.children)
