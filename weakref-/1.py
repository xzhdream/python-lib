import time
import gc

# gc.set_debug(gc.DEBUG_LEAK)

class Node(object):

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def __del__(self):
        print ('__del__',self)

n = Node(0)
del n
print('1'*10)

n1 = Node(1)
n2 = Node(2)
n1.add_child(n2)
del n1
print('2'*10)

print(n2.parent)
print('3'*10)


