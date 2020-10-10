import gc


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

n1 = Node(1)
n2 = Node(2)
print (n1, n2)
print('-1'*10)

n1.add_child(n2)
del n1
del n2
print('-2'*10)

gc.collect()
print('-3'*10)

# 64
print(gc.garbage)
print('-4'*10)