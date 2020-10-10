def a():
    yield 1
    yield 2
    return 3

def b():
    x = yield from a()
    yield x

t = b()
x = t.send(None)
print(x)

x = t.send(None)
print(x)