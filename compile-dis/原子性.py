def x():
    a = []
    a.append(1)

def y():
    a = 1
    a+=1

def z():
    a = 1
    b = a
    print(b)

import dis
dis.dis(x)
print('---')
dis.dis(y)
print('---')
dis.dis(z)
