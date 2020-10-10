from collections import namedtuple

A = namedtuple('A',['x','y','z'])
a = A(1,2,3)
print(a)
a = a._replace(x=4)
print(a)
