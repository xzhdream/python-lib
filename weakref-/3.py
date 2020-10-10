import weakref

class Node(object):
    def __init__(self, data):
        self.data = data
        self._parent = None
        self.children = []

    @property
    def parent(self):
        return None if self._parent is None else self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node, callback)

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def __del__(self):
        print('__del__',self)


def callback(ref):
    print ('__del__1', ref)


n1 = Node(0)
n2 = Node(2)
print (n1,n2)

n1.add_child(n2)
del n1

print('****')
