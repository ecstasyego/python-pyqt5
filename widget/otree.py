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
            
root = OTreeWrapper()
root.a = OTreeWrapper()
root.a.a = OTreeWrapper()
root.a.b = OTreeWrapper()
root.a.b.a = OTreeWrapper()
root.a.b.b = OTreeWrapper()
root.a.b.b.a = OTreeWrapper()
root.a.c = OTreeWrapper()
root.a.d = OTreeWrapper()
OTreeWrapper.progeny(root)

print(root.a.parent)
print(root.a.children)
