from collections import namedtuple
from weakref import ref

l = list()
_l = list()

# Point = namedtuple('Point', ['x', 'y'])
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y


def callback(ref):
    print ('__del__', ref)


for x in range(10):
    p = Point(x,x**2)
    t = ref(p,callback)
    print(t)
    l.append(t)
    _l.append(p)

print(len(l),l)
print(len(_l),_l)

t = _l[6]
del t,_l[6]

print(len(_l),_l)


# print(len(l),l)